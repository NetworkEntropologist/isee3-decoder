# X. ISEE-C Minor Telemetry Frame Engineering Format

## Sheet 1 of 2

*Original page 13, Revision C, 9/8/77*

![Section X: Minor Telemetry Frame Engineering Format, sheet 1](../images/sec10-minor-frame-engineering.png)

In the engineering format, the minor frame is mostly filled with the accelerometer output (AT ACC, every 8th word), the analog and digital subcoms, and the two indirect addresses I<sub>1</sub> and I<sub>2</sub>. The word-by-word assignment is in [Appendix C](../appendix-c/index.md).

Legend from the diagram:

| Label | Meaning |
|---|---|
| ASI 1 | Analog Subcom (ASI) 1 (see [page 5](07-subcom-formats.md)) |
| DSI | Digital Subcom (DSI) (see [page 5](07-subcom-formats.md)) |
| ASI 2 | Analog Subcom (ASI) 2 (see [page 5](07-subcom-formats.md)) |
| I<sub>1</sub>, I<sub>2</sub> | Indirect Address No. 1 & No. 2 (see [page 14](#sheet-2-of-2)) |

The fixed words (60 = Frame Counter, 61–63) follow the same rule as the scientific format. See [Section VI](06-minor-frame-scientific.md#fixed-words).

## Sheet 2 of 2

*Original page 14, Revision A, 12/7/76*

Indirect Address No. 1 (I<sub>1</sub>) and No. 2 (I<sub>2</sub>) independently select any of these 16 parameters.

| Address | Unit | Measurement |
|---|---|---|
| AI<sub>16</sub> | SCH | 16 Chan f<sub>16</sub> (100 KHz) Data |
| AI<sub>17</sub> | SCH | 16 Chan f<sub>15</sub> (56 KHz) Data |
| AI<sub>18</sub> | SCH | 16 Chan f<sub>14</sub> (31 KHz) Data |
| AI<sub>19</sub> | SCH | 16 Chan f<sub>13</sub> (17 KHz) Data |
| AI<sub>20</sub> | SCH | 16 Chan f<sub>12</sub> (10 KHz) Data |
| AI<sub>21</sub> | SD | Static Phase A |
| AI<sub>22</sub> | SD | Static Phase B |
| AI<sub>23</sub> | AT | Accelerometer Output |
| AI<sub>24</sub> | SMH | X-Axis Magnetic Field Data |
| AI<sub>25</sub> | SMH | Y-Axis Magnetic Field Data |
| AI<sub>26</sub> | SMH | Z-Axis Magnetic Field Data |
| AI<sub>27</sub> | PW | Non-Essential Bus Current |
| AI<sub>28</sub> | PW | Main Bus Voltage |
| AI<sub>29</sub> | PW | Essential Bus Current |
| AI<sub>30</sub> | PW | Solar Array Current |
| AI<sub>31</sub> | TL | Remainder |
