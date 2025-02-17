def create_board():
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

def take_shot(board):
    while True:
        try:
            row = int(input("Enter row to shoot (0-9): "))
            col = int(input("Enter column to shoot (0-9): "))
            
            if 0 <= row < 10 and 0 <= col < 10:
                if board[row][col] == "B":
                    print("🎯 Hit!")
                    board[row][col] = "X"
                elif board[row][col] == "~":
                    print("💦Miss!")
                    board[row][col] = "O"
                else:
                    print("You've already shot there!. Try again")
                    continue
                return
            else:
                print("Out of bounds! Try again.")

        except ValueError:
            print("Invalid input. Enter numbers between 0 and 9.")

def all_ships_destroyed(board):
    return all(cell != "B" for row in board for cell in row)

def battleship_game():
    print("Welcome to Battleship!")

    # Create boards for Player 1 and Player 2
    board1 = create_board()
    board2 = create_board()

    # Player 1 places ships
    print("\nPlayer 1, place your ships:")
    for ship, size in ships.items():
        place_ship(board1, ship, size)

    # Player 2 places ships
    print("\nPlayer 2, place your ships:")
    for ship, size in ships.items():
        place_ship(board2, ship, size)

    # Start the game loop
    current_player = 1
    player_board = board2  # Player 1 shoots at Player 2's board
    opponent_board = board1

    while True:
        print(f"\nPlayer {current_player}'s turn!")
        print_board(player_board, hide_ships=True)

        take_shot(player_board)

        if all_ships_destroyed(player_board):
            print(f"🎉 Player {current_player} wins! All ships destroyed!")
            break

        # Switch turns
        current_player = 2 if current_player == 1 else 1
        player_board, opponent_board = opponent_board, player_board

battleship_game()
