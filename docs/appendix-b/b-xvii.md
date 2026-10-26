# B-XVII. Smith (SMH) Experiment Telemetry List

## Page B-28 (Sheet 1 of 2)

*Rev. C, 9/8/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 27 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A |
| 28 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A |
| 29 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A |
| 30 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A |
| 58 | 60 | - | SMH | Hskg Data | A |  | 8 Parameters Commutated:<br>1. First Pos ID (OV)<br>2. PA Out V RMS<br>3. Elec Temp<br>4. Sensor Temp<br>5. +12 VDC Supply Mon<br>6. A/D Conv. Ref Volt<br>7. Range ID<br>8. +24 VDC RF PS Volt |
| 58 | 61 | - | SMH | SA A or X Fld Data | A |  | The type of data received (SA or Fld) is selected by command (P68). |
| 58 | 62 | - | SMH | SA B or Y Fld Data | A |  | The type of data received (SA or Fld) is selected by command (P68). |
| 58 | 63 | - | SMH | SA C or Z Fld Data | A |  | The type of data received (SA or Fld) is selected by command (P68). |
| 59 | 63 | See below | SMH | Inst Status | D |  |  |
| 59 | 63 | 7 (MSB) | SMH | Cal Status | D | 0/1 = OFF/ON |  |
| 59 | 63 | 6 | SMH | Ranging Mode | D | 0/1 = Man/Auto |  |
| 59 | 63 | 5 | SMH | Analog Data Mode | D | 0/1 = Normal/Alt. |  |
| 59 | 63 | 4, 3, 2 | SMH | Cal Step ID | D | BCD 0 = Step 1<br>1 = Step 2<br>2 = Step 3<br>3 = Step 4<br>4 = Step 5<br>5 = Step 6<br>6 = Step 7<br>7 = Step 8 | Data is valid to identify steps only when Bit 7 = 1. |
| 59 | 63 | 1, 0 (LSB) | SMH | Not Used |  |  |  |

**Note A** (bracketed remark covering words 27–30): 32 bit word.<br>bits 0-2, Inst. Opn. Range ID<br>bits 3-11, X-Axis Mag Fld<br>bits 12-20, Y-Axis Mag Fld<br>bits 21-29, Z-Axis Mag Fld<br>bits 30, 31, Not Used

## Page B-29 (Sheet 2 of 2)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 70 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 71 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 72 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 73 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 112 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 113 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 114 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |
| 115 | - | - | SMH | Triaxial Mag Fld Data | D |  | See note A (32 bit word) |

**Note A**: each group of four words (70–73 and 112–115) is one 32 bit word, laid out as on sheet 1: bits 0-2, Inst. Opn. Range ID; bits 3-11, X-Axis Mag Fld; bits 12-20, Y-Axis Mag Fld; bits 21-29, Z-Axis Mag Fld; bits 30, 31, Not Used.

