#SELECT name, buy, sell, color_1, color_2 
# FROM umbrellas 
# WHERE diy=false AND source='Bug-Off' AND size_of='1x1';

import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

umbrellas = range(14982,15049)

#Query 33

Results33 = []

for key in umbrellas:
    elem_decoded1 = r.hmget(key,'DIY')[0].decode()
    elem_decoded2 = r.hmget(key,'Source')[0].decode()
    elem_decoded3 = r.hmget(key,'Size')[0].decode()

    if (elem_decoded1 == 'No') and (elem_decoded2 == 'Recycle bin') and (elem_decoded3 == '1x1'): 
        Result33 = []
        Result33.append(r.hmget(key,'Name')[0].decode())
        Result33.append(r.hmget(key,'Buy')[0].decode())
        Result33.append(r.hmget(key,'Color_1')[0].decode())
        Result33.append(r.hmget(key,'Color_2')[0].decode())
        Results33.append(Result33)
    
#print("Query 33 : ", Results33)

timeit.timeit()
