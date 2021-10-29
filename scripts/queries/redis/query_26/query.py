import redis

r = redis.Redis()

#keys corresponding to tables
reactions = range(12086,12130)

#Query 27
results27 = []
for key in reactions:
    elem_decoded = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == 'Big Sister'):
        result27 = []
        result27.append(r.hmget(key,'Name')[0].decode())
        result27.append(r.hmget(key,'Source_Notes')[0].decode())
        results27.append(result27)
print("Query 27 :", results27)