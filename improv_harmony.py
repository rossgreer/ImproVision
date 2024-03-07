# setup: 4 musicians/groups, in a semi-circle around camera, nobody directly in the middle
# from camera's perspective: violin 1 on far left, violin 2 left, viola right, cello far right
# default camera position: horizontally level, facing middle of semi-circle
# human initializes starting pitch for each instrument (i.e. robot doesn't have to do this, assume this is already done)

# -------------------------------------------------------------------------------------------------------

# (run robot_instructions function from robot_instructions_as_dict.py to find out what instruments should move when)

# for measure, info in instructions_by_measure.items():
#   if ("move-on cue" detected) or (30 seconds passes without "move-on cue"):
#       for instr in info:
#           if info[instr] == "up half":
#               (find and center camera on instr, i.e. eye contact)
#               (wait 1 second)
#               (tilt up 30 degrees)
#               (tilt back down to default state)
#           elif info[instr] == "up whole":
#               (find and center camera on instr, i.e. eye contact)
#               (wait 1 second)
#               (tilt up 60 degrees)
#               (tilt back down to default state)   
#           elif info[instr] == "down half":
#               (find and center camera on instr, i.e. eye contact)
#               (wait 1 second)
#               (tilt down 30 degrees)
#               (tilt back up to default state)   
#           elif info[instr] == "down whole":
#               (find and center camera on instr, i.e. eye contact)
#               (wait 1 second)
#               (tilt down 60 degrees)
#               (tilt back up to default state)
#           else:
#               (skip this instr)
#       (then global cue function)
#   (then move on to next measure)



# GLOBAL CUE FUNCTION - to communicate to musicians that they should switch to new note now

# once all individual cues have taken place:
#   pan around
#   return to default state (facing the middle)
#   then big nod (90 degrees upward, then return to default state) to cue simultaneous changes
#   potentially sync with monitor with "3, 2, 1" countdown

# -------------------------------------------------------------------------------------------------------

# open questions
# - is the dictionary format useful as output of the robot_instructions function? easy to access?
# - what if someone misses or misinterprets a cue (e.g. goes up a whole step instead of half)? would mess up future chords as well
# - how to define the "move-on cue" - what counts as desire to change/boredom/displeasure?
#   - could do a trial run with an explicitly defined move-on cue for the musicians ("raise your eyebrows if you're bored")
#     and then, once we know everything else is working, make the cue more naturalistic
# - try out what tilt angles work best for which cues




# helpful camera links
# https://github.com/PTZOptics/Robotics-Research-Learning-Support-Program 
# https://ptzoptics.imagerelay.com/ml/PTZOptics-Command-List-HTTP-CGI-G3 