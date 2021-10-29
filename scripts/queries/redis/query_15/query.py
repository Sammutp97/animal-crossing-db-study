import redis

r = redis.Redis()

#keys corresponding to tables
floors = range(2446,2622)

#Query 16
results16 = []
for key in floors:
    elem_decoded = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded1 = r.hmget(key,'HHA_Concept_2')[0].decode()
    if (elem_decoded == 'expensive') and (elem_decoded1 == 'facility') :
        result16 = []
        result16.append(r.hmget(key,'Name')[0].decode())
        result16.append(r.hmget(key,'Buy')[0].decode())
        result16.append(r.hmget(key,'Sell')[0].decode())
        result16.append(r.hmget(key,'Catalog')[0].decode())
        result16.append(r.hmget(key,'VFX')[0].decode())
        result16.append(r.hmget(key,'Color_1')[0].decode())
        result16.append(r.hmget(key,'Color_2')[0].decode())
        result16.append(r.hmget(key,'Tag')[0].decode())
        result16.append(r.hmget(key,'Source')[0].decode())
        results16.append(result16)
print("Query 16 :", results16)