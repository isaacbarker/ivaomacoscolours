import sys
import json

# VCL colour data courtesy of: https://docwiki.embarcadero.com/RADStudio/Alexandria/en/Colors_in_the_VCL.
color_data = {
  "clBlack": "$000000",
  "clMaroon": "$000080",
  "clGreen": "$008000",
  "clOlive": "$008080",
  "clNavy": "$800000",
  "clPurple": "$800080",
  "clTeal": "$808000",
  "clGray": "$808080",
  "clSilver": "$C0C0C0",
  "clRed": "$0000FF",
  "clLime": "$00FF00",
  "clYellow": "$00FFFF",
  "clBlue": "$FF0000",
  "clFuchsia": "$FF00FF",
  "clAqua": "$FFFF00",
  "clWhite": "$FFFFFF",
  "clMoneyGreen": "$C0DCC0",
  "clSkyBlue": "$F0CAA6",
  "clCream": "$F0FBFF",
  "clMedGray": "$A4A0A0",
  "clNone": "$1FFFFFFF",
}

# Converts .clr colour convention from windows to hex codes recognisable by Aurora macos
def hex_convert(input_str):

  # See if value if in colour_data or drop value if not currently compatible with macos configs e.g. VOR_SYMBOL
  if input_str in color_data.keys():
    hex_code_str = color_data[input_str]
  elif input_str.startswith('$'):
    hex_code_str = input_str
  else:
    return None

  # Remove the dollar sign if present
  if hex_code_str.startswith('$'):
      hex_code_str = hex_code_str[1:]

  # Remove alpha indicator
  if len(hex_code_str) == 8:
    hex_code_str = hex_code_str[2:]

  # Format colour code to hex
  hex_units = [hex_code_str[i:i+2] for i in range(0, len(hex_code_str), 2)]
  hex_units.reverse()

  hex_code_str = ''.join(hex_units)

  # Convert the string to an integer and then format it as a hex string
  return '#' + format(int(hex_code_str, 16), '06X')

# Get input file from command line arguments
input_file = None
output_file = None

if len(sys.argv) > 2:
  input_file = sys.argv[1]
  output_file = sys.argv[2]
else:
  print('An error occured please include an input & output file when running this application. e.g python3 convert.py <insert input file path here> <output path here>')

# Read input file and convert to dict
colours = {}

with open(input_file, 'r') as file:
  
  for line in file:
    vals = line.split('=')

    # Convert colour value to hex code
    hex_str = hex_convert(vals[1].strip())
    
    # Drop invalid configs
    if hex_str != None:
      colours[vals[0]] = hex_str

# Convert colours to json to be exported as a profile.json
with open('template.json', 'r') as file:
  data = json.load(file)
  data['palette'] = colours

with open(output_file, 'w') as file:
  json.dump(data, file, indent=4)
