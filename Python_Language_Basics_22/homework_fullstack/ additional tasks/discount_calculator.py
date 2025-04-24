# task11 discount_calculator
import math
cost = int(input())
precent = int(input())

bagrain = (cost - (cost / 100 * precent))
print((cost / 100 * precent))
print(math.ceil(bagrain))

