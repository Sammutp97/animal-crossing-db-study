import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

tools = range(13661,13861)

#Query 31

Results31 = []

for key in tools:
    elem_decoded1 = r.hmget(key,'DIY')[0].decode()
    elem_decoded2 = r.hmget(key,'Uses')[0].decode()

    if (elem_decoded1 == 'Yes') and (elem_decoded2 == 'Unlimited'):
        Result31 = []
        Result31.append(r.hmget(key,'Name')[0].decode())
        Result31.append(r.hmget(key,'Variation')[0].decode())
        Result31.append(r.hmget(key,'Buy')[0].decode())
        Result31.append(r.hmget(key,'Sell')[0].decode())
        Result31.append(r.hmget(key,'Color_1')[0].decode())
        Result31.append(r.hmget(key,'Color_2')[0].decode())
        Result31.append(r.hmget(key,'Source')[0].decode())
        Result31.append(r.hmget(key,'Set')[0].decode())
        Result31.append(r.hmget(key,'Size')[0].decode())
        Results31.append(Result31)

#print("Query 31 : ", Results31)

timeit.timeit()