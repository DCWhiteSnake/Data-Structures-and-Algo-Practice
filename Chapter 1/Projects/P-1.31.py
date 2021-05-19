denominations = {1000:0, 500:0, 200:0, 100:0, 50:0,
                 5:0}

denominationsArray = [1000,500, 200, 100, 50, 5]

charged = int(input("Enter the charged amount: "))
given = int(input("Enter the amount given by the customer: "))
change = given - charged

for x in denominationsArray:
    if change >= x:
        denominations[x] = change // x
        change = change - x * denominations[x]
        
for x in denominations:
    print(x, denominations[x])

