#SELECT name, buy, sell, vfx, color_1, color_2, catalog, source, window_type, window_color, pane_type, curtain_type, curtain_color, ceiling_type 
# FROM wallpaper 
# WHERE hha_concept_1='zen-style' AND tag='Nature Walls' AND diy=false;import redis

import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

wallpaper = range(15898,16145)

#Query 38

Results38 = []

for key in wallpaper:
    elem_decoded1 = r.hmget(key,'HHA_Concept_1')[0].decode()
    elem_decoded2 = r.hmget(key,'Tag')[0].decode()
    elem_decoded3 = r.hmget(key,'DIY')[0].decode()

    if (elem_decoded1 == 'zen-style') and (elem_decoded2 == 'Nature Walls') and (elem_decoded3 == 'No'):
        Result38 = []
        Result38.append(r.hmget(key,'Name')[0].decode())
        Result38.append(r.hmget(key,'Buy')[0].decode())
        Result38.append(r.hmget(key,'Sell')[0].decode())
        Result38.append(r.hmget(key,'VFX')[0].decode())
        Result38.append(r.hmget(key,'Color_1')[0].decode())
        Result38.append(r.hmget(key,'Color_2')[0].decode())
        Result38.append(r.hmget(key,'Source')[0].decode())
        Result38.append(r.hmget(key,'Window_Type')[0].decode())
        Result38.append(r.hmget(key,'Window_Color')[0].decode())
        Result38.append(r.hmget(key,'Pane_Type')[0].decode())
        Result38.append(r.hmget(key,'Curtain_Type')[0].decode())
        Result38.append(r.hmget(key,'Curtain_Color')[0].decode())
        Result38.append(r.hmget(key,'Ceiling_Type')[0].decode())
        Results38.append(Result38)

#print('Query 38 : ', Results38)

timeit.timeit()
