# 파이썬 기초 12: 내장 모듈 사용 (math, random, datetime)
import math
import random
from datetime import date, timedelta

print(math.sqrt(16), math.pi, math.ceil(2.1), math.floor(2.9))

random.seed(42)
print(random.randint(1, 10), random.choice(["a", "b", "c"]))
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(len(nums), sorted(nums))

d = date(2026, 11, 20)
print(d, d.weekday(), d + timedelta(days=10))
print((date(2026, 12, 25) - d).days, "일 남음")
