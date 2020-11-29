import argparse
import os
import sys
from rotation import rotation

# Create the parser
parser = argparse.ArgumentParser(description="List the content of the folder")
#Adding arguments
parser.add_argument('--image_dir',metavar='path',type=str,help='the path to list')
parser.add_argument('--rotation',action='store',type=int)
#Execute parse_args()
args = parser.parse_args()
input_path = args.image_dir
rotation = args.rotation

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()



