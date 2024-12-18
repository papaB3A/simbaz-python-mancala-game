import datetime
from board import print_board
from score import print_score

def save_record():
    x = datetime.datetime.now()

    # write the current date and time to the scores text file
    # write the last board rendered plus players scores  
    with open('scores.txt', 'a') as file:
        file.write(f"\n{x.strftime('%I')}:{x.strftime('%M')} {x.strftime('%p')}\n")
        file.write(f"{x.strftime('%d')}th {x.strftime('%B')}, {x.strftime('%Y')}\n")
        file.write(print_board())
        file.write(print_score())