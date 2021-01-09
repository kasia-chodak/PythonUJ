year = int(input("Wpisz rok:"))

def leap_Year(year) :
    if year % 4 == 0 and year % 400 == 0 :
        return True
    elif year % 4 == 0 and year %100 != 0 :
        return True
    elif year % 4 == 0 and year % 100 == 0 and year %400 != 0 :
        return False
    else :
        return False

if not year < 1900 or year > 100000 :
    print(leap_Year(year))
else :
    print("Rok poza właściwym zakresem.")