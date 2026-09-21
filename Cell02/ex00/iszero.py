try:
    number = int(input())
    if number == 0 :
        print("This number is equal from zero.")
    else:
        print("This number is different from zero.")
except ValueError:
    print("Error enter int Type")