# V. ISEE-C Telemetry Timing Table

*Original page 3*

| Bit Rate Time (sec) | Major Frame | Minor Frame | Analog Subcoms (word) | Digital Subcom (word) | Fixed Words |
|---|:-:|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0.5 | ↓ | 1 | 1 | 1 | 1 |
| 1.0 | ↓ | 2 | 2 | 2 | 2 |
| 1.5 | ↓ | 3 | 3 | 3 | 3 |
| 2.0 | ↓ | 4 | 4 | 4 | 0 |
| 2.5 | ↓ | 5 | 5 | 5 | 1 |
| ⋮ | ↓ | ⋮ | ⋮ | ⋮ | ⋮ |
| 30.5 | ↓ | 61 | 61 | 61 | 1 |
| 31.0 | ↓ | 62 | 62 | 62 | 2 |
| 31.5 | ↓ | 63 | 63 | 63 | 3 |
| 32.0 | ↓ | 64 | 0 | 0 | 0 |
| | ↓ | 65 | 1 | 1 | 1 |
| | ↓ | ⋮ | ⋮ | ⋮ | ⋮ |
| | ↓ | 125 | 61 | 61 | 1 |
| | ↓ | 126 | 62 | 62 | 2 |
| | ↓ | 127 | 63 | 63 | 3 |
| 64.0 | ↓ | 128 | 0 | 0 | 0 |
| | ↓ | 129 | 1 | 1 | 1 |
| | ↓ | ⋮ | ⋮ | ⋮ | ⋮ |
| | ↓ | 189 | 61 | 61 | 1 |
| | ↓ | 190 | 62 | 62 | 2 |
| | ↓ | 191 | 63 | 63 | 3 |
| 96.0 | ↓ | 192 | 0 | 0 | 0 |
| | ↓ | 193 | 1 | 1 | 1 |
| | ↓ | ⋮ | ⋮ | ⋮ | ⋮ |
| | ↓ | 253 | 61 | 61 | 1 |
| | ↓ | 254 | 62 | 62 | 2 |
| | ↓ | 255 | 63 | 63 | 3 |
| 128.0 | 1 | 0 | 0 | 0 | 0 |

!!! info "Summary"
    - One minor frame takes 0.5 s, so a major frame of 256 minor frames takes 128 s.
    - Analog and digital subcom step = minor frame mod 64. Each subcom cycle repeats four times per major frame.
    - Fixed-word step = minor frame mod 4.
    - The telemetry content of a minor frame therefore depends only on its minor frame number mod 64. See [Appendix A by sub-frame position](../appendix-a/by-subframe.md).
