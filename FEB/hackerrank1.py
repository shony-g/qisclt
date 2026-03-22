

year = int(input(" Please enter a year"))

# function=is_leap(year)
flag = False

if 1900 <= year <= 10**5:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                flag==True
            else:
                flag==False
        else:
            flag==True
    else:
        flag==False
print(flag)



