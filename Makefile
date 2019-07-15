general:
	git clone 'https://github.com/bontibon/kjv'
	curl $(url) | ./conv.py > kjv/kjv.tsv
	cd kjv && make
	mv kjv/kjv $(name)
	rm -rf kjv
	
sfb98:
	make url='http://www.folkbibeln.it/arkiv/SFB_1998_Open_Song_v1.xml' name=sfb98 general
sfb15:
	make url='http://www.folkbibeln.it/arkiv/SFB_2015_Open_Song_v2.xml' name=sfb15 general

index:
	pandoc --css pandoc.css -t html -s --metadata pagetitle=sfb readme.md > index.html