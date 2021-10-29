import redis

r = redis.Redis()

#keys corresponding to tables
miscellaneous = range(6748,8055)

#Query 22
results22 = []
for key in miscellaneous:
    result22 = []
    result22.append(r.hmget(key,'Name')[0].decode())
    result22.append(r.hmget(key,'Buy')[0].decode())
    result22.append(r.hmget(key,'Sell')[0].decode())
    result22.append(r.hmget(key,'Catalog')[0].decode())
    result22.append(r.hmget(key,'Color_1')[0].decode())
    result22.append(r.hmget(key,'Color_2')[0].decode())
    result22.append(r.hmget(key,'Source')[0].decode())
    result22.append(r.hmget(key,'Outdoor')[0].decode())
    result22.append(r.hmget(key,'HHA_Concept_1')[0].decode())
    result22.append(r.hmget(key,'HHA_Concept_2')[0].decode())
    result22.append(r.hmget(key,'Speaker_Type')[0].decode())
    result22.append(r.hmget(key,'Lighting_Type')[0].decode())
    result22.append(r.hmget(key,'Tag')[0].decode())
    results22.append(result22)
print("Query 22 :", results22)