def creat_Board():
    return [["~"] * 10 for _ in range(10)] 

ships = {
        "Destroyer" : 2,
    "Subamrine" : 3,
    "Battleship" : 4,
    "Carrier" : 5,
}

def place_ship(board,ship_name,size):
    while True:
        try:
            print(f"Placing {ship_name} (size: {size})")
            row = int(input("Enter row (0-9): "))
            col = int(input("Enter column (0-9): "))
            direction = input("Enter direction(H for horizontal, V for vertical)").upper()

            positions = []
            
            for i in range(size):
                if direction == "H":
                    positions.append((row, col + i))
                elif direction == "V":
                    positions.append((row + i, col))

            if all(0 <= r < 10 and 0 <= c < 10 for r, c in positions) and all(board[r][c] == "~" for r, c in positions):
                for r, c in positions:
                    board[r][c] = "B"
                return
            
        except ValueError:
            print("invalid position. Try again")

def print_board(board,hide_ships=False):
    print(" " + " ".join(str(i)for i in range(10)))
    for i, row in enumerate(board):
        if hide_ships:
            print(f"{i} " + " ".join("~" if cell == "B" else cell for cell in row))
        else:
            print(f"{i} " + " ".join(row))