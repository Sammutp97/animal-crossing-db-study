import redis

r = redis.Redis()

#keys corresponding to tables
recipes = range(12130,12725)

#Query 28
results28 = []
for key in recipes:
    result28 = []
    result28.append(r.hmget(key,'Name')[0].decode())
    result28.append(r.hmget(key,'Category')[0].decode())
    result28.append(r.hmget(key,'Sell')[0].decode())
    result28.append(r.hmget(key,'Source')[0].decode())
    result28.append(r.hmget(key,'Recipes_to_Unlock')[0].decode())
    results28.append(result28)
print("Query 28 :", results28)
