#!/usr/bin/env python3

import pandas as pd

import sys
from flask import Flask, request

app = Flask(__name__, template_folder="")


data = {}

for version in ["98", "15"]:
    df = pd.read_csv("sfb98.tsv", sep="\t", header=None)
    df.columns = [
        "book_name",
        "book_abbr",
        "book_num",
        "chapter_num",
        "verse_num",
        "verse",
    ]
    df = df.set_index(["book_num", "chapter_num", "verse_num"])
    # for Matt 17:21
    df.verse.fillna("", inplace=True)

    data[version] = df

# case-insensitive
book_names = pd.Series(df.book_name.unique()).str.lower()
book_abbr = pd.Series(df.book_abbr.unique()).str.lower()


def book_lookup(ref):
    # s is something like 1 Mos 1:1, 1 Krön 1:1
    # first, we try to find the book_name or abbr

    for i, name in enumerate(book_names):
        if ref.startswith(name):
            return i, name

    # search abbrs
    for i, name in enumerate(book_abbr):
        if ref.startswith(name):
            return i, name

    raise ReferenceError("Can't find book: " + ref)


def lookup(ref, key):
    df = data[key]

    book_idx, book_name = book_lookup(ref)
    book_num = book_idx + 1
    # now, find the chapter / verse
    rest = ref.replace(book_name, "")
    if rest == "":
        return " ".join(df.loc[book_num, :, :].verse)

    rest = rest.split(":")
    chap_num = int(rest[0].strip())

    if len(rest) == 1:
        # only chapter supplied, 1 Mos 1
        verses = df.loc[book_num, chap_num, :].verse.values
    elif len(rest) == 2:
        verse_range = rest[1].strip().split("-")
        verse_lo = int(verse_range[0])
        if len(verse_range) == 1:
            # only one verse supplied, 1 Mos 1:1
            verses = [df.loc[book_num, chap_num, verse_lo].verse]
        else:
            # range supplied, 1 Mos 1:1-10
            verse_hi = int(verse_range[1])
            verses = df.loc[book_num, chap_num, verse_lo:verse_hi].verse.values
    else:
        raise ReferenceError("Can't find reference: " + "".join(rest))

    return " ".join(verses)


@app.route("/<reference>", methods=["GET"])
def idx(reference):
    if "sfb15" in request.args:
        key = "15"
    else:
        key = "98"

    try:
        return lookup(reference.lower(), key)
    except ReferenceError as e:
        return str(e), 404


port = sys.argv[1]
app.run("0.0.0.0", port=port)
