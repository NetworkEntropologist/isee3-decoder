[![Python 3.10.19](https://img.shields.io/badge/python-3.10.19-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-31019/)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/thenetworkentropologist)

# ISEE-3 Decoder

A repo to cover my attempts at decoding and extracting useful data from telemetry frames for the ISEE-3/ICE-3 reboot project.

## Background
I'm not going to go into a lot of detail on the background of the ISEE-3 (International Sun-Earth Explorer-3) aka ICE-3 (International Cometary Explorer) satellite and mission, as there is already a lot of information available on this from a large number of sources online. You can start at [Wikipedia](https://en.wikipedia.org/wiki/International_Cometary_Explorer) if you want to read more about this fascinating spacecraft and mission.

In 2014, this spacecraft passed in-between the Earth and Moon, and became the subject of a crowd-funded *reboot* project, which also made it one of the first NASA spacecraft to taken control of by a civilian group. Once again I am not going to go into a lot of detail on this project, as this has already been covered in detail by several other people, including an absolutely awesome [YouTube video](https://youtu.be/sdcksgSng0c) by [Alexander the OK](https://www.youtube.com/@Alexander-the-ok), aka [lambdaBoost](https://github.com/lambdaBoost) on GitHub. In fact, I can quite confidently say that Alex's video on this topic is what inspired me to go down this rabbit hole in the first place.

## Information Sources
Despite the fact that NASA has gotten rid of a lot of the documentation pertaining to this mission (the mission was over, the documentation was almost entirely on paper, and there was no real, compelling reason to keep it around), there is still a surprising amount of information available online. I will attempt to list as many of these here as I can.

* [NASA documentation archive](https://voyager.gsfc.nasa.gov/Library/ISEE_library.html): NASA still have a number of documents in archive and most importantly for this project, these include the documentation on the telemetry formats and lists.
* [KA9Q's Decoding work](https://www.ka9q.net/isee.html): Phil Karn, aka KA9Q has done a lot of work in terms of decoding the raw bitstream received by the reboot team.
* [Official NASA page on this project](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=1978-079A)
* [Spench's telemetry archive](https://spench.net/~balint/public/isee-3/): This archive contains, as far as I can determine, the full set of decoded telemetry frames as recorded by the reboot team.

## Goals
Goals for this project are:

1. Read in raw telemetry dump files and break these into individual frames. ✅
2. Extract FRC (Frame Sequence Counter). ✅
3. Map out full frame word layout for engineering frames. 🚧
4. Extract engineering data in human readable format. ❌
5. Pump engineering data into Prometheus. ❌
6. Map out full frame word layout for science frames. 🚧
7. Extract science data in human readable format. ❌
8. Pump engineering data into Prometheus. ❌
9. Build pretty Grafana dashboards. ❌

## Updates
This is purely a passion project. As such I will be working on this as/when I have time and spoons to work on this. This means that updates here will not happen at any set interval, so if you want to hear more about this project and the progress, you are welcome to Watch this repo. I might add a website for this project at a later date, but this is not a done deal just yet.
