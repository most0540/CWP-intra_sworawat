import sys

if len(sys.argv) == 2:
    input_string = sys.argv[1]

    z_conunt = input_string.count('z')

    if z_conunt > 0:
        print("z" * z_conunt)
    else:
        print("none")
else:
    print("none")