from checkmate import checkmate


def main():

    board = (
        "R....\n"
        ".K...\n"
        ".....\n"
        ".....\n"
        ".Q..."
    )
    print(board)
    checkmate(board)


if __name__ == "__main__":
    main()
