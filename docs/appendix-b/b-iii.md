# B-III. Command (CM) Subsystem Telemetry List

## Page B-4 (Sheet 1 of 1)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 15 | - | CM-03 | Wire Ant Deploy (+) | A |  |  |
| 58 | 36 | - | CM-03 | Wire Ant Deploy (-) | A |  |  |
| 59 | 20 | - | CM-01 | Cmd Dcdr B Cmd Ctr | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 21 | - | CM-01 | Cmd Dcdr A Cmd Ctr | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 22 | - | CM-03 | Wire Ant CMD Flags | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 23 | 7-2 | CM-03 | Wire Ant Deploy Flags | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 23 | 1 | CM-03 | Btry Present | D | 0/1 = OFF/ON | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 51 | - | CM-03 | Accel Pulse Ctr | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 52 | - | CM-01 | Cmd Dcdr B CMD Ctr | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 53 | - | CM-01 | Cmd Dcdr A CMD Ctr | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 54 | - | CM-03 | HPS Htrs CMD Status | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 59 | 55 | - | CM-03 | HPS Htrs CMD Status | D |  | [See IX of Text](../sections/09-digital-subcom-word-detail.md) |
| 61 | 2 | 0 | CM-03 | 3D SSS Bypass | D | See Remarks | 0/1 = Disabled/Enabled |
| 62 | 2 | 7 | CM-03 | Timer A | D | ″ | 0/1 = Disabled/Enabled |
| 62 | 2 | 6 | CM-03 | Timer B | D | ″ | 0/1 = Disabled/Enabled |
| 122 | 1 | - | CM-01 | CMD Dcdr A -10V Mon | A |  |  |
| 122 | 2 | - | CM-01 | CMD Dcdr B -10V Mon | A |  |  |
| 122 | 9 | - | CM-01 | CMD Dcdr A +10V Mon | A |  |  |
| 122 | 10 | - | CM-01 | CMD Dcdr B +10V Mon | A |  |  |
| 122 | 23 | - | CM-01 | CMD Dcdr A Temp | A |  |  |

## Transcription notes

- The See IX of Text bracket appears to start at 58/36. It is applied here only to the DSI (word 59) rows, which are the ones Section IX covers.
- 62/2 bits 7 and 6 (Timer A and Timer B) are shown as **Spare** in [Section VIII](../sections/08-status-register.md). [B-VI](b-vi.md) agrees with this page.

