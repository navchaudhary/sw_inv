Tested with:
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32

server.py:
	binds to a port 7070 on localhost
	modify port in case it is occupied

client.py:
	conncects to server on same port as scpecified in server


Assumption:
Assumed that unique Stream ID needs to be explicitly printed in the output to differentiate two orders
with same Header from two different streams.

Additionally printed some metadata as each order is processed.