## IVAO Colour Scheme Converter. 

This program converts .clr files used by the windows version of Aurora to a prefrences.json file used by macOS versions of Aurora. 

**This has been designed with the default IVAO XU colour schemes and config guidance in mind so may not work with other division or custom colour schemes but is not associated in any shape or form with the division or IVAO itself!**

## Usage

Ensure you have python version `3` installed. 

Download the `convert.py` and `template.json` file from this repo. A custom `template.json` could be made for your personal needs as the code will only replace the `palette` field. It is currently configured to match as closely to the guidance by the XU divsion here:

https://wiki.ivao.aero/en/home/divisions/xu/getting-started

Download / Find your .clr file and place it in the same directory as convert.py and template.json.

Run `python3 convert.py <name of input file>.clr <name of output file>.json`

The code will then convert the .clr file to a preferences.json based on the template.json file. 

You can then place your .json file in `~/.config/IVAO/Aurora/Settings/Profiles`. This will then appear in the profiles tab in Aurora macOS.


