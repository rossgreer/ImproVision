# setup: 4 musicians/groups, in a semi-circle around camera, nobody directly in the middle

# default camera position: horizontally level, facing middle of semi-circle


# INDIVIDUAL CUE FUNCTIONS

# order of groups: Gr_1, Gr_2, Gr_3, Gr_4
# for each individual musician/group you want to change:
#   make 'eye contact' (i.e., center on musician/group)
#   wait 1 second
#   perform desired cue (see below)
#   if you want more than 1 whole step (unnecessary for now):
#       pause 0.5 seconds while continuing to look at musician
#       then nod again
#   then turn to the next musician you want to change (i.e., pan past musicians you don't want to change)
# return to default state facing middle

# def up_half(player):
#   tilt up 30 degrees
#   return to default state

# def up_whole(player):
#   tilt up 60 degrees
#   return to default state

# def down_half(player):
#   tilt down 30 degrees
#   return to default state

# def up_whole(player):
#   tilt down 60 degrees
#   return to default state



# GLOBAL CUE FUNCTION

# once all individual cues have taken place:
#   pan around
#   return to default state (facing the middle)
#   then big nod (90 degrees upward, then return to default state) to cue simultaneous changes
