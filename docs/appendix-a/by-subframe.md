# Appendix A by Sub-frame Position

!!! info "Not part of the original document"
    This page is derived from [Appendix A](index.md) and [Section V, Telemetry Timing Table](../sections/05-timing-table.md). It regroups Appendix A by minor-frame position as a convenience for decoding. Appendix A remains the authoritative transcription.

## Frame structure (from the Telemetry Timing Table)

- Each minor frame lasts 0.5 s and contains 128 words (0–127).
- A major frame is 256 minor frames (0–255), lasting 128 s.
- The analog subcoms (words 58 = ASI 1 and 122 = ASI 2) and the digital subcom (word 59 = DSI) step through subcom words 0–63, so subcom word = minor frame mod 64. Each 64-step cycle runs four times per major frame, starting at minor frames 0, 64, 128 and 192.
- The fixed words (words 60–63) step through subcom words 0–3, so subcom word = minor frame mod 4. Word 60 carries the subcom ID of the current phase in bits 1,0.

So the telemetry content of minor frame *m* depends only on *m* mod 64, which this file calls the **sub-frame position**. There are 64 positions (0–63). Each one occurs four times per major frame.

## How to read this file

0. **Quick reference.** One matrix shows every sub-frame position against the subcommutated words, so you can see at a glance what each frame carries.
1. **Common words.** One table lists the 121 words whose content is the same in every minor frame (all words except 58, 59, 60–63 and 122).
2. **Per-position tables.** Each of the 64 sub-frame position tables lists only the seven words that change: 58, 59, 60, 61, 62, 63 and 122. Position 122/39 has two rows, split by bit range, as in the source.

The other conventions and transcription notes are the same as in [Appendix A](index.md), and its transcription notes are repeated at the end.

## Quick reference: subcommutated words by sub-frame position

Each row is one sub-frame position (minor frame mod 64) and shows what each subcommutated word carries in it. Cells read "Unit ID: Telemetry Descriptor". Words 60–63 follow the fixed-word phase (minor frame mod 4), given in its own column. Full details for each entry (A/D, digital states, remarks) are in the per-position tables further down.

| Pos | Minor frames | Word 58 (ASI 1) | Word 59 (DSI) | Word 122 (ASI 2) | Phase | Word 60 | Word 61 | Word 62 | Word 63 |
|---:|---|---|---|---|:-:|---|---|---|---|
| 0 | 0, 64, 128, 192 | BAH: +5 Volt Pwr Monitor | AM: PAS Attitude | AM: PAS Pwr Mon | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 1 | 1, 65, 129, 193 | BAH: High Voltage A | AM: PAS Attitude | CM: Cmd Dcdr A -10V Mon | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 2 | 2, 66, 130, 194 | BAH: High Voltage B | AM: PAS Attitude | CM: Cmd Dcdr B -10V Mon | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 3 | 3, 67, 131, 195 | BAH: Sweep A Mon | AM: PAS Attitude | AT: Accel Pwr Mon | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 4 | 4, 68, 132, 196 | BAH: Sweep B Mon | AM: PAS Attitude | AT: HPS-A TC | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 5 | 5, 69, 133, 197 | ANH: X-Ray Mem Logic Volt | AM: PAS Attitude | AT: HPS-B TC | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 6 | 6, 70, 134, 198 | ANH: SST Hskg Data | AM: PAS Attitude | AM: FSS-A Pwr Mon | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 7 | 7, 71, 135, 199 | ANH: SST Hskg Data | AM: PAS Attitude | AM: FSS-A Bias Volt | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 8 | 8, 72, 136, 200 | HOH: Hskg Data | AM: PAS Attitude | AM: FSS-B Bias Volt | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 9 | 9, 73, 137, 201 | HOH: Hskg Data | AM: PAS Attitude | CM: Cmd Dcdr A +10V Mon | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 10 | 10, 74, 138, 202 | HOH: Hskg Data | AT: HPS Elec A CMD Status | CM: Cmd Dcdr B +10V Mon | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 11 | 11, 75, 139, 203 | HOH: Hskg Data | AT: HPS Elec A CMD Status | AM: FSS-B Pwr Mon | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 12 | 12, 76, 140, 204 | HOH: GRB PM Volt Mon | AT: HPS Elec A CMD Status | HOH: Low Volt Conv | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 13 | 13, 77, 141, 205 | ANH: X-Ray Hskg Data | AT: HPS Elec A CMD Status | HOH: Stepped Defl Volt (UL) | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 14 | 14, 78, 142, 206 | ANH: X-Ray Hskg Data | AT: HPS Elec A CMD Status | AT: HPS-A Tk Press | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 15 | 15, 79, 143, 207 | CM: Wire Ant Deploy (+) | AT: HPS Elec B CMD Status | AT: HPS-B Tk Press | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 16 | 16, 80, 144, 208 | BAH: Exp Temp | AT: HPS Elec B CMD Status | TL: DMU Temp | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 17 | 17, 81, 145, 209 | AT: Accel Temp | AT: HPS Elec B CMD Status | TYH: HETS Temp | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 18 | 18, 82, 146, 210 | ANH: X-Ray Mem Temp | AT: HPS Elec B CMD Status | SBH: θB or θB* Temp | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 19 | 19, 83, 147, 211 | ANH: X-Ray Temp | AT: HPS Elec B CMD Status | TYH: VLETS Temp | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 20 | 20, 84, 148, 212 | ANH: SST Temp | CM-01: CMD Dcdr B CMD Ctr | AM: FSS Elec Temp | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 21 | 21, 85, 149, 213 | HKH: Drift Chamb Temp | CM-01: CMD Dcdr A CMD Ctr | AM: PAS Elec Temp | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 22 | 22, 86, 150, 214 | HKH: Silicon Det Temp | CM-03: Wire Ant CMD Flags | AM: PAS Sensor Temp | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 23 | 23, 87, 151, 215 | MEH: Elec Temp | CM-03: Wire Ant Deploy Flags | CM: Cmd Dcdr A Temp | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 24 | 24, 88, 152, 216 | MEH: CsI Xtal Temp | BAH: EED No. 1 Arm Status | PW: Btry Temp | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 25 | 25, 89, 153, 217 | HOH: UOM Pkg Temp | BAH: EED No. 2 Arm Status | PW: Pwr Module Temp | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 26 | 26, 90, 154, 218 | HOH: MPI Pkg Temp | Spare | PW: MAM Temp | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 27 | 27, 91, 155, 219 | SCH: Short Ant. Preamp Temp | SBH: CMD State/Status | PW: Solar Array Temps | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 28 | 28, 92, 156, 220 | SCH: B Ant Preamp Temp | SBH: CMD State/Status | SD: Xpndr A WB Fil Temp | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 29 | 29, 93, 157, 221 | STH: Exp Temp | SCH: Inst Status | SD: Xpndr B WB Fil Temp | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 30 | 30, 94, 158, 222 | DFH: Cold Plate Temp | OGH: Exp Status Data | SD: Xpndr A RF Tstr Temp | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 31 | 31, 95, 159, 223 | DFH: Conv Temp | OGH: Exp Status Data | SD: Xpndr B RF Tstr Temp | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 32 | 32, 96, 160, 224 | HKH: Pwr Mon | TL: Sun Time (8 MSB) | TL: +3.2V Cal | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 33 | 33, 97, 161, 225 | IHHK: Exp Status | TL: Sun Time (8 LSB) | TL: +0.1V Cal | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 34 | 34, 98, 162, 226 | HKH: Hskg Data | TL: Sun Period (8 MSB) | TL: +5.0V Cal | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 35 | 35, 99, 163, 227 | HKH: Hskg Data | TL: Sun Period (8 LSB) | TL: +2.5V Cal | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 36 | 36, 100, 164, 228 | CM: Wire Ant Deploy (-) | TL: Mag Time (8 MSB) | TL: Radiation Mon | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 37 | 37, 101, 165, 229 | MEH: Exp Pwr ON Mon | TL: Mag Time (8 LSB) | TL: A/D Ramp | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 38 | 38, 102, 166, 230 | Spare | TL: Mag Period (8 MSB) | TL: 2.5V @ 2 M | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 39 | 39, 103, 167, 231 | SCH: Pwr Mon | TL: Mag Period (8 LSB) | AT: HPS Elec A Temp (s) [bits 0-23]<br>TEH: Exp Temps [bits 24, 25, 26] | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 40 | 40, 104, 168, 232 | STH: Det Temp | TL: SSC Cmd Reg Status R. O | AT: HPS Elec B Temp(s) | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 41 | 41, 105, 169, 233 | DFH: Prm Pwr Conv Mon | TL: SSC Cmd Reg Status R. O. | PW: Btry Disch Cur | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 42 | 42, 106, 170, 234 | DFH: BU Pwr Conv Mon | TL: SSC Cmd Reg Status R. O. | PW: Btry Volt | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 43 | 43, 107, 171, 235 | DFH: Tel 1 Kskg Data | TYH: HET Cmd Status | PW: Main Bus Volt | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 44 | 44, 108, 172, 236 | DFH: Tel 2 Hskg Data | TYH: HET Cmd Status | PW: Non-Ess Bus Cur | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 45 | 45, 109, 173, 237 | DFH: Tel 3 Hskg Data | TYH: HET Cmd Status | PW: Ess Bus Cur | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 46 | 46, 110, 174, 238 | OGH: + Volt Mon | TYH: HET Cmd Status | PW: Solar Array Cur | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 47 | 47, 111, 175, 239 | OGH: High Volt Mon | Spare | PW: Shunt Dump Cur | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 48 | 48, 112, 176, 240 | SBH: B Pwr Mon | PW: Configuration Status | PW: Btry Chg Cur | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 49 | 49, 113, 177, 241 | SBH: B * Pwr Mon | SD: Configuration Status | SD: Xpndr B Sig Str | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 50 | 50, 114, 178, 242 | Spare | SD: Configuration Status | SD: Xpndr A Static Ph | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 51 | 51, 115, 179, 243 | TYH: VLETS Hskg Data | AT: Accel Pulse Ctr | SD: Xpndr B Static Ph | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 52 | 52, 116, 180, 244 | TYH: HETS Pwr Mon | CM: CMD Dcdr B Cmd Ctr | SD: Xpndr A Rcvr Conv Volt | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 53 | 53, 117, 181, 245 | TYH: VLETS Pwr Mon | CM: Cmd Dcdr A CMD Ctr | SD: Xpndr A Xmtr Conv Volt | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 54 | 54, 118, 182, 246 | AM: FSS-A Coarse (V01) | AT: HPS Htrs Cmd Status | SD: Xpndr B Rcvr Conv Volt | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 55 | 55, 119, 183, 247 | AM: FSS-A Coarse (V02) | AT: HPS Htrs Cmd Status | SD: Xpndr B Xmtr Conv Volt | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 56 | 56, 120, 184, 248 | AM: FSS-A Coarse (V03) | Spare | SD: Xpndr A RF Pwr | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 57 | 57, 121, 185, 249 | AM: FSS-A Fine (VS) | Spare | SD: Xpndr B RF Pwr | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 58 | 58, 122, 186, 250 | AM: FSS-A Fine (VC) | Spare | SD: Xpndr A Sig Str | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 59 | 59, 123, 187, 251 | -: Spare | TL: Data System ID | AM: FSS-B Coarse (V01) | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |
| 60 | 60, 124, 188, 252 | SMH: Hskg Data | Spare | AM: FSS-B Coarse (V02) | 0 | Subcom ID = 0 | TL: S/C Clock (8 MSB's) | TL: S/C Clock (Bits 9-16) | TL: S/C Clock (8 LSB's) |
| 61 | 61, 125, 189, 253 | SMH: SA A or X Fld Data | MEH: Inst Status | AM: FSS-B Coarse (VO3) | 1 | Subcom ID = 1 | TL: Variable Mem R/O (8 bits) | TL: Indirect Add Reg (8 bits) | TL: Execute Add R/O (8 bits) |
| 62 | 62, 126, 190, 254 | SMH: SA B or Y Fld Data | MEH: Inst Status | AM: FSS-B Fine (VS) | 2 | Subcom ID = 2 | TL: Status Reg | TL: Status Reg | TL: Status Reg |
| 63 | 63, 127, 191, 255 | SMH: SA C or Z Fld Data | SMH: Inst Status | AM: FSS-B Fine (VC) | 3 | Subcom ID = 3 | TL: Variable Mem R/O (8 bits) | TL: CMD Reg (Bits 1-8) | TL: CMD Reg (Bits 9-16) |

## Common words (identical in every minor frame)

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 0 |  |  | MEH | Cosmic Ray Rlectron Data | D |  | [See B-XIII App B](../appendix-b/b-xiii.md) |
| 1 |  |  | MEH | Cosmic Ray Electron Data | D |  | [See B-XIII App B](../appendix-b/b-xiii.md) |
| 2 |  |  | MEH | Cosmic Ray Electron Data | D |  | [See B-XIII App B](../appendix-b/b-xiii.md) |
| 3 |  |  | MEH | Cosmic Ray Rlectron Data | D |  | [See B-XIII App B](../appendix-b/b-xiii.md) |
| 4 |  |  | SBH | Am Exp. Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 5 |  |  | TYH | VLET PHA Data | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 6 |  |  | TYH | VLET PHA Data | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 7 |  |  | TYH | VLET Rates and PHA Status | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 8 |  |  | TYH | HET Rates | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 9 |  |  | TYH | HET PHA Data | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 10 |  |  | TYH | HET PHA Data | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 11 |  |  | TYH | HET PHA Data | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 12 |  |  | DFH | Tel 1 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 13 |  |  | DFH | Tel 1 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 14 |  |  | DFH | Tel 2 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 15 |  |  | DFH | Tel 2 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 16 |  |  | DFH | Tel 3 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 17 |  |  | DFH | Tel 3 Exp Data | D |  | [See B-X, App B](../appendix-b/b-x.md) |
| 18 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 19 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 20 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 21 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 22 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 23 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 24 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 25 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 26 |  |  | HOH | Exp Data | D |  | [See B-XII, App B](../appendix-b/b-xii.md) |
| 27 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 28 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 29 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 30 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 31 |  |  | HKH | Cosmic Ray Event Data | D |  | [See B-XI, App B](../appendix-b/b-xi.md) |
| 32 |  |  | HKH | Cosmic Ray Event Data | D |  | [See B-XI, App B](../appendix-b/b-xi.md) |
| 33 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 34 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 35 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 36 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 37 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 38 |  |  | OGH | Exp Data | D |  | [See B-XIV, App B](../appendix-b/b-xiv.md) |
| 39 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 40 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 41 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 42 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 43 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 44 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 45 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 46 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 47 |  |  | ANH | X-Ray Experiment Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 48 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 49 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 50 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 51 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 52 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 53 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 54 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 55 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 56 |  |  | SBH | Exp Ph/Status Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 57 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 64 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 65 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 66 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 67 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 68 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 69 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 70 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 71 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 72 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 73 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 74 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 75 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 76 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 77 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 78 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 79 |  |  | ANH | X-Ray Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 80 |  |  | STH | Exp Data | D |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 81 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 82 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 83 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 84 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 85 |  |  | SCH | 16 Chan f₁₆ (100 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 86 |  |  | SCH | 16 Chan f₁₅ (56 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 87 |  |  | SCH | 16 Chan f₁₄ (31 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 88 |  |  | SCH | 16 Chan f₁₃ (17 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 89 |  |  | SCH | 16 Chan f₁₂ (10 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 90 |  |  | SCH | 16 Chan f₁₁ (5.6 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 91 |  |  | SCH | 16 Chan f₁₀ (3.1 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 92 |  |  | SCH | 16 Chan f₉ (1.7 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 93 |  |  | SCH | 16 Chan f₈ (1 KHz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 94 |  |  | SCH | 16 Chan f₇ (560 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 95 |  |  | SCH | 16 Chan f₆ (310 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 96 |  |  | SCH | 16 Chan f₅ (170 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 97 |  |  | SCH | 16 Chan f₄ (100 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 98 |  |  | SCH | 16 Chan f₃ (56 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 99 |  |  | SCH | 16 Chan f₂ (31 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 100 |  |  | SBH | Am Exp Date | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 101 |  |  | SCH | 16 Chan f₁ (17 Hz) Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 102 |  |  | SCH | 8 Chan Data | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 103 |  |  | BAH | Solar Wind Ions Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 104 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 105 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 106 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 107 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 108 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 109 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 110 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 111 |  |  | BAH | Solar Wind Electrons Data | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 112 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 113 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 114 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 115 |  |  | SMH | Triaxial Mag Fld Data | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 116 |  |  | SBH | Am Exp Data | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 117 |  |  | ANH | SST Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 118 |  |  | ANH | SST Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 119 |  |  | ANH | SST Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 120 |  |  | ANH | SST Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 121 |  |  | ANH | SST Exp Data | D |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 123 |  |  | TL | Encoder Dump | D |  |  |
| 124 |  |  | TL | Encoder Dump | D |  |  |
| 125 |  |  | TL | Encoder Dump | D |  |  |
| 126 |  |  | TL | Sync | D |  |  |
| 127 |  |  | TL | Sync | D |  |  |

## Sub-frame position tables

### Sub-frame position 0

Minor frames 0, 64, 128, 192 of each major frame. Subcom word 0 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 0 |  | BAH | +5 Volt Pwr Monitor | A |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 59 | 0 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 0 |  | AM | PAS Pwr Mon | A |  |  |

### Sub-frame position 1

Minor frames 1, 65, 129, 193 of each major frame. Subcom word 1 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 1 |  | BAH | High Voltage A | A |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 59 | 1 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 1 |  | CM | Cmd Dcdr A -10V Mon | A |  |  |

### Sub-frame position 2

Minor frames 2, 66, 130, 194 of each major frame. Subcom word 2 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 2 |  | BAH | High Voltage B | A |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 59 | 2 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 2 |  | CM | Cmd Dcdr B -10V Mon | A |  |  |

### Sub-frame position 3

Minor frames 3, 67, 131, 195 of each major frame. Subcom word 3 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 3 |  | BAH | Sweep A Mon | A |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 59 | 3 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 3 |  | AT | Accel Pwr Mon | A |  |  |

### Sub-frame position 4

Minor frames 4, 68, 132, 196 of each major frame. Subcom word 4 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 4 |  | BAH | Sweep B Mon | A |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 59 | 4 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 4 |  | AT | HPS-A TC | A |  |  |

### Sub-frame position 5

Minor frames 5, 69, 133, 197 of each major frame. Subcom word 5 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 5 |  | ANH | X-Ray Mem Logic Volt | A |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 59 | 5 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 5 |  | AT | HPS-B TC | A |  |  |

### Sub-frame position 6

Minor frames 6, 70, 134, 198 of each major frame. Subcom word 6 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 6 |  | ANH | SST Hskg Data | A |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 59 | 6 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 6 |  | AM | FSS-A Pwr Mon | A |  |  |

### Sub-frame position 7

Minor frames 7, 71, 135, 199 of each major frame. Subcom word 7 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 7 |  | ANH | SST Hskg Data | A |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 59 | 7 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 7 |  | AM | FSS-A Bias Volt | A |  |  |

### Sub-frame position 8

Minor frames 8, 72, 136, 200 of each major frame. Subcom word 8 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 8 |  | HOH | Hskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 8 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 8 |  | AM | FSS-B Bias Volt | A |  |  |

### Sub-frame position 9

Minor frames 9, 73, 137, 201 of each major frame. Subcom word 9 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 9 |  | HOH | Hskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 9 |  | AM | PAS Attitude | D |  | [See B-I, App B](../appendix-b/b-i.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 9 |  | CM | Cmd Dcdr A +10V Mon | A |  |  |

### Sub-frame position 10

Minor frames 10, 74, 138, 202 of each major frame. Subcom word 10 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 10 |  | HOH | Hskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 10 |  | AT | HPS Elec A CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 10 |  | CM | Cmd Dcdr B +10V Mon | A |  |  |

### Sub-frame position 11

Minor frames 11, 75, 139, 203 of each major frame. Subcom word 11 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 11 |  | HOH | Hskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 11 |  | AT | HPS Elec A CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 11 |  | AM | FSS-B Pwr Mon | A |  |  |

### Sub-frame position 12

Minor frames 12, 76, 140, 204 of each major frame. Subcom word 12 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 12 |  | HOH | GRB PM Volt Mon | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 12 |  | AT | HPS Elec A CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 12 |  | HOH | Low Volt Conv | A |  | [See B-XII, App B](../appendix-b/b-xii.md) |

### Sub-frame position 13

Minor frames 13, 77, 141, 205 of each major frame. Subcom word 13 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 13 |  | ANH | X-Ray Hskg Data | A |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 59 | 13 |  | AT | HPS Elec A CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 13 |  | HOH | Stepped Defl Volt (UL) | A |  | [See B-XII, App B](../appendix-b/b-xii.md) |

### Sub-frame position 14

Minor frames 14, 78, 142, 206 of each major frame. Subcom word 14 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 14 |  | ANH | X-Ray Hskg Data | A |  | [See B-VIII, App B](../appendix-b/b-viii.md) |
| 59 | 14 |  | AT | HPS Elec A CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 14 |  | AT | HPS-A Tk Press | A |  |  |

### Sub-frame position 15

Minor frames 15, 79, 143, 207 of each major frame. Subcom word 15 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 15 |  | CM | Wire Ant Deploy (+) | A |  |  |
| 59 | 15 |  | AT | HPS Elec B CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 15 |  | AT | HPS-B Tk Press | A |  |  |

### Sub-frame position 16

Minor frames 16, 80, 144, 208 of each major frame. Subcom word 16 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 16 |  | BAH | Exp Temp | A |  |  |
| 59 | 16 |  | AT | HPS Elec B CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 16 |  | TL | DMU Temp | A |  |  |

### Sub-frame position 17

Minor frames 17, 81, 145, 209 of each major frame. Subcom word 17 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 17 |  | AT | Accel Temp | A |  |  |
| 59 | 17 |  | AT | HPS Elec B CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 17 |  | TYH | HETS Temp | A |  |  |

### Sub-frame position 18

Minor frames 18, 82, 146, 210 of each major frame. Subcom word 18 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 18 |  | ANH | X-Ray Mem Temp | A |  |  |
| 59 | 18 |  | AT | HPS Elec B CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 18 |  | SBH | θB or θB* Temp | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |

### Sub-frame position 19

Minor frames 19, 83, 147, 211 of each major frame. Subcom word 19 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 19 |  | ANH | X-Ray Temp | A |  |  |
| 59 | 19 |  | AT | HPS Elec B CMD Status | D |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 19 |  | TYH | VLETS Temp | A |  |  |

### Sub-frame position 20

Minor frames 20, 84, 148, 212 of each major frame. Subcom word 20 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 20 |  | ANH | SST Temp | A |  |  |
| 59 | 20 |  | CM-01 | CMD Dcdr B CMD Ctr | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 20 |  | AM | FSS Elec Temp | A |  |  |

### Sub-frame position 21

Minor frames 21, 85, 149, 213 of each major frame. Subcom word 21 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 21 |  | HKH | Drift Chamb Temp | A |  |  |
| 59 | 21 |  | CM-01 | CMD Dcdr A CMD Ctr | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 21 |  | AM | PAS Elec Temp | A |  |  |

### Sub-frame position 22

Minor frames 22, 86, 150, 214 of each major frame. Subcom word 22 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 22 |  | HKH | Silicon Det Temp | A |  |  |
| 59 | 22 |  | CM-03 | Wire Ant CMD Flags | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 22 |  | AM | PAS Sensor Temp | A |  |  |

### Sub-frame position 23

Minor frames 23, 87, 151, 215 of each major frame. Subcom word 23 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 23 |  | MEH | Elec Temp | A |  |  |
| 59 | 23 |  | CM-03 | Wire Ant Deploy Flags | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 23 |  | CM | Cmd Dcdr A Temp | A |  |  |

### Sub-frame position 24

Minor frames 24, 88, 152, 216 of each major frame. Subcom word 24 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 24 |  | MEH | CsI Xtal Temp | A |  |  |
| 59 | 24 |  | BAH | EED No. 1 Arm Status | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 24 |  | PW | Btry Temp | A |  |  |

### Sub-frame position 25

Minor frames 25, 89, 153, 217 of each major frame. Subcom word 25 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 25 |  | HOH | UOM Pkg Temp | A |  |  |
| 59 | 25 |  | BAH | EED No. 2 Arm Status | D |  | [See B-IX, App B](../appendix-b/b-ix.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 25 |  | PW | Pwr Module Temp | A |  |  |

### Sub-frame position 26

Minor frames 26, 90, 154, 218 of each major frame. Subcom word 26 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 26 |  | HOH | MPI Pkg Temp | A |  |  |
| 59 | 26 |  |  | Spare |  |  |  |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 26 |  | PW | MAM Temp | A |  |  |

### Sub-frame position 27

Minor frames 27, 91, 155, 219 of each major frame. Subcom word 27 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 27 |  | SCH | Short Ant. Preamp Temp | A |  |  |
| 59 | 27 |  | SBH | CMD State/Status | D |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 27 |  | PW | Solar Array Temps | A |  | [See B-IV, App B](../appendix-b/b-iv.md) |

### Sub-frame position 28

Minor frames 28, 92, 156, 220 of each major frame. Subcom word 28 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 28 |  | SCH | B Ant Preamp Temp | A |  |  |
| 59 | 28 |  | SBH | CMD State/Status | D |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 28 |  | SD | Xpndr A WB Fil Temp | A |  |  |

### Sub-frame position 29

Minor frames 29, 93, 157, 221 of each major frame. Subcom word 29 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 29 |  | STH | Exp Temp | A |  |  |
| 59 | 29 |  | SCH | Inst Status | D |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 29 |  | SD | Xpndr B WB Fil Temp | A |  |  |

### Sub-frame position 30

Minor frames 30, 94, 158, 222 of each major frame. Subcom word 30 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 30 |  | DFH | Cold Plate Temp | A |  |  |
| 59 | 30 |  | OGH | Exp Status Data | D |  | [See B-XIV, App B](../appendix-b/b-xiv.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 30 |  | SD | Xpndr A RF Tstr Temp | A |  |  |

### Sub-frame position 31

Minor frames 31, 95, 159, 223 of each major frame. Subcom word 31 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 31 |  | DFH | Conv Temp | A |  |  |
| 59 | 31 |  | OGH | Exp Status Data | D |  | [See B-XIV, App B](../appendix-b/b-xiv.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 31 |  | SD | Xpndr B RF Tstr Temp | A |  |  |

### Sub-frame position 32

Minor frames 32, 96, 160, 224 of each major frame. Subcom word 32 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 32 |  | HKH | Pwr Mon | A |  |  |
| 59 | 32 |  | TL | Sun Time (8 MSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 32 |  | TL | +3.2V Cal | A |  |  |

### Sub-frame position 33

Minor frames 33, 97, 161, 225 of each major frame. Subcom word 33 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 33 |  | IHHK | Exp Status | A |  |  |
| 59 | 33 |  | TL | Sun Time (8 LSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 33 |  | TL | +0.1V Cal | A |  |  |

### Sub-frame position 34

Minor frames 34, 98, 162, 226 of each major frame. Subcom word 34 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 34 |  | HKH | Hskg Data | A |  | [See B-XI, App B](../appendix-b/b-xi.md) |
| 59 | 34 |  | TL | Sun Period (8 MSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 34 |  | TL | +5.0V Cal | A |  |  |

### Sub-frame position 35

Minor frames 35, 99, 163, 227 of each major frame. Subcom word 35 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 35 |  | HKH | Hskg Data | A |  | [See B-XI, App B](../appendix-b/b-xi.md) |
| 59 | 35 |  | TL | Sun Period (8 LSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 35 |  | TL | +2.5V Cal | A |  |  |

### Sub-frame position 36

Minor frames 36, 100, 164, 228 of each major frame. Subcom word 36 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 36 |  | CM | Wire Ant Deploy (-) | A |  |  |
| 59 | 36 |  | TL | Mag Time (8 MSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 36 |  | TL | Radiation Mon | A |  |  |

### Sub-frame position 37

Minor frames 37, 101, 165, 229 of each major frame. Subcom word 37 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 37 |  | MEH | Exp Pwr ON Mon | A |  | [See B-XIII, App B](../appendix-b/b-xiii.md) |
| 59 | 37 |  | TL | Mag Time (8 LSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 37 |  | TL | A/D Ramp | A |  |  |

### Sub-frame position 38

Minor frames 38, 102, 166, 230 of each major frame. Subcom word 38 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 38 |  |  | Spare | A |  |  |
| 59 | 38 |  | TL | Mag Period (8 MSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 38 |  | TL | 2.5V @ 2 M | A |  |  |

### Sub-frame position 39

Minor frames 39, 103, 167, 231 of each major frame. Subcom word 39 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 39 |  | SCH | Pwr Mon | A |  | [See B-XVI, App B](../appendix-b/b-xvi.md) |
| 59 | 39 |  | TL | Mag Period (8 LSB) | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 39 | 0-23 | AT | HPS Elec A Temp (s) | A |  | [See B-II, App B](../appendix-b/b-ii.md) |
| 122 | 39 | 24, 25, 26 | TEH | Exp Temps | A |  | [See B-XIX, App B](../appendix-b/b-xix.md) |

### Sub-frame position 40

Minor frames 40, 104, 168, 232 of each major frame. Subcom word 40 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 40 |  | STH | Det Temp | A |  | [See B-XVIII, App B](../appendix-b/b-xviii.md) |
| 59 | 40 |  | TL | SSC Cmd Reg Status R. O | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 40 |  | AT | HPS Elec B Temp(s) | A |  |  |

### Sub-frame position 41

Minor frames 41, 105, 169, 233 of each major frame. Subcom word 41 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 41 |  | DFH | Prm Pwr Conv Mon | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 41 |  | TL | SSC Cmd Reg Status R. O. | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 41 |  | PW | Btry Disch Cur | A |  |  |

### Sub-frame position 42

Minor frames 42, 106, 170, 234 of each major frame. Subcom word 42 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 42 |  | DFH | BU Pwr Conv Mon | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 42 |  | TL | SSC Cmd Reg Status R. O. | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 42 |  | PW | Btry Volt | A |  |  |

### Sub-frame position 43

Minor frames 43, 107, 171, 235 of each major frame. Subcom word 43 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 43 |  | DFH | Tel 1 Kskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 43 |  | TYH | HET Cmd Status | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 43 |  | PW | Main Bus Volt | A |  |  |

### Sub-frame position 44

Minor frames 44, 108, 172, 236 of each major frame. Subcom word 44 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 44 |  | DFH | Tel 2 Hskg Data | A |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 44 |  | TYH | HET Cmd Status | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 44 |  | PW | Non-Ess Bus Cur | A |  |  |

### Sub-frame position 45

Minor frames 45, 109, 173, 237 of each major frame. Subcom word 45 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 45 |  | DFH | Tel 3 Hskg Data |  |  | [See B-X, App B](../appendix-b/b-x.md) |
| 59 | 45 |  | TYH | HET Cmd Status | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 45 |  | PW | Ess Bus Cur | A |  |  |

### Sub-frame position 46

Minor frames 46, 110, 174, 238 of each major frame. Subcom word 46 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 46 |  | OGH | + Volt Mon | A |  | [See B-XIV, App B](../appendix-b/b-xiv.md) |
| 59 | 46 |  | TYH | HET Cmd Status | D |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 46 |  | PW | Solar Array Cur | A |  |  |

### Sub-frame position 47

Minor frames 47, 111, 175, 239 of each major frame. Subcom word 47 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 47 |  | OGH | High Volt Mon | A |  | [See B-XIV, App B](../appendix-b/b-xiv.md) |
| 59 | 47 |  |  | Spare |  |  |  |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 47 |  | PW | Shunt Dump Cur | A |  |  |

### Sub-frame position 48

Minor frames 48, 112, 176, 240 of each major frame. Subcom word 48 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 48 |  | SBH | B Pwr Mon | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 59 | 48 |  | PW | Configuration Status | D |  | [See B-IV, App B](../appendix-b/b-iv.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 48 |  | PW | Btry Chg Cur | A |  |  |

### Sub-frame position 49

Minor frames 49, 113, 177, 241 of each major frame. Subcom word 49 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 49 |  | SBH | B * Pwr Mon | A |  | [See B-XV, App B](../appendix-b/b-xv.md) |
| 59 | 49 |  | SD | Configuration Status | D |  | [See B-V, App B](../appendix-b/b-v.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 49 |  | SD | Xpndr B Sig Str | A |  |  |

### Sub-frame position 50

Minor frames 50, 114, 178, 242 of each major frame. Subcom word 50 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 50 |  |  | Spare |  |  |  |
| 59 | 50 |  | SD | Configuration Status | D |  |  |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 50 |  | SD | Xpndr A Static Ph | A |  |  |

### Sub-frame position 51

Minor frames 51, 115, 179, 243 of each major frame. Subcom word 51 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 51 |  | TYH | VLETS Hskg Data | A |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 59 | 51 |  | AT | Accel Pulse Ctr | D |  | [See B-11, App B](../appendix-b/b-ii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 51 |  | SD | Xpndr B Static Ph | A |  |  |

### Sub-frame position 52

Minor frames 52, 116, 180, 244 of each major frame. Subcom word 52 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 52 |  | TYH | HETS Pwr Mon | A |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 59 | 52 |  | CM | CMD Dcdr B Cmd Ctr | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 52 |  | SD | Xpndr A Rcvr Conv Volt | A |  |  |

### Sub-frame position 53

Minor frames 53, 117, 181, 245 of each major frame. Subcom word 53 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 53 |  | TYH | VLETS Pwr Mon | A |  | [See B-XX, App B](../appendix-b/b-xx.md) |
| 59 | 53 |  | CM | Cmd Dcdr A CMD Ctr | D |  | [See B-III, App B](../appendix-b/b-iii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 53 |  | SD | Xpndr A Xmtr Conv Volt | A |  |  |

### Sub-frame position 54

Minor frames 54, 118, 182, 246 of each major frame. Subcom word 54 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 54 |  | AM | FSS-A Coarse (V01) | A |  |  |
| 59 | 54 |  | AT | HPS Htrs Cmd Status | D |  | [See B-11, App B](../appendix-b/b-ii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 54 |  | SD | Xpndr B Rcvr Conv Volt | A |  |  |

### Sub-frame position 55

Minor frames 55, 119, 183, 247 of each major frame. Subcom word 55 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 55 |  | AM | FSS-A Coarse (V02) | A |  |  |
| 59 | 55 |  | AT | HPS Htrs Cmd Status | D |  | [See B-11, App B](../appendix-b/b-ii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 55 |  | SD | Xpndr B Xmtr Conv Volt | A |  |  |

### Sub-frame position 56

Minor frames 56, 120, 184, 248 of each major frame. Subcom word 56 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 56 |  | AM | FSS-A Coarse (V03) | A |  |  |
| 59 | 56 |  |  | Spare | D |  |  |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 56 |  | SD | Xpndr A RF Pwr | A |  |  |

### Sub-frame position 57

Minor frames 57, 121, 185, 249 of each major frame. Subcom word 57 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 57 |  | AM | FSS-A Fine (VS) | A |  |  |
| 59 | 57 |  |  | Spare | D |  |  |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 57 |  | SD | Xpndr B RF Pwr | A |  |  |

### Sub-frame position 58

Minor frames 58, 122, 186, 250 of each major frame. Subcom word 58 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 58 |  | AM | FSS-A Fine (VC) | A |  |  |
| 59 | 58 |  |  | Spare | D |  |  |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 58 |  | SD | Xpndr A Sig Str | A |  |  |

### Sub-frame position 59

Minor frames 59, 123, 187, 251 of each major frame. Subcom word 59 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 59 |  | - | Spare | A |  |  |
| 59 | 59 |  | TL | Data System ID | D |  | [See B-VII, App B](../appendix-b/b-vii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 59 |  | AM | FSS-B Coarse (V01) | A |  |  |

### Sub-frame position 60

Minor frames 60, 124, 188, 252 of each major frame. Subcom word 60 for words 58, 59 and 122; fixed-word phase 0 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 60 |  | SMH | Hskg Data | A |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 59 | 60 |  |  | Spare | D |  |  |
| 60 | 0 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 0 |  |
| 61 | 0 | 7-0 | TL | S/C Clock | D | 8 MSB's |  |
| 62 | 0 | 7-0 | TL | S/C Clock | D | Bits 9-16 |  |
| 63 | 0 | 7-0 | TL | S/C Clock | D | 8 LSB's |  |
| 122 | 60 |  | AM | FSS-B Coarse (V02) | A |  |  |

### Sub-frame position 61

Minor frames 61, 125, 189, 253 of each major frame. Subcom word 61 for words 58, 59 and 122; fixed-word phase 1 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 61 |  | SMH | SA A or X Fld Data | A |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 59 | 61 |  | MEH | Inst Status | D |  | [See B-XIII, App B](../appendix-b/b-xiii.md) |
| 60 | 1 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 0 |  |
| 61 | 1 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 1 | 7-0 | TL | Indirect Add Reg | D | 8 bits |  |
| 63 | 1 | 7-0 | TL | Execute Add R/O | D | 8 bits |  |
| 122 | 61 |  | AM | FSS-B Coarse (VO3) | A |  |  |

### Sub-frame position 62

Minor frames 62, 126, 190, 254 of each major frame. Subcom word 62 for words 58, 59 and 122; fixed-word phase 2 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 62 |  | SMH | SA B or Y Fld Data | A |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 59 | 62 |  | MEH | Inst Status | D |  | [See B-XIII, App B](../appendix-b/b-xiii.md) |
| 60 | 2 | 1,0 | TL | Work 61, 62, 63 Subcom ID | D | Bit 0 = 0 bit 1 = 1 |  |
| 61 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 62 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 63 | 2 | 7-0 | TL | Status Reg | D |  | [See VIII of Text](../sections/08-status-register.md) |
| 122 | 62 |  | AM | FSS-B Fine (VS) | A |  |  |

### Sub-frame position 63

Minor frames 63, 127, 191, 255 of each major frame. Subcom word 63 for words 58, 59 and 122; fixed-word phase 3 for words 60–63.

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 63 |  | SMH | SA C or Z Fld Data | A |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 59 | 63 |  | SMH | Inst Status | D |  | [See B-XVII, App B](../appendix-b/b-xvii.md) |
| 60 | 3 | 1,0 | TL | Word 61, 62, 63 Subcom ID | D | Bit 0 = 1 bit 1 = 1 |  |
| 61 | 3 | 7-0 | TL | Variable Mem R/O | D | 8 bits |  |
| 62 | 3 | 7-0 | TL | CMD Reg | D | Bits 1-8 |  |
| 63 | 3 | 7-0 | TL | CMD Reg | D | Bits 9-16 |  |
| 122 | 63 |  | AM | FSS-B Fine (VC) | A |  |  |

## Transcription notes (from Appendix A)

The tables above are transcribed as printed. Where [Appendix B](../appendix-b/index.md) settles a question, that is noted here; the tables themselves are not changed.

- **58/33**: Unit ID is printed "IHHK". [B-XI](../appendix-b/b-xi.md) lists 58/33 (Exp Status) under **HKH**, which confirms it is a typo.
- **58/34–35**: Only the bottom of the "See B-XI" bracket is legible. [B-XI](../appendix-b/b-xi.md) lists 58/32, 33, 34 and 35 under HKH, so the bracket most likely covers 58/32–35.
- **58/8–12**: These HOH words are bracketed to "See B-X, App B". [B-XII](../appendix-b/b-xii.md) (HOH) lists them, and [B-X](../appendix-b/b-x.md) (DFH) does not, so the B-X reference is an error in the original.
- **58/45, 58/50, 59/26, 59/47**: The Analog/Digital column is blank in the original. [B-X](../appendix-b/b-x.md) gives 58/45 (Tel 3 Hskg Data) as **A**. The others are spares.
- **58/59**: The Unit ID is a single dash. This is a spare.
- **59/51, 59/54–55**: The remark is printed "B-11". [B-II](../appendix-b/b-ii.md) lists these words, which confirms **B-II**. B-II also notes that they are "also listed in B-III as CM-03 outputs", which explains why [Section IX](../sections/09-digital-subcom-word-detail.md) gives unit CM / CM-03.
- **59/50**: Not covered by the B-V remark on the row above. [B-V](../appendix-b/b-v.md) lists both 59/49 and 59/50.
- **Page A-5 brackets** (58/41–63): The bracket lines on this page are skewed, so their ranges were assigned by Unit ID grouping. Appendix B confirms every one: DFH 41–45 → [B-X](../appendix-b/b-x.md), OGH 46–47 → [B-XIV](../appendix-b/b-xiv.md), SBH 48–49 → [B-XV](../appendix-b/b-xv.md), TYH 51–53 → [B-XX](../appendix-b/b-xx.md), SMH 60–63 → [B-XVII](../appendix-b/b-xvii.md).
- **122/39**: This row is split across two rows by the Bit column (0-23 / 24, 25, 26). The Bit column here is the **supercommutation slot**, not a bit position. Word 122/39 is supercommutated 32 times: slots 0–23 are AT, 24–26 are TEH (Teegarden), and the rest are sync. See [B-II](../appendix-b/b-ii.md) and [B-XIX](../appendix-b/b-xix.md).
- **AM** is used as a Unit ID. It is the Attitude Measurement subsystem ([B-I](../appendix-b/b-i.md)), although the glossary only defines AM as "Amplitude".
- **Typos kept as printed**: "Rlectron" (words 0, 3), "Kskg" (58/43), "Work" (60/2), "Date" (word 100), and "VO3" with a letter O (122/61).
