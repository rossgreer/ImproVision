import pretty_midi

def robot_instructions(midi_file_name):
    """
    Analyzes a MIDI file to prepare measure-by-measure signaling instructions for a robot.
    
    Parameters:
    midi_file_name (str): The path to the MIDI file to be analyzed. Currently assumed to be in 4/4 time at 120 bpm.
    Arbitrary number of instruments and measures.
    
    Returns:
    A list of dictionaries, each representing a measure and containing instruments with their movements. 
    """
    midi_data = pretty_midi.PrettyMIDI(midi_file_name)
    instructions = []

    for instrument in midi_data.instruments:
        if not instrument.is_drum: # Skip drums, MIDI treats those weirdly
            previous_pitch = None
            previous_measure = None

            for note in sorted(instrument.notes, key=lambda x: x.start):
                # Assuming 4/4 time signature and 120 bpm
                measure_number = int(note.start / (60 / 120) / 4) + 1 # 60/120/4 because 60secs/120bpm in 4/4 time

                if previous_pitch is not None and previous_measure is not None and measure_number != previous_measure:
                    pitch_difference = note.pitch - previous_pitch
                    movement = determine_robot_movement(pitch_difference)

                    while len(instructions) < measure_number - 1:
                        instructions.append({}) # Add a new dictionary for each new measure

                    instrument_name = instrument.name or f"Program {instrument.program}"
                    instructions[measure_number - 2][instrument_name] = movement # -2 because we skip the first measure (i.e., moving into measure 1) & list indexing

                previous_pitch = note.pitch
                previous_measure = measure_number
    
    return instructions

def determine_robot_movement(pitch_difference):
    """Determines the movement for the robot based on pitch difference."""
    if pitch_difference == 0:
        return "stay"
    elif pitch_difference == 1:
        return "up half"
    elif pitch_difference == 2:
        return "up whole"
    elif pitch_difference == -1:
        return "down half"
    elif pitch_difference == -2:
        return "down whole"
    else:
        return "irregular"

# Example usage:
midi_file_name = 'next_right_thing_2.mid'
robot_instructions_by_measure = robot_instructions(midi_file_name)
print(robot_instructions_by_measure)

# Example output:
# [{'Violin I': 'up half', 'Violin II': 'stay', 'Viola': 'down whole', 'Violoncello': 'stay'}, .....]
# and so on for all measures