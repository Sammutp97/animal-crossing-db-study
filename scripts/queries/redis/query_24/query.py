import redis

r = redis.Redis()

#keys corresponding to tables
photos = range(8506,11634)

#Query 25
results25 = []
for key in photos:
    elem_decoded = r.hmget(key,'Size')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == '1x1') and (elem_decoded1 != 'High Friendship') :
        result25 = []
        result25.append(r.hmget(key,'Name')[0].decode())
        result25.append(r.hmget(key,'Buy')[0].decode())
        result25.append(r.hmget(key,'Sell')[0].decode())
        result25.append(r.hmget(key,'Catalog')[0].decode())
        result25.append(r.hmget(key,'Color_1')[0].decode())
        result25.append(r.hmget(key,'Color_2')[0].decode())
        result25.append(r.hmget(key,'Body_Title')[0].decode())
        results25.append(result25)
print("Query 25 :", results25)