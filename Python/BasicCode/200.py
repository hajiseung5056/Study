ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
p = 0

for row in ohlc[1:]:
    p += (row[3] - row[0])

print(p)