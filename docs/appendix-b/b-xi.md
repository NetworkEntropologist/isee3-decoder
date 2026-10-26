# B-XI. Heckman (HKH) Telemetry List

## Page B-16 (Sheet 1 of 2)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 31 | - | - | HKH | Cosmic Ray Event Data | D |  | 256 bits commutated. 16 consecutive minor frames contain 256 bits corresponding to one cosmic ray event. |
| 32 | - | - | HKH | Cosmic Ray Event Data | D |  | 256 bits commutated. 16 consecutive minor frames contain 256 bits corresponding to one cosmic ray event. |
| 58 | 21 | - | HKH | Drift Chamb Temp | A |  |  |
| 58 | 22 | - | HKH | Silicon Det Temp | A |  |  |
| 58 | 32 | - | HKH | Pwr Mon | A | > 0.5V if LV Pwr ON, and > 2.5V if Gas Valves ENABLED |  |
| 58 | 33 | - | HKH | Exp Status | A |  | 16 parameters commutated:<br>1. 8192 Hz S/C Clock<br>2. Si/Li Det No. 1<br>3. Si/Li Det No. 2<br>4. Si/Li Det No. 3<br>5. Si/Li Det No. 4<br>6. Si/Li Det No. 5<br>7. Si/Li Det No. 6<br>8. Si/Li Det No. 7<br>9. Si/Li Det No. 8<br>10. Si/Li Det No. 9<br>11. Si/Li Det No. 10<br>12. Plastic Scint.<br>13. Drift Chamb No. 6<br>14. Drift Chamb No. 5<br>15. Drift Chamb No. 2<br>16. Drift Chamb No. 1 |
| 58 | 34 | - | HKH | Hskg Data | A |  | 4 parameters commutated:<br>1. Si/Li HV Sup Mon<br>2. PMT HV Sup Mon<br>3. Drift Chamb HV Sup Mon<br>4. Dig. Sys. 1 LV Mon |

## Page B-17 (Sheet 2 of 2)

*Rev. A, 12/7/76*

| Minor Frame Word | Subcom Word | Bit | Unit ID | Telemetry Descriptor | Analog or Digital | Analog Range or Digital States | Remarks |
|---:|---:|---|---|---|:-:|---|---|
| 58 | 35 | - | HKH | Hskg Data | A | > 2.5 V = Enabled | 4 Parameters Commutated:<br>1. Dig Sys 2 LV Mon<br>2. Gas Sys Intermed Press<br>3. Drift Chamb Press<br>4. Gas Sys Rsvr Press |

