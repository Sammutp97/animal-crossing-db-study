import redis

r = redis.Redis()

#keys corresponding to tables
bottoms = range(472,1198)
tops = range(13861,14982)

#Query 20
results20 = []
results_bo = []
for key in bottoms :
    elem_decoded = r.hmget(key,'Color_1')[0].decode()
    elem_decoded1 = r.hmget(key,'Color_2')[0].decode()
    if (elem_decoded == 'Black') or (elem_decoded1 == 'Black'):
        result_bo = []
        result_bo.append(r.hmget(key,'Name')[0].decode())
        result_bo.append(elem_decoded)
        result_bo.append(elem_decoded1)
        results_bo.append(result_bo)
results_to = []
for key in tops :
    elem_decoded = r.hmget(key,'Color_1')[0].decode()
    elem_decoded1 = r.hmget(key,'Color_2')[0].decode()
    if (elem_decoded == 'Black') or (elem_decoded1 == 'Black'):
        result_to = []
        result_to.append(r.hmget(key,'Name')[0].decode())
        result_to.append(elem_decoded)
        result_to.append(elem_decoded1)
        results_to.append(result_to)

for bo in results_bo :
    for to in results_to :
        result20 = []
        result20.append(bo)
        result20.append(to)
        results20.append(result20)
print("Query 20 :", results20)