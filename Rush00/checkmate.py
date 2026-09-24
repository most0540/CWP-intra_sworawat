def checkmate(board):
    """ตรวจว่าคิงถูกรุกหรือไม่ แล้วแสดง Success, Fail หรือ Error"""

    if not isinstance(board, str):
        print("Error")
        return

    rows = board.splitlines()
    size = len(rows)

    if size == 0:
        print("Error")
        return

    for row in rows:
        if len(row) != size:
            print("Error")
            return

    king_count = 0
    king_row = -1
    king_col = -1

    for row in range(size):
        for col in range(size):
            if rows[row][col] == "K":
                king_count += 1
                king_row = row
                king_col = col
                if king_count > 1:
                        print("Error")
                        return
    
    if king_count <= 0:
            print("Error")
            return
                



    directions = [
        (0, 1, "RQ"),    
        (0, -1, "RQ"),   
        (1, 0, "RQ"),    
        (-1, 0, "RQ"),   
        (1, 1, "BQ"),    
        (1, -1, "BQ"),   
        (-1, 1, "BQ"),   
        (-1, -1, "BQ"),
    ]

    for row_step, col_step, attackers in directions:

        row = king_row + row_step
        col = king_col + col_step

        while 0 <= row < size and 0 <= col < size:
            piece = rows[row][col]

            if piece in "KPBRQ":
                if piece in attackers:
                    print("Success")
                    return

                break

            row += row_step
            col += col_step

    pawn_row = king_row + 1

    for pawn_col in [king_col - 1, king_col + 1]:
        if 0 <= pawn_row < size and 0 <= pawn_col < size:
            if rows[pawn_row][pawn_col] == "P":
                print("Success")
                return

    print("Fail")
