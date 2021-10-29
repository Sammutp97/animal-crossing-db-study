import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)
#Query 2
list_sell = []
for key in accessories :
    elem = r.hmget(key,'Sell')
    list_sell.append(int(elem[0].decode()))
results2 = sum(list_sell)/len(list_sell)
print("Query 2 :", results2)