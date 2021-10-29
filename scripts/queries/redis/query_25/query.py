import redis

r = redis.Redis()

#keys corresponding to tables
posters = range(11634,12086)

#Query 26
results26 = []
for key in posters:
    elem_decoded = r.hmget(key,'Size')[0].decode()
    elem_decoded1 = r.hmget(key,'Color_1')[0].decode()
    elem_decoded2 = r.hmget(key,'Color_2')[0].decode()
    if (elem_decoded == '1x1') and (elem_decoded1 == 'Blue') and (elem_decoded2 == 'Gray'):
        result26 = []
        result26.append(r.hmget(key,'Name')[0].decode())
        result26.append(r.hmget(key,'Buy')[0].decode())
        result26.append(r.hmget(key,'Sell')[0].decode())
        result26.append(r.hmget(key,'Catalog')[0].decode())
        result26.append(r.hmget(key,'Source')[0].decode())
        result26.append(r.hmget(key,'Source_Notes')[0].decode())
        results26.append(result26)
print("Query 26 :", results26)