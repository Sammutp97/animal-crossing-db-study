import redis

r = redis.Redis()

#keys corresponding to tables
construction = range(1198,1434)

#Query 12
results12 = []
for key in construction :
    elem_decoded = r.hmget(key,'Category')[0].decode()
    elem_decoded1 = int(r.hmget(key,'Buy')[0].decode())
    if (elem_decoded == 'Bridge') and (elem_decoded1 < 100000) :
        result12 = []
        result12.append(r.hmget(key,'Name')[0].decode())
        result12.append(r.hmget(key,'Source')[0].decode())
        results12.append(result12)
print("Query 12 :", results12)