#using Python standard libraries
import random 
import math
from datetime import datetime

print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)

print(math.sqrt(25))
print(random.randbytes(16))

print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10))
print(random.uniform(1,10))

print(random.choice(["apple","banana","cherry"]))
print(random.choices(["apple","banana","cherry"],k=3))
print(random.sample(["apple","banana","cherry"],k=2))
