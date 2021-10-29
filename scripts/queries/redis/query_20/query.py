import redis

r = redis.Redis()

#keys corresponding to tables
insects = range(6668,6748)

#Query 21
results21 = []
for key in insects:
    elem_decoded = r.hmget(key,'Where/How')[0].decode()
    elem_decoded1 = r.hmget(key,'Weather')[0].decode()
    if (elem_decoded == 'On palm trees') and (elem_decoded1 == 'Any weather') :
        result21 = []
        result21.append(r.hmget(key,'Name')[0].decode())
        result21.append(r.hmget(key,'Sell')[0].decode())
        result21.append(r.hmget(key,'Color_1')[0].decode())
        result21.append(r.hmget(key,'Color_2')[0].decode())
        result21.append(int(r.hmget(key,'Total_Catches_to_Unlock')[0].decode()))
        result21.append(r.hmget(key,'Spawn_Rates')[0].decode())
        results21.append(result21)
print("Query 21 :", sorted(results21,key = lambda x: x[4]))