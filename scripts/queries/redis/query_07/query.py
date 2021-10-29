import redis

r = redis.Redis()

#keys corresponding to tables
art = range(306,376)

#Query 8
results8 = []
for key in art :
    elem_decoded = r.hmget(key,'Size')[0].decode()
    elem_decoded2 = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded3 = r.hmget(key,'HHA_Concept_2')[0].decode()
    elem_decoded4 = r.hmget(key,'Tag')[0].decode()
    if (elem_decoded == '1x1') and (elem_decoded2 == 'expensive') and (elem_decoded3 == 'folk art') and (elem_decoded4 == 'Sculpture') :
        result8 = []
        result8.append(r.hmget(key,'Name')[0].decode())
        result8.append(r.hmget(key,'Category')[0].decode())
        result8.append(r.hmget(key,'Buy')[0].decode())
        result8.append(r.hmget(key,'Sell')[0].decode())
        result8.append(r.hmget(key,'Catalog')[0].decode())
        result8.append(r.hmget(key,'Artist')[0].decode())
        result8.append(r.hmget(key,'Museum_Description')[0].decode())
        results8.append(result8)

print("Query 8 :", results8)