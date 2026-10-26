# VIII. Status Register ISEE-C Words 61, 62, 63 in Minor Frame

*Original page 6, Revision C, 9/8/77*

The status register occupies words 61, 62 and 63 of the minor frame when the fixed-word phase is 2 (word 60 LSBs = 10). See [Section VI](06-minor-frame-scientific.md#fixed-words). Bit 7 is the MSB and bit 0 the LSB.

## Word 61

Unit: TL, AT, SE

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | TL Parity | Correct | Wrong |
| 6 | Third Stage | Separated | Attached |
| 5 | HPS-A Latch Valve 1 Position | Closed | Open |
| 4 | HPS-B Latch Valve 2 Position | Closed | Open |
| 3 | HPS-A Latch Valve 3 Position | Closed | Open |
| 2 | HPS-B Latch Valve 4 Position | Closed | Open |
| 1 | Spare | | |
| 0 (LSB) | Third Stage Separation Switch Bypass | Disabled | Enabled |

## Word 62

Unit: SE, CM-03, SD

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Spare | | |
| 6 | Spare | | |
| 5 | +Y Inertia Boom | Folded | Deployed |
| 4 | −Y Inertia Boom | Folded | Deployed |
| 3 | Transponder A | Unlock | Lock |
| 2 | Transponder B | Unlock | Lock |
| 1 | +X Boom | Folded | Deployed |
| 0 (LSB) | −X Boom | Folded | Deployed |

!!! note "Appendix B differs"
    [B-III](../appendix-b/b-iii.md) and [B-VI](../appendix-b/b-vi.md) assign word 62 bits 7 and 6 to **Timer A** and **Timer B** (CM-03, 0/1 = Disabled/Enabled), where this page shows them as spare. Appendix B also gives the units of bits 5, 4, 1 and 0 as CM-03.

## Word 63

Unit: CM-01

| Bit | Function | 0 = | 1 = |
|:-:|---|---|---|
| 7 (MSB) | Command Drivers A | Disable | Enable |
| 6 | Command Drivers B | Disable | Enable |
| 5 | Data Present Decoder A | No | Yes |
| 4 | Data Present Decoder B | No | Yes |
| 3 | Parity Decoder A | OK | False |
| 2 | Parity Decoder B | OK | False |
| 1 | Address Decoder A | OK | False |
| 0 (LSB) | Address Decoder B | OK | False |
