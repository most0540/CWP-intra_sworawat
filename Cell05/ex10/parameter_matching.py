import sys
if len(sys.argv) == 2:
    target_word = sys.argv[1]
    user = input("What was the parameter? ")
    if user == target_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")