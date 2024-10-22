def return_coins(coins,remain):
    coins.sort(reverse=True)
    returned_coins = {}

    idx = 0
    while idx < len(coins) and remain != 0:
        returned = remain // coins[idx]
        remain %= coins[idx]
        if returned > 0:
            returned_coins[coins[idx]] = returned
        idx += 1
    if remain != 0:
        return "Error"
    result = f"Number of coins to take: {sum(returned_coins.values())}\n"
    for k, v in returned_coins.items():
        if v > 0:
           result += f"{v} coin(s) with value {k}\n"
    return result.strip()


coin_list = [int(el) for el in input().split(', ')]
change = int(input())

coins_dict = {}

print(return_coins(coin_list,change))


