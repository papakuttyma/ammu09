year = int(input("Enter Year: "))
if year % 4 == 0 & year % 100 != 0:
    print(year, "yes")
elif year % 100 == 0:
    print(year, "no")
elif year % 400 ==0:
    print(year, "yes")
else:
    print(year, "no")
