
import helpers

def load_file(filename: str) -> list:

    _raw_file_contents = ''

    with open(filename, 'r') as _raw_telemetry_file:
        _raw_file_contents = _raw_telemetry_file.readlines()

    return _raw_file_contents

def parse_file(file_contents: list, start_marker: str) -> list:

    _file_frames = []
    _frame_bytes = []
    _frame_time = ''
    _frame_byte_index = 0
    _frame_number = 0

    print('Starting processing...')
    
    for _file_line in file_contents:

        if _file_line.strip() != '': # Only if this line is not blank
            # First, break the line into individual words
            _line_contents = str(_file_line.strip()).split()

            # Now we need to find the start of the next frame
            if str(_line_contents[0]) == start_marker:
                # Save the previous frame before starting a new one
                if _frame_bytes:
                    _file_frames.append({
                        'index' : _frame_number,
                        'time_index' : _frame_time,
                        'bytes' : _frame_bytes
                        })

                # Reset the counters and indeces
                _frame_number = helpers.format_number(_line_contents[1])
                _frame_time = helpers.mission_time(_line_contents[5])
                _frame_byte_index = 0
                _frame_bytes = []

                print(f'Processing frame {_frame_number} with time index {_frame_time}')

            # Continue with the current frame
            if len(str(_line_contents[0])) == 2:
                _row_byte_index = 0

                for _row_byte in str(_file_line).split(): 
                    _frame_bytes.append(int(_row_byte, 16).to_bytes(1, 'little'))
                    _frame_byte_index += 1    
                    _row_byte_index += 1 # Remember to increment the index

    return _file_frames

