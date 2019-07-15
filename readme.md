# [sfb](https://github.com/MrYakobo/sfb.git)

This is an api to access the word of god in Swedish. It utilizes bontibon's excellent script [kjv](https://github.com/bontibon/kjv).

This project scrapes xml files from [folkbibeln.it](http://folkbibeln.it) and turns it into tsv, the format used by kjv. A simple web server is written in Go to faciliate requests.

HTTP requests and parameters are passed like in ordinary to kjv, except the books are from SFB. The default output is cleaned up a bit (stripping the header and verse numbers), making it easy for applications to "look up" a bible verse. A HTTP parameter `?annotate` can be supplied to get kjvs default output instead. Defaults to `sfb98`, can be changed with the parameter `?sfb15`.

### Examples

```
> GET /1 Mos 1:1
< HTTP/1.1 200 OK
<
I begynnelsen skapade Gud himmel och jord.
```

```
> GET /Joh 3:16?annotate
< HTTP/1.1 200 OK
<
Johannesevangeliet
3:16	Ty så älskade Gud världen att han utgav sin enfödde Son, för att den som tror på honom inte skall gå förlorad utan ha evigt liv.
```

```
> GET /Matt 17:21
< HTTP/1.1 200 OK
< 
```

```
> GET /1 Mos 3:100
< HTTP/1.1 400 Bad Request
<
Error: The requested passage does not exist
Unknown reference: 1 Mos 3:100
```

```
> GET /foo
< HTTP 1.1/404 Not Found
```

`Matt 17:21` is an omitted verse, hence the server replied with nothing.

### API ref
```
BOOK := (1 Mos|2 Mos|3 Mos|4 Mos|5 Mos|Jos|Dom|Rut|1 Sam|2 Sam|1 Kung|2 Kung|1 Krön|2 Krön|Esr|Neh|Est|Job|Ps|Ords|Pred|Höga v|Jes|Jer|Klag|Hes|Dan|Hos|Joel|Am|Ob|Jon|Mik|Nah|Hab|Sef|Hagg|Sak|Mal|Matt|Mark|Luk|Joh|Apg|Rom|1 Kor|2 Kor|Gal|Ef|Fil|Kol|1 Thess|2 Thess|1 Tim|2 Tim|Tit|Filem|Heb|Jak|1 Pet|2 Pet|1 Joh|2 Joh|3 Joh|Jud|Upp)

FLAGS := (annotate|sfb15)

REQUEST := GET /(BOOK)?[FLAGS]
```

## Install

```
git clone https://github.com/MrYakobo/sfb.git
make sfb98
go run srv.go PORT
```