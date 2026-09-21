import sys
args = sys.argv[1:]
if len(args) == 0:
    print("none")
else:
    for param in args:
        if not param.endswith("ism"):
            print(param + "ism")