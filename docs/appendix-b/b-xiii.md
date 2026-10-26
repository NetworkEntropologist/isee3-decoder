# B-XIII. Meyer (MEH) Experiment Telemetry List

## Page B-20 (Sheet 1 of 1)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 0 | - | - | MEH | Cosmic Ray Electron Data | D |  | See note A |
| 1 | - | - | MEH | Cosmic Ray Electron Data | D |  | See note A |
| 2 | - | - | MEH | Cosmic Ray Electron Data | D |  | See note A |
| 3 | - | - | MEH | Cosmic Ray Electron Data | D |  | See note A |
| 58 | 23 | - | MEH | Elec Temp | A |  |  |
| 58 | 24 | - | MEH | CsI Xtal Temp | A |  |  |
| 58 | 37 | - | MEH | Exp Pwr On Mon | A | > 2.5 V = ON |  |
| 59 | 61 | - | MEH | Inst Status | D |  | See note B |
| 59 | 62 | - | MEH | Inst Status | D |  | See note B |

**Note A** (bracketed remark covering words 0–3): 3 types of data, selected internally.<br>1. Event Readout: 96 bits (3 cons. minor frames) per event.<br>2. Rate Readout: occurs every 32 spins. 224 bits (7 cons. minor frames).<br>3. Null Readout: No data available.

**Note B** (bracketed remark covering DSI words 61–62): 64 bits commutated.<br>bits 1-32, command verification<br>bits 33-40, general status<br>bits 41-52, GH rate<br>bits 53-64, GB rate

