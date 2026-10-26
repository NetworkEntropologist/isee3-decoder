# B-II. Attitude and Orbit Control (AT) Subsystem Telemetry List

## Page B-3 (Sheet 1 of 1)

*Rev. C, 9/8/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 17 | - | AT | Accel Temp | A |  |  |
| 59 | 10 | - | AT | AOCS Elec A CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 11 | - | AT | AOCS Elec A CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 12 | - | AT | AOCS Elec A CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 13 | - | AT | AOCS Elec A CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 14 | - | AT | AOCS Elec A CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 15 | - | AT | AOCS Elec B CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 16 | - | AT | AOCS Elec B CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 17 | - | AT | AOCS Elec B CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 18 | - | AT | AOCS Elec B CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 19 | - | AT | AOCS Elec B CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | 40 Bit Word |
| 59 | 51 | - | AT | Accel Pulse Ctr | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | Also listed in [B-III](b-iii.md) as CM-03 Outputs |
| 59 | 54 | - | AT | HPS Htrs CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | Also listed in [B-III](b-iii.md) as CM-03 Outputs |
| 59 | 55 | - | AT | HPS Htrs CMD Status | D | [See IX of Text](../sections/09-digital-subcom-word-detail.md) | Also listed in [B-III](b-iii.md) as CM-03 Outputs |
| 61 | 2 | 5 | AT | HPS A LV 1 POS | D | 0/1 = Closed/Open | Fixed Word Status Bits, [See VIII of Text](../sections/08-status-register.md) |
| 61 | 2 | 3 | AT | HPS A LV 3 POS | D | 0/1 = Closed/Open | Fixed Word Status Bits, [See VIII of Text](../sections/08-status-register.md) |
| 61 | 2 | 4 | AT | HPS B LV 2 POS | D | 0/1 = Closed/Open | Fixed Word Status Bits, [See VIII of Text](../sections/08-status-register.md) |
| 61 | 2 | 2 | AT | HPS B LV 4 POS | D | 0/1 = Closed/Open | Fixed Word Status Bits, [See VIII of Text](../sections/08-status-register.md) |
| 122 | 3 | - | AT | Accel Pwr Mon | A | > 0.5 V = On |  |
| 122 | 4 | - | AT | HPS-A TC 5 | A |  |  |
| 122 | 5 | - | AT | HPS-B TC 6 | A |  |  |
| 122 | 14 | - | AT | HPS-A Tk Press | A |  |  |
| 122 | 15 | - | AT | HPS-B Tk Press | A |  |  |

## Page B-3a (Sheet 1a)

*Rev. B, 4/20/77*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 122 | 39 | 0 - 23 | AT | HPS -A Elec A Temp (s) | A |  | Word 39 is supercommutated 32 times. 0 thru 23 contain AT data. 24, 25 and 26 contain TEH data. Remaining are used for sync. |
| 122 | 40 | 0-23 | AT | HPS-B Elec B Temp (s) | A |  | Word 40 is supercommutated 32 times. 0 thru 23 contain AT data. The remaining are used for sync. |

## Transcription notes

- Words 59/10–19 are called **AOCS Elec A/B CMD Status** here, and **HPS Elec A/B CMD Status** in [Appendix A](../appendix-a/index.md). The 40 Bit Word brackets group 59/10–14 (Elec A) and 59/15–19 (Elec B). Their bit layout is in [Section IX](../sections/09-digital-subcom-word-detail.md).
- This page resolves the unit-ID difference noted in Section IX. 59/51, 59/54 and 59/55 are AT telemetry that is also listed in [B-III](b-iii.md) as CM-03 outputs.
- Sheet B-3a explains the **0-23** in the Bit column of 122/39 and 122/40. It is the supercommutation slot (32 slots per word), not a bit position. Slots 24–26 of 122/39 are the [TEH](b-xix.md) temperatures.

