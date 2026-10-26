# B-XV. Steinberg (SBH) Experiment Telemetry List

## Page B-22 (Sheet 1 of 3)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 4 | - | - | SBH | Am Exp Data | A |  |  |
| 20 | - | - | SBH | Am Exp Data | A |  |  |
| 36 | - | - | SBH | Am Exp Data | A |  |  |
| 52 | - | - | SBH | Am Exp Data | A |  |  |
| 56 | - | - | SBH | Exp Ph/Status Data | A |  |  |
| 58 | 48 | - | SBH | B Pwr Mon | A | > 1.0 VDC = On |  |
| 58 | 49 | - | SBH | B\* Pwr Mon | A | > 1.0 VDC = On |  |
| 59 | 27 | See below | SBH | CMD State/Status | D |  |  |
| 59 | 27 | 7 (MSB) | SBH | Inhibit | D | See Remarks | 0/1 = Norm Rcvr Opn/Sync Sig to Rcvr Inhibited |
| 59 | 27 | 6 | SBH | Status Sel | D | See Remarks | 0/1 = Status B/Status B\* |
| 59 | 27 | 5 | SBH | Cal Mode | D | See Remarks | 0/1 = No Cal on Previous Cmd Exec/Cal on previous Cmd Exec or Pwr ON |
| 59 | 27 | 4 (MSB), 3 | SBH | Maj Frame Type | D | See Remarks | 00 = Type 3<br>01 = Type 1<br>10 = Type 2 |
| 59 | 27 | 2 (MSB), 1 | SBH | Mode ID (from Last CMD exec) | D | See Remarks | 00 = Mode 1 (B:B\*)<br>01 = Mode 2 (B only)<br>10 = Mode 3 (B\* only) |
| 59 | 27 | 0 | SBH | CM1 Cmd Verif | D | See Remarks | 0/1 = PAV + Pwr ON/PAV + PWR OFF |

## Page B-23 (Sheet 2 of 3)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 59 | 28 | See below | SBH | CMD State/Status | D |  |  |
| 59 | 28 | 7 (MSB) | SBH | CM2 CMD Verif | D | See Remarks | 0/1 = PAV - PWR ON/PAV - PWR OFF |
| 59 | 28 | 6 | SBH | CM3 CMD Verif | D | See Remarks | 0/1 = PAU + PWR ON/PAU + PWR OFF |
| 59 | 28 | 5 | SBH | CM4 CMD Verif | D | ″ | 0/1 = PAU - PWR ON/PAU - PWR OFF |
| 59 | 28 | 4 | SBH | CM5 CMD Verif | D | ″ | 0/1 = PAZ + PWR ON/PAZ + PWR OFF |
| 59 | 28 | 3 | SBH | CM6 CMD Verif | D | ″ | 0/1 = PAZ - PWR ON/PAZ - PWR OFF |
| 59 | 28 | 2 | SBH | CM7 CMD Verif | D | ″ | 0/1 = NG PWR ON/NG PWR OFF |
| 59 | 28 | 1 | SBH | CM8 CMD Verif | D | ″ | 0/1 = Dipole U/Dipole V |
| 59 | 28 | 0 (LSB) | SBH | Status B\* | D | ″ | 0 = Normal seq of Status B and Status B\*<br>1 = Only Status B\* is Mon |

The Minor Frame Word and Subcom Word cells of the bit 0 row are blank in the original; 59/28 is implied and written out here.

## Page B-24 (Sheet 3 of 3)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 68 | - | - | SBH | Am Exp Data | A |  |  |
| 84 | - | - | SBH | Am Exp Data | A |  |  |
| 100 | - | - | SBH | Am Exp Data | A |  |  |
| 116 | - | - | SBH | Am Exp Data | A |  |  |
| 122 | 18 | - | SBH | θB or θB\* Temp | A |  | θB thermistor connected to primary DHU. θB\* is connected to the backup DHU. |

