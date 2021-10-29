import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)

#Query 3
list_profit = []
for key in accessories :
    elem = r.hmget(key,'Buy')
    if elem[0].decode() != '-1':
        sell_price = r.hmget(key,'Sell')
        list_profit.append(int(sell_price[0].decode()) - int(elem[0].decode()))
results3 = sum(list_profit)/len(list_profit)
print("Query 3 :", results3)