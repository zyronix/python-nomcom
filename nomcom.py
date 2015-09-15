#!/usr/bin/python
import hashlib
import struct

candidates = ["John",
"Mary",
"Bashful",
"Dopey",
"Sleepy",
"Grouchy",
"Doc",
"Sneazy",
"Handsome",
"Cassandra",
"Pollyanna",
"Pendragon",
"Pandora",
"Faith",
"Hope",
"Charity",
"Lee",
"Longsuffering",
"Chastity",
"Smith",
"Pride",
"Sloth",
"Envy",
"Anger",
"Kascynsky"]
to_select = 10
pool = 25
result = []
for i in range (0, to_select - 1):
    m = hashlib.md5()
    pre = struct.pack('>H', i)
    m.update(pre)
    m.update("9319./2.5.8.10.12./9.18.26.34.41.45./")
    m.update(pre)

    hex = m.hexdigest()
    inter = int("0x"+hex, 0)
    print inter
    selected = inter % (pool - i)
    print selected
    result.append(candidates[selected])    

print result
