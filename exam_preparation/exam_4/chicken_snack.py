from collections import deque

amount_of_money = [int(el) for el in input().split()]
food_prices = deque([int(el) for el in input().split()])
food_eaten = 0

while amount_of_money and food_prices:
    current_amount_of_money = amount_of_money.pop()
    current_food_price = food_prices.popleft()

    if current_amount_of_money == current_food_price:
        food_eaten += 1
        continue

    elif current_amount_of_money > current_food_price:
        change = current_amount_of_money - current_food_price
        food_eaten += 1
        if len(amount_of_money) > 0:
            amount_of_money[-1] += change
        else:
            amount_of_money.append(change)

    else:
        continue

if food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
elif food_eaten > 0:
    print(f"Henry ate: {food_eaten} {'foods' if food_eaten > 1 else 'food'}.")
else:
    print("Henry remained hungry. He will try next weekend again.")

