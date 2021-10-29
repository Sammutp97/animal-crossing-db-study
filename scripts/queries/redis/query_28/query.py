import redis

r = redis.Redis()

#keys corresponding to tables
rugs = range(12725,12857)

#Query 29
results29 = []
for key in rugs:
    elem_decoded = r.hmget(key,'Size')[0].decode()
    elem_decoded1 = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded2 = r.hmget(key,'Tag')[0].decode()
    if (elem_decoded == '3x3') and (elem_decoded1 == 'living room') and (elem_decoded2 == 'Pattern Rugs'):
        result29 = []
        result29.append(r.hmget(key,'Name')[0].decode())
        result29.append(r.hmget(key,'DIY')[0].decode())
        result29.append(r.hmget(key,'Buy')[0].decode())
        result29.append(r.hmget(key,'Sell')[0].decode())
        result29.append(r.hmget(key,'Catalog')[0].decode())
        result29.append(r.hmget(key,'Source')[0].decode())
        result29.append(r.hmget(key,'Source_Notes')[0].decode())
        result29.append(r.hmget(key,'Color_1')[0].decode())
        result29.append(r.hmget(key,'Color_2')[0].decode())
        results29.append(result29)
print("Query 29 :", results29)