import redis

r = redis.Redis()

#keys corresponding to tables
shoes = range(12857,13311)

#Query 30
results30 = []
for key in shoes:
    elem_decoded = r.hmget(key,'DIY')[0].decode()
    elem_decoded1 = r.hmget(key,'Source')[0].decode()
    if (elem_decoded == 'No') and (elem_decoded1 == 'Kicks'):
        result30 = []
        result30.append(r.hmget(key,'Name')[0].decode())
        result30.append(r.hmget(key,'Variation')[0].decode())
        result30.append(r.hmget(key,'Sell')[0].decode())
        result30.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result30.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result30.append(r.hmget(key,'Color_1')[0].decode())
        result30.append(r.hmget(key,'Color_2')[0].decode())
        result30.append(r.hmget(key,'Label_Themes')[0].decode())
        results30.append(result30)
print("Query 30 :", results30)