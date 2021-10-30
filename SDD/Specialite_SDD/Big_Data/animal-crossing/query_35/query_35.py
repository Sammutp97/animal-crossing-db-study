#SELECT v.name, v.favorite_song, m.source, m.buy 
# FROM villagers AS v, music AS m 
# WHERE v.favorite_song=m.name 
# ORDER BY (m.name, v.name);

import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

villagers = range(15049,15440)
music = range(8055,8153)

#Query 35

Results35 = []

for key_v in villagers:
    elem_decoded1 = r.hmget(key_v,'Favorite_Song')[0].decode()
    for key_m in music:
        elem_decoded2 = r.hmget(key_m,'Name')[0].decode()
        if (elem_decoded1 == elem_decoded2):
            Result35 = []
            Result35.append(r.hmget(key_v,'Name')[0].decode())
            Result35.append(r.hmget(key_v,'Favorite_Song')[0].decode())
            Result35.append(r.hmget(key_m,'Source')[0].decode())
            Result35.append(r.hmget(key_m,'Buy')[0].decode())
            Result35.append(r.hmget(key_m,'Name')[0].decode())
            Results35.append(Result35)

L= sorted(Results35, key = lambda x: x[4])

for x in L:
    del x[-1]
    
#print("Query 35 :", L)

timeit.timeit()






    