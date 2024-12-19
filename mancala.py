# imports
from progress import save_record
from score import print_score
from board import print_board
from variables import option, player_onez_turn, ar_ray

# array of beads in each mancala and pit
ar_ray = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
player_onez_turn = True

# custom switch case structure
def switch_case(case):
    options = {
        "a": case_0,
        "b": case_1,
        "c": case_2,
        "d": case_3,
        "e": case_4,
        "f": case_5,
        "g": case_7,
        "h": case_8,
        "i": case_9,
        "j": case_10,
        "k": case_11,
        "l": case_12,
        "q": end_game
    }
    options.get(case, default)()

def case_0():
    add_beads_to_consecutive_pits(0)

def case_1():
    add_beads_to_consecutive_pits(1)

def case_2():
    add_beads_to_consecutive_pits(2)

def case_3():
    add_beads_to_consecutive_pits(3)

def case_4():
    add_beads_to_consecutive_pits(4)

def case_5():
    add_beads_to_consecutive_pits(5)

def case_7():
    add_beads_to_consecutive_pits(7)

def case_8():
    add_beads_to_consecutive_pits(8)

def case_9():
    add_beads_to_consecutive_pits(9)

def case_10():
    add_beads_to_consecutive_pits(10)

def case_11():
    add_beads_to_consecutive_pits(11)

def case_12():
    add_beads_to_consecutive_pits(12)

def end_game():
    print("Game Over...")
    print_score(print_score=True)
    save_progress = ""
    while save_progress not in ('y', 'n'):
        try:
            save_progress = input("Do you wish to save your progress [Y/n]? ").lower()
            if save_progress not in ('y', 'n'):
                raise ValueError("Oops! Invalid input")
            elif save_progress == "y":
                print("Saving...")
                save_record()
            elif save_progress == "n":
                print("Exiting...")
        except ValueError as e:
            print(f"{e}\n")

def default():
    print("Invalid Input!!\n")

# helper function
def add_beads_to_consecutive_pits(current_index):
    bead_count = int(ar_ray[current_index])
    ar_ray[current_index] = 0 
    for consecutive_index in range(1, (bead_count + 1)):
        target_index = (current_index + consecutive_index) % len(ar_ray)
        ar_ray[target_index] = int(ar_ray[target_index]) + 1

def computer_move():
    for i in range(6):  # Check pits A-F
        if ar_ray[i] > 0:  # If the pit is non-empty
            print(f"Computer chooses pit {chr(i + ord('a'))}...")
            switch_case(chr(i + ord('a')))
            break

# Game setup: Choose mode
game_mode = input("Choose game mode: (1) One Player (2) Two Players: ").strip()
if game_mode not in ['1', '2']:
    raise ValueError("Invalid game mode selected. Please choose '1' or '2'.")

# player's turn switched in each loop 
while option != "q":
    try:
        if player_onez_turn:
            print("\nPlayer One's turn...")
            player = ["A-F", "Player 1"]
        else:
            if game_mode == '1':
                print("\nComputer's turn...")
                computer_move()
                player_onez_turn = not player_onez_turn
                continue  # Skip to the next loop iteration
            else:
                print("\nPlayer Two's turn...")
                player = ["G-L", "Player 2"]

        print_board(print_board=True)

        option = input(f"*{player[1]}, enter move: {player[0]} (or 'q' to QUIT)\n-> ").lower()
        if not option.isalpha():
            raise ValueError("Please enter an alphabetic letter!!")

        # if player_onez_turn & option entered is not in the tuple (a,b,c,d,e,f,q)
        if player_onez_turn and option not in ("a", "b", "c", "d", "e", "f", "q"):
            raise ValueError(f"Please enter a move from {player[0]} (or 'q' to QUIT)")
        elif not player_onez_turn and option not in ("g", "h", "i", "j", "k", "l", "q"):
            raise ValueError(f"Please enter a move from {player[0]} (or 'q' to QUIT)")
        elif player_onez_turn and option in ("a", "b", "c", "d", "e", "f"):
            pit_index = ord(option) - ord('a')
            if int(ar_ray[pit_index]) == 0:
                raise ValueError("You can't pick an empty pit! Please choose a pit with beads.")
            else:
                switch_case(option)
        elif not player_onez_turn and option in ("g", "h", "i", "j", "k", "l"):
            pit_index = ord(option) - ord('g') + 7
            if int(ar_ray[pit_index]) == 0:
                raise ValueError("You can't pick an empty pit! Please choose a pit with beads.")
            else:
                switch_case(option)
        elif option == "q":
            switch_case(option)

        # check if either of the players' pits are all empty...if so print the re-rendered board and end game
        if player_onez_turn and all(int(ar_ray[i]) == 0 for i in range(6)):
            print_board(print_board=True)
            end_game()
            break
        elif not player_onez_turn and all(int(ar_ray[i]) == 0 for i in range(7, 13)):
            print_board(print_board=True)
            end_game()
            break

        # switch player's turn at the end
        player_onez_turn = not player_onez_turn
    except ValueError as e:
        print(f"Error: {e}\n")