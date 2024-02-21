# Manual display of what instrument moves how
# See analyze_midi_mvt_func.py for an automated version that can take any MIDI file as input

# Gr_1 = top line of score
# Gr_2 = second line
# Gr_3 = third line
# Gr_4 = bottom line

# measure 1 is given by human administrator

# for each new measure: 
#   wait until "desire to change" is detected from any musician/group -- details TBD
#   perform individual cue, Gr_1 through Gr_4 in order
#   then global cue

# measure 2
# up_half(Gr_1)
# down_whole(Gr_3)

# measure 3
# up_whole(Gr_1)
# up_whole(Gr_2)
# down_half(Gr_4)

# measure 4
# down_whole(Gr_2)

# measure 5
# up_whole(Gr_1)
# down_whole(Gr_3)
# up_half(Gr_4)

# measure 6
# down_half(Gr_3)

# measure 7
# up_half(Gr_3)

# measure 8
# up_whole(Gr_1)
# up_whole(Gr_2)
# up_whole(Gr_3)
# up_whole(Gr_4)

# measure 9
# up_whole(Gr_2)
# down_whole(Gr_4)

# measure 10
# down_whole(Gr_1)
# up_half(Gr_2)
# up_whole(Gr_3)

# measure 11
# down_half(Gr_2)

# measure 12
# up_half(Gr_2)
# down_whole(Gr_3)

# measure 13
# up_whole(Gr_1)
# up_whole(Gr_2)
# up_whole(Gr_4)

# measure 14
# down_whole(Gr_4)

# measure 15
# up_half(Gr_1)
# up_whole(Gr_2)
# down_whole(Gr_3)

# measure 16
# down_whole(Gr_2)
# down_half(Gr_3)