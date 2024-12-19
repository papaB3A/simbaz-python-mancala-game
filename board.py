from variables import ar_ray

def print_board(**kwargs):
    # this loop prevents unwanted spaces from being added to the board after a player's move
    for i in range(len(ar_ray)):
            # the current ar_ray element should initially be interpretted as an integer
            ar_ray[i]= int(ar_ray[i])
            if int(ar_ray[i]) < 10:
                # the printed expression needs an extra space so it can take up two digits in my board
                ar_ray[i]= " "+ str(ar_ray[i])
            else:
                ar_ray[i]= str(ar_ray[i])
        
    board = (
        "\n+------+------+-<<<<<-Player 2------+------+------+------+\n"
        "|      |L     |K     |J     |I     |H     |G     |      |\n"
        f"|      |  {ar_ray[12]}  |  {ar_ray[11]}  |  {ar_ray[10]}  |  {ar_ray[9]}  |  {ar_ray[8]}  |  {ar_ray[7]}  |      |\n"
        "|      |      |      |      |      |      |      |      |\n"
        f"|  {ar_ray[-1]}  |------+------+------+------+------+------|  {ar_ray[6]}  |\n"
        "|      |A     |B     |C     |D     |E     |F     |      |\n"
        f"|      |  {ar_ray[0]}  |  {ar_ray[1]}  |  {ar_ray[2]}  |  {ar_ray[3]}  |  {ar_ray[4]}  |  {ar_ray[5]}  |      |\n"
        "|      |      |      |      |      |      |      |      |\n"
        "+------+------+------Player 1>>>>>-+------+------+------+\n"
    )

    if kwargs.get("print_board"):
        print(board)
    else:
        return board