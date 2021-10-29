import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)

#Query 6
result6 = set()
for key in accessories :
    elem = r.hmget(key,'Variation')
    result6.add(elem[0].decode())
print("Query 6 :", sorted(result6))