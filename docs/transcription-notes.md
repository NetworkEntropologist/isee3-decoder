# Transcription notes

## Source

The source is a scanned PDF of ISEE Notebook 18g-2 (86 pages). It is Fairchild document 905-TL-3006-01, Revision C, 8 September 1977. Most of the tables in the original are printed rotated 90°. The PDF's embedded OCR layer is unusable, so everything here was transcribed visually from the page images.

## Conventions

- **Spelling and typos are kept as printed.** Suspected errors are listed below, or flagged in a note on the page where they occur. They are not silently corrected.
- **Down-arrows** in the original carry a value (minor frame word, unit ID, analog/digital) across several rows. On this site the value is written out on every row.
- **Brackets** in the Remarks column group several rows under one remark. On this site the remark is repeated on every row it covers.
- **Diagrams** (Sections IV, VI, VII, X, XI, XII, XIII and XIV) are reproduced as page images, rotated upright and cropped. Each one has a short text summary. Where a diagram's content is fully tabulated elsewhere, the page links to that table.
- **Revision and date** of each original page are given in italics under each heading.
- **Cross-references** in the original ("See VIII of Text", "See IX of Text", "See page 14 of text", "See Appendix A, word 58", "See B-XVII, App B") are turned into links.
- **Ditto marks** in Appendix B's Analog Range column are kept as ″. Ditto marks standing in for a whole descriptor are written out, with a note on the page.

## Section IX

- Word 13 (and word 18): bit 7 is weighted 2<sup>10</sup>, then bits 6–0 run 2<sup>5</sup>…2<sup>0</sup>. Weights 2<sup>6</sup>–2<sup>9</sup> are missing as printed.
- Word 48, bit 5 is barely legible. It is read as "Main Bus OC Detector".
- Words 51, 54 and 55 have unit CM / CM-03 here but AT in Appendix A. [B-II](appendix-b/b-ii.md) explains both: AT telemetry, also listed as CM-03 outputs.

## Glossary

- Typos kept as printed: "Panaramic", "Radio Frequence", "Scintalator", "DeFeiter", "High Energy Telescope Telescope".
- P, PC, UH, UL and UW have no definition.
- The glossary defines AM as "Amplitude", but AM is also the unit ID of the Attitude Measurement subsystem ([B-I](appendix-b/b-i.md)).
- TEH (Teegarden, [B-XIX](appendix-b/b-xix.md)) is not in the glossary. UW, UH and UL appear in [B-XII](appendix-b/b-xii.md).

## Appendix A

See the notes at the end of [Appendix A](appendix-a/index.md#transcription-notes).

## Appendix B

Each Appendix B page has its own notes. The main ones:

- **B-II / B-XIX**: 122/39 and 122/40 are supercommutated 32 times. In both, the Bit column gives the slot number.
- **B-III / B-VI**: status register word 62, bits 7 and 6, are Timer A and Timer B. Section VIII shows them as spare.
- **B-XX**: one row is printed with minor frame word 56 instead of 59 (59/46). 122/19 is printed "HETS Temp", where Appendix A has VLETS Temp.
- **Section titles** spell three investigators differently from the glossary: "Hovestat" (Hovestadt), "Ogilive" (Ogilvie) and "Scarf" (Scharf).

## Appendix C

- Word 57: the descriptor reads "ASI 2 AS 2", which looks like a later annotation.
- Word 59 is DSI but is marked A. Every other DSI word is D.
- Word 82 (Indirect No. 1) is marked A. The other Indirect words have no A/D entry.
- Words 88 and 96 (Accel Output) have no A/D entry. All the other Accel Output words are A.
- Page C-3 (words 46–68) is Rev. C, 9/8/77. The other pages are Rev. A, 12/7/76.
