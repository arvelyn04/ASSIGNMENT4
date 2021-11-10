def read_3integers():

    fruit_1 = int(input("PRICE OF THE APPLE: "))
    yourOrder = int(input("HOW MANY APPLES DO YOU WANT TO BUY: "))
    yourMoney = int(input("YOUR MONEY HERE: "))
    return fruit_1, yourOrder, yourMoney

def average3(a1, a2, a3):
    return a3-(a1*a2)

val1,val2,val3 = read_3integers()

print(f"YOU CAN BUY {val1} APPLES AND YOUR CHANGE IS {average3(val1, val2, val3): .4f}. ")