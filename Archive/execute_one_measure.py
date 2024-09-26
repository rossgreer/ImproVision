from Archive.robot_instructions import robot_instructions
from Archive.control_camera import post
import time

# Global instrument order from left to right
INSTRUMENT_ORDER = ['Violin I', 'Violin II', 'Viola', 'Violoncello']


def execute_one_measure(midi_file_name, measure_number):
    """
    Executes camera movements based on the instructions extracted from a specific measure in a MIDI file,
    panning from left to right across a semi-circle of instruments.

    Parameters:
    midi_file_name (str): The path to the MIDI file.
    measure_number (int): The specific measure number to extract movement directions from.
    """
    instructions_by_measure = robot_instructions(midi_file_name)

    if measure_number < 1 or measure_number > len(instructions_by_measure):
        print(f"Measure number {measure_number} is out of range for the given MIDI file.")
        return

    measure_instructions = instructions_by_measure[measure_number - 1]

    # Center
    post("home")
    time.sleep(4)

    # Start by panning to the far left
    post("left")  
    time.sleep(1.5)  # Wait a bit
    post("ptzstop")  # Stop the camera movement

    # Iterate over instruments in order
    for instrument in INSTRUMENT_ORDER:
        time.sleep(1)
        movement = measure_instructions.get(instrument)
        if movement:
            print(f"Executing movement for {instrument}: {movement}")
            execute_movement_for_instrument(movement) # See helper function below
        else:
            print(f"{instrument} has no specific movement. 'Looking' at the instrument.")
            time.sleep(1)
        
        time.sleep(1)

        # Pan to the next instrument on the right
        if instrument != INSTRUMENT_ORDER[-1]:
            post("right")
            time.sleep(1)  
            post("ptzstop")
    
    # Final 'slam' cue
    post("home")
    time.sleep(3)
    post('ptzstop')
    time.sleep(1)
    post('up')
    time.sleep(0.7)
    post('down')
    time.sleep(0.7)


def execute_movement_for_instrument(movement):
    """
    Executes the camera movement based on the specified movement instruction.

    Parameters:
    movement (str): The movement instruction (e.g., "up half", "up whole").
    """
    if movement == "up half":
        post("up")
        time.sleep(0.7)
        post("ptzstop")
        # Return to horizontal
        time.sleep(2)
        post("down")
        time.sleep(0.6)
        post("ptzstop")
    elif movement == "up whole":
        post("up")
        time.sleep(0.5)
        post("ptzstop")
        time.sleep(0.5)  # Pause between half steps
        post("up")
        time.sleep(0.5)
        post("ptzstop")
        # Return to horizontal
        time.sleep(2)
        post("down")
        time.sleep(0.6)
        post("ptzstop")
    elif movement == "down half":
        post("down")
        time.sleep(0.7)
        post("ptzstop")
        # Return to horizontal
        time.sleep(2)
        post("up")
        time.sleep(0.7)
        post("ptzstop")
    elif movement == "down whole":
        post("down")
        time.sleep(0.5)
        post("ptzstop")
        time.sleep(0.5)  # Pause between half steps
        post("down")
        time.sleep(0.5)
        post("ptzstop")
        # Return to horizontal
        time.sleep(2)
        post("up")
        time.sleep(0.7)
        post("ptzstop")


# Example usage
midi_file_name = 'next_right_thing_2.mid'
measure_number = 4
execute_one_measure(midi_file_name, measure_number)

# in the future, replace post("left") and post("right") with ways to center on instrument instead
