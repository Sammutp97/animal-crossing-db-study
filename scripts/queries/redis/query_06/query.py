import redis

r = redis.Redis()

#keys corresponding to tables
achievements = range(222,306)

#Query 7
results7 = []
for key in achievements :
    result7 = []
    result7.append((r.hmget(key,'#'))[0].decode())
    result7.append((r.hmget(key,'Name'))[0].decode())
    result7.append((r.hmget(key,'Award_Criteria'))[0].decode())
    elem_decoded = r.hmget(key,'Num_of_Tiers')[0].decode()
    result7.append(elem_decoded)
    if elem_decoded == '1' :
        result7.append(r.hmget(key,'Tier_1')[0].decode())
        result7.append(r.hmget(key,'Reward_Tier_1')[0].decode())
    if elem_decoded == '2' :
        result7.append(r.hmget(key,'Tier_2')[0].decode())
        result7.append(int((r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())))
    if elem_decoded == '3' :
        result7.append(r.hmget(key,'Tier_3')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())))
    if elem_decoded == '4' :
        result7.append(r.hmget(key,'Tier_4')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())) + int((r.hmget(key,'Reward_Tier_4')[0].decode())))
    if elem_decoded == '5' :
        result7.append(r.hmget(key,'Tier_5')[0].decode())
        result7.append((int(r.hmget(key,'Reward_Tier_1')[0].decode())) + int((r.hmget(key,'Reward_Tier_2')[0].decode())) + int((r.hmget(key,'Reward_Tier_3')[0].decode())) + int((r.hmget(key,'Reward_Tier_4')[0].decode())) + int((r.hmget(key,'Reward_Tier_5')[0].decode())))
    results7.append(result7)

print("Query 7 :", results7)