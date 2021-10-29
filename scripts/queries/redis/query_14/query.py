import redis

r = redis.Redis()

#keys corresponding to tables
fish = range(2366,2446)

#Query 15
results15 = []
for key in fish:
    elem_decoded = r.hmget(key,'Where/How')[0].decode()
    elem_decoded1 = r.hmget(key,'Lighting_Type')[0].decode()
    if (elem_decoded == 'Sea') and (elem_decoded1 == 'Fluorescent') :
        result15 = []
        result15.append(r.hmget(key,'Name')[0].decode())
        result15.append(r.hmget(key,'Sell')[0].decode())
        result15.append(r.hmget(key,'Color_1')[0].decode())
        result15.append(r.hmget(key,'Color_2')[0].decode())
        result15.append(r.hmget(key,'Shadow')[0].decode())
        result15.append(int(r.hmget(key,'Total_Catches_to_Unlock')[0].decode()))
        result15.append(r.hmget(key,'Spawn_Rates')[0].decode())
        result15.append(r.hmget(key,'Rain/Snow_Catch_Up')[0].decode())
        results15.append(result15)
print("Query 15 :", sorted(results15,key = lambda x: x[5]))