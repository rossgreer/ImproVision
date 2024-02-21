# Function for how each instrument moves for each measure (half/whole step, up/down)

import pretty_midi


def analyze_midi_movements(midi_file_name):
    """
    Analyzes the movements of instruments in a MIDI file.
    
    Parameters:
    midi_file_name (str): The path to the MIDI file to be analyzed.
    """

    midi_data = pretty_midi.PrettyMIDI(midi_file_name)

    # Use this part below to display measures
    # Currently assumes file is in 4/4 at 120 bpm
    bpm = 120  
    time_signature = 4  
    seconds_per_beat = 60 / bpm
    seconds_per_measure = seconds_per_beat * time_signature

    # Iterate through each instrument in the MIDI file
    for instrument in midi_data.instruments:
        # Skip drums because MIDI treats those differently
        if not instrument.is_drum:
            previous_pitch = None
            # Iterate through the notes played by the instrument
            for note in sorted(instrument.notes, key=lambda x: x.start):
                # Convert start time to measure number
                measure_number = note.start / seconds_per_measure + 1  # Adding 1 to start measure count at 1
                if previous_pitch is not None:
                    # Determine the movement
                    pitch_difference = note.pitch - previous_pitch
                    if pitch_difference == 0:
                        movement = "stays the same"
                    elif pitch_difference == 1:
                        movement = "moves up a half step"
                    elif pitch_difference == 2:
                        movement = "moves up a whole step"
                    elif pitch_difference == -1:
                        movement = "moves down a half step"
                    elif pitch_difference == -2:
                        movement = "moves down a whole step"
                    else:
                        movement = "moves irregularly"
                    # Output the instrument name, note pitch, measure number, and movement
                    print(f"{instrument.name} (Program {instrument.program}), Note pitch: {note.pitch}, Measure: {int(measure_number)}: {movement}")
                previous_pitch = note.pitch


# Example
midi_file_name = 'next_right_thing_2.mid'
analyze_midi_movements(midi_file_name)