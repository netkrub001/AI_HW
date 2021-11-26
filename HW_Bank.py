print("======|Welcome to Bank|=======")
print("     Bank : 100,500,1000      ")
money = int(input("Enter your money : "))
customer = 0
customer = money
while customer < 20000:
    if customer / 1000 != 0:
        num = int(customer / 1000)
        print(f"1000 : {num}")
        customer %= 1000

    if customer / 500 != 0:
        num = int(customer / 500)
        print(f"500 : {num}")
        customer %= 500

    if customer / 100 != 0:
        num = int(customer / 100)
        print(f"100 : {num}")
        customer %= 100
    break
else:
    print("Error")
print("==============================")
print(f"Withdraws : {money}")
print("==========|Thankyou|==========")