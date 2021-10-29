import redis

r = redis.Redis()

#keys corresponding to tables
music = range(8055,8153)

#Query 23
results23 = []
for key in music:
    result23 = []
    result23.append(r.hmget(key,'Name')[0].decode())
    result23.append(r.hmget(key,'Buy')[0].decode())
    result23.append(r.hmget(key,'Sell')[0].decode())
    result23.append(r.hmget(key,'Catalog')[0].decode())
    result23.append(r.hmget(key,'Color_1')[0].decode())
    result23.append(r.hmget(key,'Color_2')[0].decode())
    result23.append(r.hmget(key,'Source')[0].decode())
    result23.append(r.hmget(key,'Source_Notes')[0].decode())
    result23.append(r.hmget(key,'Size')[0].decode())
    results23.append(result23)
print("Query 23 :", results23)