#SELECT name, variation, sell, seasonal_availability, villager_equippable, color_1, color_2, label_themes
#  FROM tops 
# WHERE diy=false AND source='Recycle bin';

import redis
import timeit 

r = redis.Redis()

#Keys corresponding to tables

tops = range(13861,14982)

#Query 32

Results32 = []

for key in tops:
    elem_decoded1 = r.hmget(key,'DIY')[0].decode()
    elem_decoded2 = r.hmget(key,'Source')[0].decode()

    if (elem_decoded1 == 'No') and (elem_decoded2 == 'Recycle bin'): 
        Result32 = []
        Result32.append(r.hmget(key,'Name')[0].decode())
        Result32.append(r.hmget(key,'Variation')[0].decode())
        Result32.append(r.hmget(key,'Sell')[0].decode())
        Result32.append(r.hmget(key,'Seasonal_Availability')[0].decode())
        Result32.append(r.hmget(key,'Villager_Equippable')[0].decode())
        Result32.append(r.hmget(key,'Color_1')[0].decode())
        Result32.append(r.hmget(key,'Color_2')[0].decode())
        Result32.append(r.hmget(key,'Label_Themes')[0].decode())
        Results32.append(Result32)
    
#print("Query 32 : ", Results32)

timeit.timeit()

