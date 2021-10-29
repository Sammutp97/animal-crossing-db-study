import redis

r = redis.Redis()

#keys corresponding to tables
bags = range(376,472)

#Query 10
results10 = []
for key in bags :
    elem = r.hmget(key,'DIY')
    if elem[0].decode() == 'No' :
        result10 = []
        result10.append(r.hmget(key,'Name')[0].decode())
        result10.append(r.hmget(key,'Variation')[0].decode())
        result10.append(r.hmget(key,'Sell')[0].decode())
        result10.append(r.hmget(key,'Miles_Price')[0].decode())
        result10.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        result10.append(r.hmget(key,'Villager_Equippable')[0].decode())
        result10.append(r.hmget(key,'Color_1')[0].decode())
        result10.append(r.hmget(key,'Color_2')[0].decode())
        results10.append(result10)
print("Query 10 :", results10)