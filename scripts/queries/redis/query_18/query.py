import redis

r = redis.Redis()

#keys corresponding to tables
housewares = range(3393,6668)

#Query 19
results19 = []
for key in housewares:
    elem_decoded = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded1 = r.hmget(key,'Tag')[0].decode()
    if (elem_decoded == 'expensive') and (elem_decoded1 == 'Toy'):
        result19 = []
        result19.append(r.hmget(key,'Name')[0].decode())
        result19.append(r.hmget(key,'Buy')[0].decode())
        result19.append(r.hmget(key,'Sell')[0].decode())
        result19.append(r.hmget(key,'Catalog')[0].decode())
        result19.append(r.hmget(key,'Color_1')[0].decode())
        result19.append(r.hmget(key,'Color_2')[0].decode())
        result19.append(r.hmget(key,'Source')[0].decode())
        result19.append(r.hmget(key,'Outdoor')[0].decode())
        results19.append(result19)
print("Query 19 :", results19)