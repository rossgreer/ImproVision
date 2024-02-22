import pretty_midi

def robot_instructions(midi_file_name):
    """
    Analyzes a MIDI file to prepare measure-by-measure signaling instructions for a robot.
    
    Parameters:
    midi_file_name (str): The path to the MIDI file to be analyzed. Currently assumed to be in 4/4 time at 120 bpm.
    Arbitrary number of instruments and measures.
    
    Returns:
    A dictionary where keys are measures and values are new mini sub-dictionaries 
    with instruments and their respective movements.
    """
    midi_data = pretty_midi.PrettyMIDI(midi_file_name)
    instructions_by_measure = {}

    for instrument in midi_data.instruments:
        if not instrument.is_drum: # Skip drums, MIDI treats those weirdly
            previous_pitch = None
            previous_measure = None

            for note in sorted(instrument.notes, key=lambda x: x.start):
                # Assuming 4/4 time signature and 120 bpm
                measure_number = int(note.start / (60 / 120) / 4) + 1 # 60/120/4 because 60secs/120bpm in 4/4 time
                measure_key = f"Measure {measure_number}"

                if measure_key not in instructions_by_measure: # Initialize sub-dictionaries
                    instructions_by_measure[measure_key] = {}

                if previous_pitch is not None and measure_number != previous_measure:
                    pitch_difference = note.pitch - previous_pitch
                    movement = determine_robot_movement(pitch_difference) # See helper function below
                    instrument_name = instrument.name or f"Program {instrument.program}"
                    instructions_by_measure[measure_key][instrument_name] = movement

                previous_pitch = note.pitch
                previous_measure = measure_number
    
    return instructions_by_measure

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
# midi_file_name = 'next_right_thing_2.mid'
# robot_instructions_by_measure = robot_instructions(midi_file_name)
# print(robot_instructions_by_measure)

# Example output:
# {'Measure 1': {}, 'Measure 2': {'Violin I': 'up half', 'Violin II': 'stay', 'Viola': 'down whole', 'Violoncello': 'stay'}, ...
# and so on for all measures}