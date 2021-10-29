import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)
recipes = range(12130,12725)

#Query 5
results5 = []
for key in accessories :
    elem = r.hmget(key,'DIY')
    if elem[0].decode() == 'Yes' :
        elem_name = r.hmget(key,'Name')[0].decode()
        for key2 in recipes :
            elem_name2 = r.hmget(key2,'Name')[0].decode()
            if elem_name == elem_name2 :
                result5 = []
                result5.append(elem_name2)
                result5.append((r.hmget(key2,'#1'))[0].decode())
                result5.append((r.hmget(key2,'Material_1'))[0].decode())
                result5.append((r.hmget(key2,'#2'))[0].decode())
                result5.append((r.hmget(key2,'Material_2'))[0].decode())
                result5.append((r.hmget(key2,'#3'))[0].decode())
                result5.append((r.hmget(key2,'Material_3'))[0].decode())
                result5.append((r.hmget(key2,'#4'))[0].decode())
                result5.append((r.hmget(key2,'Material_4'))[0].decode())
                result5.append((r.hmget(key2,'#5'))[0].decode())
                result5.append((r.hmget(key2,'Material_5'))[0].decode())
                result5.append((r.hmget(key2,'#6'))[0].decode())
                result5.append((r.hmget(key2,'Material_6'))[0].decode())
                results5.append(result5)
print("Query 5 :", results5)