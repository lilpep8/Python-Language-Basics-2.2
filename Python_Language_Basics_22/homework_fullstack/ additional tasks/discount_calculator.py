# task11 discount_calculator
import math


cost = int(input("Введите сумму покупки: "))
percent = int(input("Введите процент скидки: "))

money_saved = (cost / 100 * percent)
amount_to_be_paid = (cost - (cost / 100 * percent))

print(f"Вы экономите: {money_saved}")
print(f"Сумма к оплате (округлено): {math.ceil(amount_to_be_paid)}")

