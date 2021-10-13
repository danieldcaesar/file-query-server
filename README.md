# file-query-server
local file query server for COMP2602

### Completed by:
Daniel Caesar | Anthony Jr. Cooper
--------------|-------------------
816023385 | 816017231
[@danieldcaesar](https://github.com/danieldcaesar) | [@lain-source](https://github.com/lain-source)


### Contributions:
The SHOW, DELETE, WORDCOUNT & SEARCH were done by Cooper.
The PUT, CREATE, LIST & EXIT commands were done by Caesar. I also did some tidying up to bring everything into uniformity afterward.

You can find the repository [here](https://github.com/danieldcaesar/file-query-server)

-----

# Documentation

All code was writted to be easily understood. Only where code is unclear, comments are present.
That being said, I will clarify the choices made here.


```SEPARATOR```
This global variable is used to combine 2 pieces of data so that it can be sent in one message. Once sent, the data is split on the server side.


```import glob```
The glob package is used only once in the LIST command. However, it was chosen because of its simplicity and ease of use.

