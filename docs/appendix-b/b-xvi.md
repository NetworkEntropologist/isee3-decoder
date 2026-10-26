# B-XVI. Scarf (SCH) Experiment Telemetry List

## Page B-25 (Sheet 1 of 3)

*Rev. C, 9/8/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 27 | - | SCH | Short Ant Preamp Temp | A |  |  |
| 58 | 28 | - | SCH | B Ant Preamp Temp | A |  |  |
| 58 | 39 | - | SCH | Pwr Mon | A | > 2.5 VDC = ON |  |
| 59 | 29 | See below | SCH | Inst Status | D |  |  |
| 59 | 29 | 7 (MSB), 6, 5 | SCH | 8 Chan MX ID | D | Octal 0 = 1000 Hz<br>1 = 560 Hz<br>2 = 310 Hz<br>3 = 170 Hz<br>4 = 100 Hz<br>5 = 56 Hz<br>6 = 31 Hz<br>7 = 17 Hz |  |
| 59 | 29 | 4 | SCH | Not Used |  |  |  |
| 59 | 29 | 3 | SCH | Lg Ant Cmpt Active | D | 0/1 = U/V |  |
| 59 | 29 | 2 | SCH | Ant Conn to 16 Chan | D | 0/1 = B/Lg (If Bit 1 = 1) |  |
| 59 | 29 | 1 | SCH | Ant Conn to 16 Chan | D | 0/1 = Short/Lg or B |  |
| 59 | 29 | 0 | SCH | Ant Conn to 8 Chan | D | 0/1 = B/Short |  |

## Page B-26 (Sheet 2 of 3)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 85 | - |  | SCH | 16 Chan f<sub>16</sub> (100 KHz) Data | A |  |  |
| 86 | - |  | SCH | 16 Chan f<sub>15</sub> (56 KHz) Data | A |  |  |
| 87 | - |  | SCH | 16 Chan f<sub>14</sub> (31 KHz) Data | A |  |  |
| 88 | - |  | SCH | 16 Chan f<sub>13</sub> (17 KHz) Data | A |  |  |
| 89 | - |  | SCH | 16 Chan f<sub>12</sub> (10 KHz) Data | A |  |  |
| 90 | - |  | SCH | 16 Chan F<sub>11</sub> (5.6 KHz) Data | A |  |  |
| 91 | - |  | SCH | 16 Chan f<sub>10</sub> (3.1 KHz) Data | A |  |  |
| 92 | - |  | SCH | 16 Chan f<sub>9</sub> (1.7 KHz) Data | A |  |  |
| 93 | - |  | SCH | 16 Chan f<sub>8</sub> (1 KHz) Data | A |  |  |
| 94 | - |  | SCH | 16 Chan f<sub>7</sub> (560 Hz) Data | A |  |  |
| 95 | - |  | SCH | 16 Chan f<sub>6</sub> (310 Hz) Data | A |  |  |
| 96 | - |  | SCH | 16 Chan f<sub>5</sub> (170 Hz) Data | A |  |  |
| 97 | - |  | SCH | 16 Chan f<sub>4</sub> (100 Hz) Data | A |  |  |
| 98 | - |  | SCH | 16 Chan f<sub>3</sub> (56 Hz) Data | A |  |  |
| 99 | - |  | SCH | 16 Chan f<sub>2</sub> (31 Hz) Data | A |  |  |
| 101 | - |  | SCH | 16 Chan f<sub>1</sub> (17 Hz) Data | A |  |  |

## Page B-27 (Sheet 3 of 3)

*Rev. B, 4/20/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 102 | - | - | SCH | 8 Chan Data | A |  | 8 Parameters Commutated:<br>8. f<sub>1</sub> (17 Hz) Data<br>7. f<sub>2</sub> (31 Hz) Data<br>6. f<sub>3</sub> (56 Hz) Data<br>5. f<sub>4</sub> (100 Hz) Data<br>4. f<sub>5</sub> (170 Hz) Data<br>3. f<sub>6</sub> (310 Hz) Data<br>2. f<sub>7</sub> (560 Hz) Data<br>1. f<sub>8</sub> (1 KHz) Data |

## Transcription notes

- The section title is printed "Scarf". The glossary spells it Scharf. On sheet 2, f<sub>11</sub> is printed with a capital F.

