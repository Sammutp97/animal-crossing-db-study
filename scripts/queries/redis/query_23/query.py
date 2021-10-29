import redis

r = redis.Redis()

#keys corresponding to tables
other = range(8153,8506)

#Query 24
results24 = []
for key in other:
    elem_decoded = int(r.hmget(key,'Stack_Size')[0].decode())
    if (elem_decoded < 30) :
        result24 = []
        result24.append(r.hmget(key,'Name')[0].decode())
        result24.append(r.hmget(key,'Sell')[0].decode())
        result24.append(r.hmget(key,'Miles_Price')[0].decode())
        result24.append(r.hmget(key,'Source')[0].decode())
        result24.append(r.hmget(key,'Source_Notes')[0].decode())
        result24.append(r.hmget(key,'Tag')[0].decode())
        result24.append(r.hmget(key,'Color_1')[0].decode())
        result24.append(r.hmget(key,'Color_2')[0].decode())
        results24.append(result24)
print("Query 24 :", results24)