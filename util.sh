#!/usr/bin/env bash

URL=''
NAME="$1"

if [ "$NAME" = "sfb98" ]; then
    URL='http://www.folkbibeln.it/arkiv/SFB_1998_Open_Song_v1.xml' 
elif [ "$NAME" = "sfb15" ]; then
    URL='http://www.folkbibeln.it/arkiv/SFB_2015_Open_Song_v2.xml' 
elif [ "$NAME" = "index" ]; then
    pandoc --css pandoc.css -t html -s --metadata pagetitle=sfb readme.md > index.html
    exit 0
else
	echo "usage: $0 [sfb98|sfb15|index]"
	exit 1
fi

curl "$URL" | ./conv.py > "data/$NAME.tsv"