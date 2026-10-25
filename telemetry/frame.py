
ENGINEER_FRAME_BYTEMAP = {
    0 : 'ACC',
    1 : 'I1',
    2 : 'I1',
    3 : 'I1',
    4 : 'I1',
    5 : 'I11',
    6 : 'I1',
    7 : 'I1',
    8 : 'ACC',
    9 : 'I2',
    10 : 'I2',
    11 : 'I2',
    12 : 'I2',
    13 : 'I2',
    14 : 'I2',
    15 : 'I2',
    16 : 'ACC',
    17 : '',
    18 : '',
    19 : '',
    20 : '',
    21 : '',
    22 : '',
    23 : '',
    24 : 'ACC',
    25 : '',
    26 : '',
    27 : '',
    28 : '',
    29 : '',
    30 : '',
    31 : '',
    32 : 'ACC',
    33 : '',
    34 : '',
    35 : '',
    36 : '',
    37 : '',
    38 : '',
    39 : '',
    40 : 'ACC',
    41 : '',
    42 : '',
    43 : '',
    44 : '',
    45 : '',
    46 : '',
    47 : '',
    48 : 'ACC',
    49 : '',
    50 : '',
    51 : '',
    52 : '',
    53 : '',
    54 : '',
    55 : '',
    56 : 'ACC',
    57 : '',
    58 : '',
    59 : '',
    60 : '',
    61 : '',
    62 : '',
    63 : '',
    64 : 'ACC',
    65 : '',
    66 : '',
    67 : '',
    68 : '',
    69 : '',
    70 : '',
    71 : '',
    72 : 'ACC',
    73 : '',
    74 : '',
    75 : '',
    76 : '',
    77 : '',
    78 : '',
    79 : '',
    80 : 'ACC',
    81 : '',
    82 : '',
    83 : '',
    84 : '',
    85 : '',
    86 : '',
    87 : '',
    88 : 'ACC',
    89 : '',
    90 : '',
    91 : '',
    92 : '',
    93 : '',
    94 : '',
    95 : '',
    96 : 'ACC',
    97 : '',
    98 : '',
    99 : '',
    100 : '',
    101 : '',
    102 : '',
    103 : '',
    104 : 'ACC',
    105 : '',
    106 : '',
    107 : '',
    108 : '',
    109 : '',
    110 : '',
    111 : '',
    112 : 'ACC',
    113 : '',
    114 : '',
    115 : '',
    116 : '',
    117 : '',
    118 : '',
    119 : '',
    120 : 'ACC',
    121 : '',
    122 : '',
    123 : '',
    124 : '',
    125 : '',
    126 : '',
    127 : '',
}


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
            self._frame_bytes_decoded.append((_byte_index, ENGINEER_FRAME_BYTEMAP[_byte_index], self._bytes[_byte_index]))

        self._decode_eng_acc()

    def _decode_eng_acc(self):

        _accel_bytes = self._bytes[::8]
        _values = [b[0] for b in _accel_bytes]
        self._frame_engineering_data['ACC'] = int(sum(_values) / len(_values))

        ...