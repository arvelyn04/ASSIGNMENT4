def read_2integers():
   
    fruit_1 = int(input("APPLE: "))
    fruit_2 = int(input("ORANGE: "))
    return fruit_1, fruit_2

def totalOf2(f1, f2):
    return (f1+f2)

Price1,Price2 = read_2integers()

print(f"Average is = {totalOf2(Price1, Price2): .4f}")