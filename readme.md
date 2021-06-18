# sfb

Lookup the word of God from an API
This api defaults to `sfb98`, can be changed with the parameter `?sfb15`.

### Examples

```
> GET /1 Mos 1:1
< HTTP/1.1 200 OK
<
I begynnelsen skapade Gud himmel och jord.
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
./util.sh sfb98
./srv.py PORT
```