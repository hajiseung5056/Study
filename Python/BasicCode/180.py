low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []

for i in range(len(low_prices)):
    변동폭 = high_prices[i]-low_prices[i]
    volatility.append(변동폭)

print(volatility)