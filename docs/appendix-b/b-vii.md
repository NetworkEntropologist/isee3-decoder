# B-VII. Telemetry and Data Processing (TL) Subsystem Telemetry List

## Page B-8 (Sheet 1 of 3)

*Rev. B, 4/20/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 59 | 32 | - | TL | Sun Time (8 MSB) | D |  |  |
| 59 | 33 | - | TL | Sun Time (8 LSB) | D |  |  |
| 59 | 34 | - | TL | Sun Period (8 MSB) | D |  |  |
| 59 | 35 | - | TL | Sun Period (8 LSB) | D |  |  |
| 59 | 36 | - | TL | Mag Time (8 MSB) | D |  |  |
| 59 | 37 | - | TL | Mag Time (8 LSB) | D |  |  |
| 59 | 38 | - | TL | Mag Period (8 MSB) | D |  |  |
| 59 | 39 | - | TL | Mag Period (8 LSB) | D |  |  |
| 59 | 40 | See below | TL | SSC CMD Reg Status | D |  |  |
| 59 | 40 | 7-0 | TL | CMD C4 thru C11 Verif | D |  |  |
| 59 | 41 | See below | TL | SSC CMD Reg Status | D |  |  |
| 59 | 41 | 7-0 | TL | CMD C12 thru C19 Verif | D |  |  |
| 59 | 42 | See below | TL | SSC CMD Reg Status | D |  |  |
| 59 | 42 | 7, 6, 5, 4 | TL | CMD C20 thru C23 Verif | D |  |  |
| 59 | 42 | 3 | TL | OA Complete | D | See Remarks | 1 = Sun Time and Sun Period Complete |
| 59 | 42 | 2 | TL | Mag Complete | D | See Remarks | 1 = Mag Time and Mag Period Complete |
| 59 | 42 | 1 | TL | Sun Control | D | See Remarks | 1/0 = Sun Sensor/ Generated Pulse |
| 59 | 42 | 0 | TL | MTOS | D | See Remarks | 1 = Sun Period increased more than 2 times or disappeared totally. |
| 59 | 59 | 7-0 | TL | Data System ID | D | All 1's = DHUB; All 0's = DHUA |  |

## Page B-9 (Sheet 2 of 3)

*Rev. B, 4/20/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 60 |  | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | See Remarks | 00 = Subcom Word 0; 01 = Subcom Word 1; 10 = Subcom Word 2; 11 = Subcom Word 3 |
| 61 | 0 | 7-0 |  | S/C Clock | D | 8 MSB's |  |
| 61 | 1 | 7-0 |  | Variable Mem RO | D |  |  |
| 61 | 2 | 7 |  | TLM Parity | D | See Remarks | 0/1 = Correct/Wrong |
| 61 | 3 | 7-0 |  | Variable Mem RO | D |  |  |
| 62 | 0 | 7-0 |  | S/C Clock | D | Bits 9-16 |  |
| 62 | 1 | 7-0 |  | Indirect Add Reg | D |  |  |
| 62 | 3 | 7-0 |  | Cmd Reg | D | Bits 1-8 |  |
| 63 | 0 | 7-0 |  | S/C Clock | D | 8 LSB's |  |
| 63 | 1 | 7-0 |  | Execute Add RO | D | 8 Bits |  |
| 63 | 3 | 7-0 |  | Cmd Reg | D | Bits 9-16 |  |
| 122 | 16 | 7-0 |  | DMU Temp | A |  |  |
| 122 | 32 | 7-0 |  | +3.2V Cal | A |  |  |
| 122 | 33 | 7-0 |  | +0.1V Cal | A |  |  |
| 122 | 34 | 7-0 |  | +5.0V Cal | A |  |  |
| 122 | 35 | 7-0 |  | +2.5V Cal | A |  |  |
| 122 | 36 | 7-0 |  | Radiation Mon | A |  |  |
| 122 | 37 | 7-0 |  | A/D Ramp | A |  |  |
| 122 | 38 | 7-0 |  | 2.5V at 2M | A |  |  |

## Page B-10 (Sheet 3 of 3)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 123 | - | - | TL | Encoder Dump | D |  |  |
| 124 | - | - | TL | Encoder Dump | D |  |  |
| 125 | - | - | TL | Encoder Dump | D |  |  |
| 126 | - | - | TL | Sync | D |  |  |
| 127 | - | - | TL | Sync | D |  |  |

## Transcription notes

- The Unit ID column on sheet 2 is blank except for the first row (word 60). All the entries are TL telemetry.

