#!/usr/bin/env python3

import xml.etree.ElementTree as ET

abbr = ["1 Mos", "2 Mos", "3 Mos", "4 Mos", "5 Mos", "Jos", "Dom", "Rut", "1 Sam", "2 Sam", "1 Kung", "2 Kung", "1 Krön", "2 Krön", "Esr", "Neh", "Est", "Job", "Ps", "Ords", "Pred", "Höga v", "Jes", "Jer", "Klag", "Hes", "Dan", "Hos", "Joel", "Am", "Ob", "Jon", "Mik", "Nah", "Hab", "Sef", "Hagg", "Sak", "Mal", "Matt", "Mark", "Luk", "Joh", "Apg", "Rom", "1 Kor", "2 Kor", "Gal", "Ef", "Fil", "Kol", "1 Thess", "2 Thess", "1 Tim", "2 Tim", "Tit", "Filem", "Heb", "Jak", "1 Pet", "2 Pet", "1 Joh", "2 Joh", "3 Joh", "Jud", "Upp"]

root = ET.parse('/dev/stdin').getroot()

for book_id,b in enumerate(root.findall('b')):
    book_name = b.attrib['n']
    for c in b.findall('c'):
        chapter_id = str(c.attrib['n'])
        for v in c.findall('v'):
            verse_id = str(v.attrib['n'])
            verse = v.text if v.text is not None else ''
            verse = verse.replace('\n', '')
            s = '\t'.join([book_name, abbr[book_id], str(book_id+1), chapter_id, verse_id, verse])
            print(s)
