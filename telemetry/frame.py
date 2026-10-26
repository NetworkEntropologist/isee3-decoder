
import formats

class TelemetryFrame:

    _bytes = []
    _frame_sequence = 0
    _frame_time = ''
    _frame_mode = True # True = Science, False = Engineering

    _frame_bytes_decoded = []
    _frame_science_data = {}
    _frame_engineering_data = {
        'ACC' : 0,
    }

    @property
    def FRAME_SEQUENCE(self):
        return self._frame_sequence

    @property
    def FRAME_COUNTER(self) -> int:
        return int.from_bytes(self._bytes[60],'little')

    @property
    def FRAME_TIME(self):
        return self._frame_time
    
    @property
    def SCIENCE_MODE(self):
        return self._frame_mode

    @property
    def FRAME_BYTES(self):
        return self._bytes
    
    @property
    def FRAME_BYTES_DECODED(self):
        return self._frame_bytes_decoded

    @property
    def FRAME_DATA(self):
        if self._frame_mode:
            return self._frame_science_data
        else:
            return self._frame_engineering_data
    
    def __init__(self, frame:dict):

        self._frame_sequence = frame['index']
        self._frame_time = frame['time_index']
        self._bytes = frame['bytes']

        self._decode_frame()

        ...

    def _decode_frame(self):
        # TODO: Add frame decode logic

        # First determine the frame type
        self._frame_mode = self._frame_type()

        if not self._frame_mode:
            self._decode_eng_frame()
            ...

    def _frame_type(self):
        global _frame_mode

        _accel_bytes = self._bytes[::8]
        _values = [b[0] for b in _accel_bytes]
        _within_range = max(_values) - min(_values) <= 3

        if _within_range:

            return False

        return True

    def _decode_eng_frame(self):

        for _byte_index in range(len(self._bytes)):
            self._frame_bytes_decoded.append((_byte_index, formats.ENGINEER_FRAME_BYTEMAP[_byte_index], self._bytes[_byte_index]))

        self._decode_eng_acc()

    def _decode_eng_acc(self):

        _accel_bytes = self._bytes[::8]
        _values = [b[0] for b in _accel_bytes]
        self._frame_engineering_data['ACC'] = int(sum(_values) / len(_values))

        ...