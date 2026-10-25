

class TelemetryFrame:

    _bytes = []
    _frame_number = 0

    @property
    def frame_number(self):
        return self._frame_number

    @property
    def frame_counter(self):
        return self._bytes[60]

    def __init__(self, frame_number: int, frame_bytes: list):

        self._frame_number = frame_number
        self._bytes = frame_bytes

        ...

    
