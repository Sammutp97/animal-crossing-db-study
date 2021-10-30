#SELECT name, buy, sell, catalog, pattern, diy, source, source_notes, outdoor 
# FROM wall_mounted 
# WHERE size_of='1x1' AND color_1='Beige' AND color_2='Yellow';

import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

wall_mounted = range(15440,15898)

#Query 37

Results37 = []

for key in wall_mounted:
    elem_decoded1 = r.hmget(key,'Size')[0].decode()
    elem_decoded2 = r.hmget(key,'Color_1')[0].decode()
    elem_decoded3 = r.hmget(key,'Color_2')[0].decode()

    if (elem_decoded1 == '1x1') and (elem_decoded2 == 'Beige') and (elem_decoded3 == 'Yellow'): 
        Result37 = []
        Result37.append(r.hmget(key,'Name')[0].decode())
        Result37.append(r.hmget(key,'Buy')[0].decode())
        Result37.append(r.hmget(key,'Sell')[0].decode())
        Result37.append(r.hmget(key,'Pattern')[0].decode())
        Result37.append(r.hmget(key,'DIY')[0].decode())
        Result37.append(r.hmget(key,'Source')[0].decode())
        Result37.append(r.hmget(key,'Source_Notes')[0].decode())
        Result37.append(r.hmget(key,'Outdoor')[0].decode())
        Results37.append(Result37)

#print("Query 37 : ", Results37)

timeit.timeit()
