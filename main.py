
import json
import frames, telemetry

telemetry_file = 'raw-telemetry/20140709.log'

frame_data = frames.parse_file(frames.load_file(telemetry_file))

frame_60_values = {}

for frame in frame_data:
    for key, value in frame.items():
        frame_60_values[key] = int(str(telemetry.frame_counter(value)), 16)
        
done = input("Done.")

