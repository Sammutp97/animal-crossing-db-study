import redis

r = redis.Redis()

#keys corresponding to tables
fencing = range(2347,2366)

#Query 14
results14 = []
for key in fencing :
    result14 = []
    result14.append(r.hmget(key,'Name')[0].decode())
    result14.append(r.hmget(key,'Sell')[0].decode())
    result14.append(r.hmget(key,'Source_Notes')[0].decode())
    results14.append(result14)
print("Query 14 :", results14)