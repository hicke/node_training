import random
import redis

# TODO: Check if exists in Redis, otherwise skip





r = redis.StrictRedis(host='localhost', port='32769', db=9)

answer = []

for throw in range(100):
    dice_throw = random.randint(1,6)
    answer.append(dice_throw)
    #print(answer.count(dice_throw))
    # print('Throw number ' + str(throw) + ': ' + str(answer))

counter = [[x,answer.count(x)] for x in set(answer)]

#print(counter)

for lst in counter:
    r.incrby(lst[0], lst[1])
    # r.set(lst[0], lst[1])
    name = "Henric"
    password = 'ic7wmr'
    # r.hmset(name, {'password':password, 'first_name':'John', 'last_name':'Doe', 'email_id':'john@gmail.com', 'phone_no':'1234567890'})

print('Values entered in redis cache.')
    #print('Number of', lst[0], '->', lst[1])
