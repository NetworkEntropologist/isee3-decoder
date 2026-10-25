
import json
import frames, telemetry.frame

telemetry_file = 'raw-telemetry/20140706.log'

frame_data = frames.parse_file(frames.load_file(telemetry_file))

frame_60_values = {}

for _frame_sequence in range(20):
    _new_frame = telemetry.frame.TelemetryFrame(frame_data[_frame_sequence])

    print(f'{_new_frame.FRAME_SEQUENCE} : {_new_frame.FRAME_TIME} : {_new_frame.FRAME_COUNTER} : {_new_frame.SCIENCE_MODE}')

#     frame_60_values[_new_frame.frame_counter] = _new_frame.frame_counter
        
# print(json.dumps(frame_60_values, indent=2))

