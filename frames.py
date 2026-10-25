
# First we need to load a file and simply grab the data from it
# Then we need to go through this file line by line and decode each block into a frame
# Finally we will store this in JSON

frame_start_marker = 'Frame'
frames = []

def format_number(number:str) -> int:

    if ',' in number:
        return int(number.replace(',',''))

    return int(number)

def load_file(filename: str) -> list:

    _raw_file_contents = ''

    with open(filename, 'r') as _raw_telemetry_file:
        _raw_file_contents = _raw_telemetry_file.readlines()

    return _raw_file_contents

def parse_file(file_contents: list) -> list:

    _file_frames = []
    _frame_bytes = []
    _frame_byte_index = 0
    _frame_number = 0

    print('Starting processing...')
    
    for _file_line in file_contents:

        if _file_line.strip() != '': # Only if this line is not blank
            # First, break the line into individual words
            _line_contents = str(_file_line.strip()).split()

            # Now we need to find the start of the next frame
            if str(_line_contents[0]) == frame_start_marker:
                # Save the previous frame before starting a new one
                if _frame_bytes:
                    _file_frames.append({_frame_number : _frame_bytes})

                # Reset the counters and indeces
                _frame_number = format_number(_line_contents[1])
                _frame_byte_index = 0
                _frame_bytes = []

                print(f'Processing frame {_frame_number}')

            # TODO: Refactor this to take hex into account and strip the byte index
            # Continue with the current frame
            elif str(_line_contents[0]).isnumeric():
                _row_byte_index = 0

                for _row_byte in str(_file_line).split():
                    _frame_bytes.append({_frame_byte_index : _row_byte})
                    _frame_byte_index += 1    
                    _row_byte_index += 1 # Remember to increment the index

    # Finally add the last frame to the list of frames
    if _frame_bytes:
        _file_frames.append({_frame_number : _frame_bytes})

    return _file_frames

