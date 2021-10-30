#SELECT DISTINCT
# v.name, *
# v.flooring, *
# CASE WHEN f.buy<>-1 THEN f.buy ELSE 0 END AS ||| f_buy |||, *
# f.diy, *
# v.wallpaper, *
# CASE WHEN w.buy<>-1 THEN w.buy ELSE 0 END AS ||| w_buy |||, *
# w.diy, *
# CASE  WHEN f.buy<>-1 AND w.buy<>-1 THEN f.buy+w.buy 
#       WHEN f.buy<>-1 THEN f.buy 
#       WHEN w.buy<>-1 THEN w.buy ELSE 0 END AS ||| total |||

#FROM villagers AS v, floors AS f, wallpaper AS w
#WHERE v.flooring=f.name AND v.wallpaper=w.name
#ORDER BY f.diy, w.diy;

import redis
import timeit

r = redis.Redis()

#Keys corresponding to tables

villagers = range(15049,15440)
floors = range(2446,2622)
wallpaper = range(15898,16145)

#Query 36

Results36 = []

for key_f in floors:
    elem_decoded1b = r.hmget(key_f,'Buy')[0].decode()
    elem_decoded1n = r.hmget(key_f,'Name')[0].decode()
    for key_v in villagers:
        elem_decoded2f = r.hmget(key_v,'Flooring')[0].decode()
        elem_decoded2w = r.hmget(key_v,'Wallpaper')[0].decode()
        for key_w in wallpaper:
            elem_decoded3b = r.hmget(key_w,'Buy')[0].decode()
            elem_decoded3n = r.hmget(key_w,'Name')[0].decode()

            if (elem_decoded2f == elem_decoded1n) & (elem_decoded2w == elem_decoded3n):
                Result36 = []
                Result36.append(r.hmget(key_v,'Name')[0].decode())   #v.name
                Result36.append(r.hmget(key_v,'Flooring')[0].decode())    #v.flooring

                if (elem_decoded1b != -1):   #CASE WHEN f.buy<>-1 THEN f.buy ELSE 0 END AS ||| f_buy |||
                    Result36.append(elem_decoded1b)
                else:
                    Result36.append(0)

                Result36.append(r.hmget(key_f,'DIY')[0].decode())   #f.diy
                Result36.append(r.hmget(key_v,'Wallpaper')[0].decode())   #v.wallpaper
            
                if (elem_decoded3b != -1):   #CASE WHEN w.buy<>-1 THEN w.buy ELSE 0 END AS ||| w_buy |||, *
                    Result36.append(elem_decoded3b)
                else:
                    Result36.append(0)

                Result36.append(r.hmget(key_w,'DIY')[0].decode())    #w.diy

                if ((elem_decoded1b != -1) & (elem_decoded3b != -1)):
                    Result36.append(elem_decoded1b+elem_decoded3b)
                if elem_decoded1b != -1:
                    Result36.append(elem_decoded1b)
                if elem_decoded3b != -1:
                    Result36.append(elem_decoded3b)
                else:
                    Result36.append(0)

                Results36.append(Result36)

L= sorted(Results36, key = lambda x: (x[3], x[6]))
#print('Query 36 : ', L)

timeit.timeit()



        
