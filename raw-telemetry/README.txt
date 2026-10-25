This is a collection of engineering and science telemetry from ISEE-3.

The earlier files are engineering and the later science.

You can tell which is which by looking at the first column in each frame.

If the values are more of less the same (around 77 - the idle accelerometer value), 
it's in engineering mode (otherwise it's in science mode).

You can decode these using: https://github.com/balint256/ice/
Use the '-i' option, and '-S' to throttle (adjust sleep time with '-s').
