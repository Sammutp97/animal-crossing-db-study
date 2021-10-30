#SELECT name, personality, hobby, birthday, catchphrase, favorite_song, style_1, style_2, color_1, color_2, wallpaper, furniture_list 
# FROM villagers 
# WHERE species='Bird' AND gender='Male' AND flooring='tatami';

import timeit

import redis

r = redis.Redis()

#Keys corresponding to tables

villagers = range(15049,15440)

#Query 34

Results34 = []

for key in villagers:
    elem_decoded1 = r.hmget(key,'Species')[0].decode()
    elem_decoded2 = r.hmget(key,'Gender')[0].decode()
    elem_decoded3 = r.hmget(key,'Flooring')[0].decode()

    if (elem_decoded1 == 'Bird') and (elem_decoded2 == 'Male') and (elem_decoded3 == 'tatami'): 
        Result34 = []
        Result34.append(r.hmget(key,'Name')[0].decode())
        Result34.append(r.hmget(key,'Personality')[0].decode())
        Result34.append(r.hmget(key,'Hobby')[0].decode())
        Result34.append(r.hmget(key,'Birthday')[0].decode())
        Result34.append(r.hmget(key,'Catchphrase')[0].decode())
        Result34.append(r.hmget(key,'Favorite_Song')[0].decode())
        Result34.append(r.hmget(key,'Style_1')[0].decode())
        Result34.append(r.hmget(key,'Style_2')[0].decode())
        Result34.append(r.hmget(key,'Color_1')[0].decode())
        Result34.append(r.hmget(key,'Color_2')[0].decode())
        Result34.append(r.hmget(key,'Wallpaper')[0].decode())
        Result34.append(r.hmget(key,'Furniture_List')[0].decode())
        Results34.append(Result34)

#print('Query 34 : ', Results34)

timeit.timeit()
