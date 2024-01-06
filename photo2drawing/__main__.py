import argparse

from photo2drawing.draw import photo_to_draw
from photo2drawing.sketch import convert_to_sketch

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument('-o', '--output', help='Output Filename', required=True)
parser.add_argument('-i', '--input', help='Input Filename', required=True)
parser.add_argument(
    '-d', '--draw', action='store_true', help='Uses draw method'
)
parser.add_argument('-s', '--show', action='store_true', help='Show images')
parser.add_argument(
    '-b', '--bright', default='1.0', help='Image brightness default=1.0'
)


# Read arguments from command line
args = parser.parse_args()

if args.draw:
    photo_to_draw(args.input, args.output, float(args.bright), args.show)
else:
    convert_to_sketch(args.input, args.output, args.show)
