import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)
#Query 1
results1 = []
for key in accessories :
    elem = r.hmget(key,'DIY')
    result1 = []
    if elem[0].decode() == 'Yes' :
        result1.append((r.hmget(key,'Name'))[0].decode())
        result1.append((r.hmget(key,'Variation'))[0].decode())
        result1.append((r.hmget(key,'Sell'))[0].decode())
        result1.append((r.hmget(key,'Miles_Price'))[0].decode())
        result1.append((r.hmget(key,'Seasonal_Availability'))[0].decode())
        result1.append((r.hmget(key,'Villager_Equippable'))[0].decode())
        result1.append((r.hmget(key,'Color_1'))[0].decode())
        result1.append((r.hmget(key,'Color_2'))[0].decode())
        results1.append(result1)
print("Query 1 : ",results1)