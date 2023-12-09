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

## Screenshots

![EGLF](https://github.com/isaacbarker/ivaomacoscolours/assets/88422596/b5c3e666-9a8c-4952-9b09-c8f2ac9aa9d6)
![IFACTS](https://github.com/isaacbarker/ivaomacoscolours/assets/88422596/34107482-585d-469d-917e-b761f39e2ca0)
![NOVA9000](https://github.com/isaacbarker/ivaomacoscolours/assets/88422596/ccff190c-eeb8-4b27-a542-0f52d84525d1)
![NODES](https://github.com/isaacbarker/ivaomacoscolours/assets/88422596/383993ec-2785-47ab-bd7f-a11cfc3cff7c)