import datetime
#array of beads in each mancala and pit
ar_ray= [4,4,4,4,4,4,0,4,4,4,4,4,4,0] 
player_onez_turn= True
def add_beads_to_consecutive_pits(current_index):
    bead_count= int(ar_ray[current_index])
    # re-assign the value of the current ar_ray element
    ar_ray[current_index]= 0 
    for consecutive_index in range(1, (bead_count + 1)):
        #this👇 prevents an IndexError that occurs when consecutive_index is greater than the ar_ray length
        target_index = (current_index + consecutive_index) % len(ar_ray)
        # add 1 to each of the consecutive pits upto the bead_count
        ar_ray[target_index] = int(ar_ray[target_index]) + 1