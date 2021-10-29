import redis

r = redis.Redis()

#keys corresponding to tables
accessories = range(0,222)
bags = range(376,472)
bottoms = range(472,1198)
dress_up = range(1434,2347)
fencing = range(2347,2366)
floors = range(2446,2622)
headwear = range(2695,3393)
housewares = range(3393,6668)
miscellaneous = range(6748,8055)
other = range(8153,8506)
photos = range(8506,11634)
recipes = range(12130,12725)
rugs = range(12725,12857)
shoes = range(12857,13311)
socks = range(13311,13661)
tools = range(13661,13861)
tops = range(13861,14982)
umbrellas = range(14982,15049)
wall_mounted = range(15440,15898)
wallpaper = range(15898,16145)

#Query 9 careful this one is much longer than the others
results9 = []
search = [accessories, bags, bottoms, dress_up, fencing, floors, headwear, housewares, miscellaneous, other, photos, rugs, shoes, socks, tools, tops, umbrellas, wall_mounted, wallpaper]
for group in search :
    results_group9 = []
    #print(group)
    for key in group :
        #print(key)
        elem = r.hmget(key,'DIY')
        if elem[0].decode() == 'Yes' :
            elem_name = r.hmget(key,'Name')[0].decode()
            for key2 in recipes :
                elem_name2 = r.hmget(key2,'Name')[0].decode()
                if elem_name == elem_name2 :
                    result9 = []
                    result9.append(elem_name2)
                    result9.append((r.hmget(key2,'#1'))[0].decode())
                    result9.append((r.hmget(key2,'Material_1'))[0].decode())
                    result9.append((r.hmget(key2,'#2'))[0].decode())
                    result9.append((r.hmget(key2,'Material_2'))[0].decode())
                    result9.append((r.hmget(key2,'#3'))[0].decode())
                    result9.append((r.hmget(key2,'Material_3'))[0].decode())
                    result9.append((r.hmget(key2,'#4'))[0].decode())
                    result9.append((r.hmget(key2,'Material_4'))[0].decode())
                    result9.append((r.hmget(key2,'#5'))[0].decode())
                    result9.append((r.hmget(key2,'Material_5'))[0].decode())
                    result9.append((r.hmget(key2,'#6'))[0].decode())
                    result9.append((r.hmget(key2,'Material_6'))[0].decode())
                    results_group9.append(result9)
    results9.append(results_group9)
#print("Query 9 :", results9) too long to be printed
print("Query 9 : done")
