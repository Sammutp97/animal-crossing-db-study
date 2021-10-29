import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)

#Query 4
result4 = []
max_profit = -1000
max_idx = 0
for key in accessories :
    elem = r.hmget(key,'Buy')
    if elem[0].decode() != '-1':
        sell_price = r.hmget(key,'Sell')
        profit = int(sell_price[0].decode()) - int(elem[0].decode())
        if profit > max_profit :
            max_profit = profit
            max_idx = key
result4.append((r.hmget(max_idx,'Name'))[0].decode())
result4.append((r.hmget(max_idx,'Variation'))[0].decode())
result4.append((r.hmget(key,'Source'))[0].decode())
result4.append(max_profit)
print("Query 4 :", result4)