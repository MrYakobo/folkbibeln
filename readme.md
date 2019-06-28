# folkbibeln api 2.0

rewritten and better than ever

folkbibeln.it has data for openlp in xml-format, so i leech that

server written in golang

list of features and legal requests:

request whole book:
	GET /1 Mos

request verse:
	GET /Joh 3:16

request verse spans
	GET /Joh 10:1-17

data should be returned in JSON:

	GET /1 Mos
	> { "verses": ["I begynnelsen...", ... ], "footnotes": {"1": ""} }

unless specifically specified to be plain.

	GET /Joh 3:16?plain
	> Ty så älskade Gud världen...

btw the xml files doesn't have footnotes. so only returning plain seems plausible

data can be stored in either a fat json file:

```json
{
"1 Mos": [
	"I begynnelsen"
]
}
```

or a fat plain text tsv file:

```
1 Mos 1:1	I begynnelsen...
1 Mos 1:2	Jorden var öde...
```

that tsv is going to be big, but then one can simply use `grep` as the CGI. almost too good to be true

	GET /Joh 3:16
	grep 'Joh 3:16' fat.tsv | cut -d '\t' -f2
	> Ty så älskade...

that seems the most unixy way.
so how do i convert the xml to tsv? python seems plausible.

could also try to reuse code from https://github.com/bontibon/kjv, as the data format doesn't look that bad. that way, i get more features.

that specification is

	Book Name, Book, Chapter, Verse, String

should be trivial.
