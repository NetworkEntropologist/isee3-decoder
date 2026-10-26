# B-XII. Hovestat (HOH) Experiment Telemetry List

## Page B-18 (Sheet 1 of 2)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 18 | - | - | HOH | Exp Data | D |  | See note A |
| 19 | - | - | HOH | Exp Data | D |  | See note A |
| 21 | - | - | HOH | Exp Data | D |  | See note A |
| 22 | - | - | HOH | Exp Data | D |  | See note A |
| 23 | - | - | HOH | Exp Data | D |  | See note A |
| 24 | - | - | HOH | Exp Data | D |  | See note A |
| 25 | - | - | HOH | Exp Data | D |  | See note A |
| 26 | - | - | HOH | Exp Data | D |  | See note A |
| 58 | 8 | - | HOH | Hskg Data | A |  | 4 parameters commutated (MX ADDR\* → parameter):<br>0 +20 KV Mon<br>1 Test Ref<br>2 +20 KV Mon<br>3 Test Ref |
| 58 | 9 | - | HOH | Hskg Data | A |  | 4 parameters commutated (MX ADDR\* → parameter):<br>0 +2.8 KV Mon<br>1 -11.9 KV Mon<br>2 Cold plate temp<br>3 Det Bias |

**Note A** (bracketed remark covering words 18–26): Each minor frame contains data transmitted in 1 of 5 "formats" (A thru E). The sequence in which the 5 formats are transmitted repeats itself every 16 minor frames. The "normal" sequence is selected by the instrument DPU, but can be altered by command.

\* MX ADDR is indicated by the last 2 bits of Experiment Data Format D.

## Page B-19 (Sheet 2 of 2)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 10 | - | HOH | Hskg Data | A |  | 4 parameters commutated (MX ADDR\* → parameter):<br>0 Gas Press 1 (UW)<br>1 Valve Temp 1<br>2 Gas Press 1<br>3 PC - Bias 1 (UW) |
| 58 | 11 | - | HOH | Hskg Data | A |  | 4 parameters commutated (MX ADDR\* → parameter):<br>0 Gas Press 2 (UH)<br>1 Valve Temp 2<br>2 Gas Press 2<br>3 PC - Bias 2 (UH) |
| 58 | 12 | - | HOH | GRB PM Volt Mon | A | > 3 VDC = ON |  |
| 58 | 25 | - | HOH | UOM Pkg Temp | A |  |  |
| 58 | 26 | - | HOH | MPI Pkg Temp | A |  |  |
| 122 | 12 | - | HOH | Low Volt Conv | A | > 3 VDC = ON |  |
| 122 | 13 | - | HOH | Stepped Defl Volt (UL) | A |  |  |

\* MX ADDR is indicated by the last 2 bits of Experiment Data Format D.

## Transcription notes

- The section title is printed "Hovestat". The glossary spells it Hovestadt.
- UW, UH and UL here are the abbreviations left undefined in the [Glossary](../sections/15-glossary.md).
- Word 20 (between 19 and 21) is SBH data. See [B-XV](b-xv.md).

