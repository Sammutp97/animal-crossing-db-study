import redis

r = redis.Redis()

#keys corresponding to tables
fossils = range(2622,2695)

#Query 17
results17 = []
for key in fossils:
    elem_decoded = r.hmget(key,'Museum')[0].decode()
    if (elem_decoded == 'Room 2'):
        result17 = []
        result17.append(r.hmget(key,'Name')[0].decode())
        result17.append(r.hmget(key,'Sell')[0].decode())
        result17.append(r.hmget(key,'Color_1')[0].decode())
        result17.append(r.hmget(key,'Color_2')[0].decode())
        result17.append(r.hmget(key,'Size')[0].decode())
        results17.append(result17)
print("Query 17 :", results17)