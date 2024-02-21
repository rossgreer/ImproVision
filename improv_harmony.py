# setup: 4 musicians/groups, in a semi-circle around camera, nobody directly in the middle
# from camera's perspective: violin 1 on far left, violin 2 left, viola right, cello far right
# default camera position: horizontally level, facing middle of semi-circle
# human initializes starting pitch for each instrument (i.e. robot doesn't have to do this, assume this is already done)

# -------------------------------------------------------------------------------------------------------

# run robot_instructions function from robot_instructions_as_dict.py to find out what instruments should move when

# for each measure:
#   when "move-on cue" is detected or if 30 seconds passes without a cue being detected:
#       individual cue functions
#       then global cue function
#   then move on to next measure


# INDIVIDUAL CUE FUNCTIONS

# for each individual musician that does not have "stay" as instruction:
#   center camera on musician ("eye contact")
#   wait 1 second
#   perform desired cue (see helper functions below)
#   then pan to next instrument that has something other than "stay"
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



# GLOBAL CUE FUNCTION - to communicate to musicians that they should switch to new note now

# once all individual cues have taken place:
#   pan around
#   return to default state (facing the middle)
#   then big nod (90 degrees upward, then return to default state) to cue simultaneous changes
#   potentially sync with monitor with "3, 2, 1" countdown

# -------------------------------------------------------------------------------------------------------

# open questions
# - what if someone misses or misinterprets a cue (e.g. goes up a whole step instead of half)? would mess up future chords as well
# - how to define the "move-on cue"
# - try out what tilt angles work best for which cues