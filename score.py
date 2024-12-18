from variables import ar_ray

def print_score(**kwargs):
    player_1_score= 0
    for index in range(7):
        player_1_score+= int(ar_ray[index])
    # scoreboard
    scoreboard= f"\n\t--------------------------------\n\t           SCOREBOARD        \n\t--------------------------------\n\t         Player 1   {player_1_score}\n\t         Player 2   {48 - player_1_score}\n\t--------------------------------\n"

    if kwargs.get("print_score"):
        print(scoreboard)
    else:
        return scoreboard

    # class player:
    #  def_init_(self name)    