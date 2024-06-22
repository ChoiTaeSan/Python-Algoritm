def min_coins(coins, amount):
    coins.sort(reverse=True)
    total_coins = 0
    for coin in coins:
        total_coins += amount // coin
        amount %= coin
        if amount == 0:
            break
    return total_coins

coins = [1, 5, 10, 25]
amount = 36
print("Minimum coins needed:", min_coins(coins, amount))
