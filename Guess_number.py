#working with the random module
import random

#lets make a random number
print(random.randrange(11))#this will start from 0 automatocally up to 11(11 is exclusive)
print(random.randrange(-2, 13))#start at -2 and stop at 13(13 is not inclusive), generate a random number in between

#now lets use randint this will include the  upper bound
print(random.randint(1,8)) # 8 is inclusive now
