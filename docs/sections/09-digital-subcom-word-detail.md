# IX. ISEE-C Digital Subcom Word Detail

These tables give the bit-level meaning of the digital subcom (DSI, minor frame word 59) words marked \* in [Section VII](07-subcom-formats.md). The word numbers are DSI subcom word numbers. Bit 7 is the MSB and bit 0 the LSB. Where the 0/1 columns are empty, the bit is part of a binary value whose weight is shown in the Function column.

## Sheet 1 of 6

*Original page 7, Revision B, 4/20/77*

### Word 10

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster No. 1 Select | Not-Selected | Selected |
| 6 | Thruster No. 2 Select | Not-Selected | Selected |
| 5 | Thruster No. 3 Select | Not-Selected | Selected |
| 4 | Thruster No. 4 Select | Not-Selected | Selected |
| 3 | Thruster No. 5 Select | Not-Selected | Selected |
| 2 | Thruster No. 6 Select | Not-Selected | Selected |
| 1 | Thruster No. 7 Select | Not-Selected | Selected |
| 0 (LSB) | Thruster No. 8 Select | Not-Selected | Selected |

### Word 11

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster No. 11 Select | Not-Selected | Selected |
| 6 | Thruster No. 12 Select | Not-Selected | Selected |
| 5 | Thruster No. 9 Select | Not-Selected | Selected |
| 4 | Thruster No. 10 Select | Not-Selected | Selected |
| 3 | Sector Initiate (2<sup>9</sup>) |  |  |
| 2 | Sector Initiate (2<sup>8</sup>) |  |  |
| 1 | Sector Initiate (2<sup>7</sup>) |  |  |
| 0 (LSB) | Sector Initiate (2<sup>6</sup>) |  |  |

### Word 12

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Sector Initiate (2<sup>5</sup>) |  |  |
| 6 | Sector Initiate (2<sup>4</sup>) |  |  |
| 5 | Sector Initiate (2<sup>3</sup>) |  |  |
| 4 | Sector Initiate (2<sup>2</sup>) |  |  |
| 3 | Sector Initiate (2<sup>1</sup>) |  |  |
| 2 | Sector Initiate (2<sup>0</sup>) |  |  |
| 1 | Sector Width Select B |  |  |
| 0 (LSB) | Sector Width Select A |  |  |

### Word 13

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | No. Firing Pulses or Spin Revolutions (2<sup>10</sup>) |  |  |
| 6 | No. Firing Pulses or Spin Revolutions (2<sup>5</sup>) |  |  |
| 5 | No. Firing Pulses or Spin Revolutions (2<sup>4</sup>) |  |  |
| 4 | No. Firing Pulses or Spin Revolutions (2<sup>3</sup>) |  |  |
| 3 | No. Firing Pulses or Spin Revolutions (2<sup>2</sup>) |  |  |
| 2 | No. Firing Pulses or Spin Revolutions (2<sup>1</sup>) |  |  |
| 1 | No. Firing Pulses or Spin Revolutions (2<sup>0</sup>) |  |  |
| 0 (LSB) | Thruster Firing Ratio D = 2<sup>3</sup> |  |  |

!!! note "Transcription note"
    Bit 7 is printed as 2<sup>10</sup>, followed directly by 2<sup>5</sup> in bit 6. Weights 2<sup>6</sup>–2<sup>9</sup> do not appear. The same layout is used for word 18 on sheet 2.

### Word 14

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster Firing Ratio C = 2<sup>2</sup> |  |  |
| 6 | Thruster Firing Ratio B = 2<sup>1</sup> |  |  |
| 5 | Thruster Firing Ratio A = 2<sup>0</sup> |  |  |
| 4 | Thruster Ratio Firing | Disabled | Enabled |
| 3 | Logic Power | Off | On |
| 2 | Maneuver Initiate/Terminate | Terminate | Initiate |
| 1 | Maneuver Complete | Incomplete | Complete |
| 0 (LSB) | +28 V On/Off | Off | On |

## Sheet 2 of 6

*Original page 8, Revision B, 4/20/77*

Words 15–19 repeat the layout of words 10–14 exactly. In [Appendix A](../appendix-a/index.md) they are "HPS Elec B CMD Status", where words 10–14 are HPS Elec A.

### Word 15

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster No. 1 Select | Not-Selected | Selected |
| 6 | Thruster No. 2 Select | Not-Selected | Selected |
| 5 | Thruster No. 3 Select | Not-Selected | Selected |
| 4 | Thruster No. 4 Select | Not-Selected | Selected |
| 3 | Thruster No. 5 Select | Not-Selected | Selected |
| 2 | Thruster No. 6 Select | Not-Selected | Selected |
| 1 | Thruster No. 7 Select | Not-Selected | Selected |
| 0 (LSB) | Thruster No. 8 Select | Not-Selected | Selected |

### Word 16

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster No. 11 Select | Not-Selected | Selected |
| 6 | Thruster No. 12 Select | Not-Selected | Selected |
| 5 | Thruster No. 9 Select | Not-Selected | Selected |
| 4 | Thruster No. 10 Select | Not-Selected | Selected |
| 3 | Sector Initiate (2<sup>9</sup>) |  |  |
| 2 | Sector Initiate (2<sup>8</sup>) |  |  |
| 1 | Sector Initiate (2<sup>7</sup>) |  |  |
| 0 (LSB) | Sector Initiate (2<sup>6</sup>) |  |  |

### Word 17

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Sector Initiate (2<sup>5</sup>) |  |  |
| 6 | Sector Initiate (2<sup>4</sup>) |  |  |
| 5 | Sector Initiate (2<sup>3</sup>) |  |  |
| 4 | Sector Initiate (2<sup>2</sup>) |  |  |
| 3 | Sector Initiate (2<sup>1</sup>) |  |  |
| 2 | Sector Initiate (2<sup>0</sup>) |  |  |
| 1 | Sector Width Select B |  |  |
| 0 (LSB) | Sector Width Select A |  |  |

### Word 18

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | No. Firing Pulses or Spin Revolutions (2<sup>10</sup>) |  |  |
| 6 | No. Firing Pulses or Spin Revolutions (2<sup>5</sup>) |  |  |
| 5 | No. Firing Pulses or Spin Revolutions (2<sup>4</sup>) |  |  |
| 4 | No. Firing Pulses or Spin Revolutions (2<sup>3</sup>) |  |  |
| 3 | No. Firing Pulses or Spin Revolutions (2<sup>2</sup>) |  |  |
| 2 | No. Firing Pulses or Spin Revolutions (2<sup>1</sup>) |  |  |
| 1 | No. Firing Pulses or Spin Revolutions (2<sup>0</sup>) |  |  |
| 0 (LSB) | Thruster Firing Ratio D = 2<sup>3</sup> |  |  |

### Word 19

Unit: AT

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Thruster Firing Ratio C = 2<sup>2</sup> |  |  |
| 6 | Thruster Firing Ratio B = 2<sup>1</sup> |  |  |
| 5 | Thruster Firing Ratio A = 2<sup>0</sup> |  |  |
| 4 | Thruster Ratio Firing | Disabled | Enabled |
| 3 | Logic Power | Off | On |
| 2 | Maneuver Initiate/Terminate | Terminate | Initiate |
| 1 | Maneuver Complete | Incomplete | Complete |
| 0 (LSB) | +28 V On/Off | Off | On |

## Sheet 3 of 6

*Original page 9, Revision A, 12/7/76*

### Words 20 & 52

Unit: CM

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Command Counter B (2<sup>7</sup>) |  |  |
| 6 | Command Counter B (2<sup>6</sup>) |  |  |
| 5 | Command Counter B (2<sup>5</sup>) |  |  |
| 4 | Command Counter B (2<sup>4</sup>) |  |  |
| 3 | Command Counter B (2<sup>3</sup>) |  |  |
| 2 | Command Counter B (2<sup>2</sup>) |  |  |
| 1 | Command Counter B (2<sup>1</sup>) |  |  |
| 0 (LSB) | Command Counter B (2<sup>0</sup>) |  |  |

### Words 21 & 53

Unit: CM

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Command Counter A (2<sup>7</sup>) |  |  |
| 6 | Command Counter A (2<sup>6</sup>) |  |  |
| 5 | Command Counter A (2<sup>5</sup>) |  |  |
| 4 | Command Counter A (2<sup>4</sup>) |  |  |
| 3 | Command Counter A (2<sup>3</sup>) |  |  |
| 2 | Command Counter A (2<sup>2</sup>) |  |  |
| 1 | Command Counter A (2<sup>1</sup>) |  |  |
| 0 (LSB) | Command Counter A (2<sup>0</sup>) |  |  |

### Word 22

Unit: CM-03

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Exp. Wire Antenna Motor | Off | On |
| 6 | Exp. Wire Antenna Mode | Retract | Deploy |
| 5 | +U Antenna | Disabled | Enabled |
| 4 | −U Antenna | Disabled | Enabled |
| 3 | +V Antenna | Disabled | Enabled |
| 2 | −V Antenna | Disabled | Enabled |
| 1 | +Z Antenna | Disabled | Enabled |
| 0 (LSB) | −Z Antenna | Disabled | Enabled |

## Sheet 4 of 6

*Original page 10, Revision A, 12/7/76*

### Word 23

Unit: CM-03

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | +U Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 6 | −U Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 5 | +V Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 4 | −V Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 3 | +Z Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 2 | −Z Antenna Limit Flag | Mid-length | Sto/Full Dep |
| 1 | Battery Present | Off | On |
| 0 (LSB) | (blank) |  |  |

The rest of this sheet is blank tables.

## Sheet 5 of 6

*Original page 11, Revision C, 9/8/77*

### Word 48

Unit: PW

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Battery Heater | Off | On |
| 6 | Main Bus UV Detector | On | Off |
| 5 | Main Bus OC Detector | Enable | Disable |
| 4 | Battery UV Detector | Enable | Disable |
| 3 | Auto Load Remove Output | Output | No Output |
| 2 | Auto Load Remove | Enable | Disable |
| 1 | Battery Status | Enable | Disable |
| 0 (LSB) | Boost Regulator | On | Off |

!!! note "Transcription note"
    Bit 5 is barely legible (it reads roughly "Dec?or"). It is transcribed as "Main Bus OC Detector" by analogy with bits 6 and 4.

### Word 49

Unit: SD

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | MGA Beam Control Converter | Off | On |
| 6 | Spare |  |  |
| 5 | Medium Gain Antenna Position (2<sup>1</sup>) |  |  |
| 4 | Medium Gain Antenna Position (2<sup>0</sup>) |  |  |
| 3 | Transponder B Modulation Index | M2 | M1 |
| 2 | Transponder B Antenna | IGA | MGA |
| 1 | Transponder B Ranging | Off | On |
| 0 (LSB) | Transponder B Digital | Off | On |

### Word 50

Unit: SD

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Transponder B Mode | Non-Coherent | Coherent |
| 6 | Transponder A Analog | Off | On |
| 5 | Transponder A Modulation Index | M2 | M1 |
| 4 | Transponder A Antenna | QFHA | MGA |
| 3 | Transponder A Ranging | Off | On |
| 2 | Transponder A Digital | Off | On |
| 1 | Transponder A Mode | Non-Coherent | Coherent |
| 0 (LSB) | Opposite DHU +7.75V | Off | On |

## Sheet 6 of 6

*Original page 12, Revision B, 4/20/77*

### Word 51

Unit: CM

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Accel. Pulse Counter (2<sup>7</sup>) |  |  |
| 6 | Accel. Pulse Counter (2<sup>6</sup>) |  |  |
| 5 | Accel. Pulse Counter (2<sup>5</sup>) |  |  |
| 4 | Accel. Pulse Counter (2<sup>4</sup>) |  |  |
| 3 | Accel. Pulse Counter (2<sup>3</sup>) |  |  |
| 2 | Accel. Pulse Counter (2<sup>2</sup>) |  |  |
| 1 | Accel. Pulse Counter (2<sup>1</sup>) |  |  |
| 0 (LSB) | Accel. Pulse Counter (2<sup>0</sup>) |  |  |

### Word 54

Unit: CM-03

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | HPS-A PRM TK HTRS | See note | See note |
| 6 | HPS-A SEC TK HTRS | See note | See note |
| 5 | HPS B PRM TK HTRS | See note | See note |
| 4 | HPS B SEC TK HTRS | See note | See note |
| 3 | HPS A/B PRM LN HTRS | See note | See note |
| 2 | HPS A/B SEC LN HTRS | See note | See note |
| 1 | (blank) |  |  |
| 0 (LSB) | (blank) |  |  |

### Word 55

Unit: CM-03

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | HPS-A PRM TK HTRS | See note | See note |
| 6 | HPS-A SEC TK HTRS | See note | See note |
| 5 | HPS B PRM TK HTRS | See note | See note |
| 4 | HPS B SEC TK HTRS | See note | See note |
| 3 | HPS A/B PRM LN HTRS | See note | See note |
| 2 | HPS A/B SEC LN HTRS | See note | See note |
| 1 | (blank) |  |  |
| 0 (LSB) | (blank) |  |  |

### Note: heater command truth table

Heater command states can be determined from the truth table below, for bit *i* of subcom words 54 and 55, where *i* = 7 thru 2.

| State | Word 54 bit *i* | Word 55 bit *i* |
|---|:-:|:-:|
| Off | 0 | 0 |
| HI | 1 | 1 |
| LO | 0 | 1 |
| MED | 1 | 0 |

!!! info "Unit ID differences"
    This section gives unit **CM** for word 51 and **CM-03** for words 54–55. [Appendix A](../appendix-a/index.md) lists all three as **AT**. [B-II](../appendix-b/b-ii.md) explains the difference: these words are AT telemetry that is "also listed in B-III as CM-03 outputs".
