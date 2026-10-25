
import json
import frames, telemetry.frame

telemetry_file = 'raw-telemetry/20140709.log'

frame_data = frames.parse_file(frames.load_file(telemetry_file))

frame_60_values = {}

for frame in frame_data:
    for key, value in frame.items():
        _new_frame = telemetry.frame.TelemetryFrame(key, value)
        frame_60_values[key] = int(_new_frame.frame_counter, 16)
        
print(json.dumps(frame_60_values, indent=2))

