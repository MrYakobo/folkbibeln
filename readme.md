# folkbibeln

An api to access the word of god. Utilizes bontibon's excellent script [kjv](https://github.com/bontibon/kjv). Scrapes xml files from folkbibeln.it and turns it into tsv, the format used by kjv. Web server written in Go.

Requests are done like in ordinary kjv, except the books are from SFB instead. An additional HTTP parameter `?annotations` can be added to get kjvs default output, otherwise it is cleaned up a bit, which is to skip the header and verse numbers, making it more of a lookup-api than a reader.
