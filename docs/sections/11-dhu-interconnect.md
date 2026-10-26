# XI. DHU Simplified Interconnect Diagram

*Original page 15, Revision A, 12/7/76*

![Section XI: DHU Simplified Interconnect Diagram](../images/sec11-dhu-interconnect.png)

The diagram shows how the Data Handling Unit (DHU) is wired:

- **Dataplexer (P1, P2, P5, P6).** Its analog gates AG<sub>0,2,4…30</sub>, analog inputs AI<sub>0</sub>–AI<sub>15</sub> and AI<sub>16</sub>–AI<sub>31</sub>, digital inputs DI<sub>0</sub>–DI<sub>15</sub> and DI<sub>16</sub>–DI<sub>31</sub>, digital gates DG<sub>0</sub>–DG<sub>15</sub> and DG<sub>16</sub>–DG<sub>31</sub>, digital shifts DS<sub>0</sub>–DS<sub>15</sub> and DS<sub>16</sub>–DS<sub>31</sub>, and status bits SB2–SB23 (into REG).
- **Analog subplexer.** Driven by AG<sub>0</sub>/AI<sub>0</sub> for ASI 1-0 to ASI 1-63 (connector P6) and by AG<sub>16</sub>/AI<sub>8</sub> for ASI 2-0 to ASI 2-63 (connector P7). Each half includes thermistor (THMS) inputs.
- **Digital subplexer.** Fed by DI<sub>0</sub>, with a REG, a ROM, subplexer status bits SSB 1–SSB 16 (P6), digital subplexer inputs DSI 0–DSI 31 (P6), and digital subplexer gate/shift outputs DSG 0–DSG 31 and DSS 0–DSS 31 (P7).

The abbreviations are defined in the [Glossary](15-glossary.md).
