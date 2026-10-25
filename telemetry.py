
from operator import itemgetter

def _split_frame(frame_data: list) -> dict:



    return {}

def frame_counter(frame_data: list) -> int:

    _split_bytes = {}
    _byte_index = 0

    for frame in frame_data:

        for key, value in frame.items():
            if key == 60:
                return value

    return 0

def parse_frame(frame_data: list) -> dict:

    _split_bytes = {}
    _byte_index = 0

    for frame in frame_data:

        for key, value in frame.items():
            _split_bytes[key] = value
            _byte_index += 1


    return _split_bytes

