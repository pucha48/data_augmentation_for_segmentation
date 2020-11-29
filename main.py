import argparse
import os
import sys
from augmentation import Augmentation

# Create the parser
parser = argparse.ArgumentParser(description="List the content of the folder")
#Adding arguments
parser.add_argument('--image_dir',metavar='path',type=str,help='the path to list')
parser.add_argument('--rotation',action='store',type=int)
parser.add_argument('--label_file',action='store',type=str)
parser.add_argument('--label_dir' ,action='store',type=str)

#Execute parse_args()
args = parser.parse_args()
image_dir = args.image_dir
label_file = args.label_file
label_dir = args.label_dir
rotation = args.rotation

if not os.path.isdir(image_dir):
    print('The path specified does not exist')
    sys.exit()

augment_object = Augmentation()
image_lst,label_lst = augment_object.load_data(image_dir,label_dir)
root = 'sample_images/'
for file in label_lst:
    image_path = os.path.join(image_dir,os.path.splitext(file)[0] + '.jpg')
    label_path = os.path.join(label_dir,file)
    points = augment_object.operate_single(image_path,label_path)
    augment_object.save_files(points,os.path.join(label_dir,file),image_path)
    # print("modified Points" , augment_object.operate_single(image_path,label_path))











