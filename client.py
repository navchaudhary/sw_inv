from socket import socket, AF_INET, SOCK_STREAM
import json
import random

#make data stream
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7070))

def gen_rand():
    valid_items = "ABCDE"
    item = random.choice(valid_items)
    qty = random.randint(1 , 5)
    return item, qty

# data source to create and send stream data generated randomly
for i in range(1, 100) :
    item2 = ""
    item3 = ""
    item, qty = gen_rand()
    if i%2 == 0:
        req = '{"Header": %s, "Lines": {"%s" : %s} }' % (i, item, qty)        
    elif i%3 == 0:
        item2, qty2 = gen_rand()
        while (item2 == item):
            item2, qty2 = gen_rand()

        req = '{"Header": %s, "Lines": {"%s" : %s, "%s" : %s} }' % (i, item, qty, item2, qty2)
    else:
        item2, qty2 = gen_rand()
        while (item2 == item):
            item2, qty2 = gen_rand()

        item3, qty3 = gen_rand()
        while (item3 == item or item3 == item2):
            item3, qty3 = gen_rand()

        req = '{"Header": %s, "Lines": {"%s" : %s, "%s" : %s, "%s": %s} }' % (i, item, qty, item2, qty2, item3, qty3)

    s.send(req.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))

# force zero inventory condition in case above
# loop didn't make it so
for i in range(100, 140):
    a='{"Header": %s, "Lines": {"A" : 5, "B" : 5, "C" : 5, "D" : 5, "E": 5} }' % i
    s.send(a.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
    
### Sample test data
##a='{"Header":1, "Lines": {"A" : 1, "C" : 1} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))
##a='{"Header":2, "Lines": {"E" : 5} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))
##a='{"Header":3, "Lines": {"D" : 4} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))
##a='{"Header":4, "Lines": {"A" : 1, "C" : 1} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))
##a='{"Header":5, "Lines": {"B" : 3, "D" : 4} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))
##a='{"Header":6, "Lines": {"D" : 4} }'
##s.send(a.encode('utf-8'))
##print(s.recv(1024).decode('utf-8'))

print("DONE...")
