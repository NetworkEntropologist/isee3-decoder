# B-XX. vonRosenvinge (TYH) Experiment Telemetry List

## Page B-32 (Sheet 1 of 1)

*Rev. B, 4/20/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 5 | - | - | TYH | VLET PHA Data | D |  | 128 bits commutated |
| 6 | - | - | TYH | VLET PHA Data | D |  | 128 bits commutated |
| 7 | - | - | TYH | VLET Rates and PHA Status | D |  | 392 bits commutated |
| 8 | - | - | TYH | HET Rates | D |  | 512 bits commutated |
| 9 | - | - | TYH | HET PHA Data | D |  | 48 bits commutated |
| 10 | - | - | TYH | HET PHA Data | D |  | 48 bits commutated |
| 11 | - | - | TYH | HET PHA Data | D |  | 48 bits commutated |
| 58 | 51 | See below | TYH | VLET Hskg Data | A |  |  |
| 58 | 51 | 7 | TYH | +12 Volt Mon | A |  |  |
| 58 | 51 | 6 | TYH | +6 Volt Mon | A |  |  |
| 58 | 51 | 5 | TYH | Preamp Temp | A |  |  |
| 58 | 51 | 4 | TYH | Pwr Conv Temp | A |  |  |
| 58 | 51 | 3, 2 | TYH | Spare | A |  |  |
| 58 | 51 | 1 | TYH | -6 V Mon | A |  |  |
| 58 | 51 | 0 | TYH | -12V Mon | A |  |  |
| 58 | 52 | - | TYH | HETS Pwr Mon | A |  |  |
| 58 | 53 | - | TYH | VLET Pwr Mon | A |  |  |
| 59 | 43 | - | TYH | HET Cmd Status | D |  | word 1 of 4 |
| 59 | 44 | - | TYH | HET Cmd Status | D |  | word 2 of 4 |
| 59 | 45 | - | TYH | HET Cmd Status | D |  | word 3 of 4 |
| 56 | 46 | - | TYH | HET Cmd Status | D |  | word 4 of 4 |
| 122 | 17 | - | TYH | HETS Temp | A |  |  |
| 122 | 19 | - | TYH | HETS Temp | A |  |  |

Words 59/44–46 are ditto marks (" " ") under "HET Cmd Status" in the original and are written out here.

The last HET Cmd Status row is printed with minor frame word **56**, not 59. Subcom word 46 and "word 4 of 4" show it is 59/46 ([Appendix A](../appendix-a/index.md) agrees).

122/19 is printed "HETS Temp" here, but [Appendix A](../appendix-a/index.md) and [Section VII](../sections/07-subcom-formats.md) give 122/19 as **VLETS Temp**.

The Bit column for 58/51 lists eight housekeeping parameters on bits 7–0 of an *analog* subcom word. This most likely means eight commutated slots, as with 122/39, rather than literal bit positions.

