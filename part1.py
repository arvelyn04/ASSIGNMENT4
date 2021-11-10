def read_3informations():
    
    Info_1 = input("NAME: ")
    Info_2 = input("AGE: ")
    Info_3 = input("ADDRESS: ")
    return Info_1, Info_2, Info_3

def allInformations3(i1, i2, i3):
    return (i1, i2, i3)

inf1,inf2,inf3 = read_3informations()

print(f"HI! MY NAME IS {inf1}. I AM {inf2} YEARS OLD. I LIVE IN {inf3}. ")