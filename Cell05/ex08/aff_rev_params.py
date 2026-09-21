import sys
if len(sys.argv) <3:
    print("none")
else:
    args = sys.argv[1:]
    for param in reversed(args):
        print(param)