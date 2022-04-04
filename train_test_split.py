import os
import random
import shutil
import argparse

# Argument Parsing
parser = argparse.ArgumentParser(description='A python script that splits the labeled data into train/test data in Yolov5 format')
parser.add_argument('-name', help='Name of custom dataset directory', default='custom_dataset')
parser.add_argument('-testsize', help='Test split size. Expects floating point number. Default test split size is 0.2', default=0.2)
parser.add_argument('-images', help='Path to images directory', default='images')
parser.add_argument('-labels', help='Path to bounding box txt files directory', default='bbox_txt')
args = vars(parser.parse_args())

img_list = os.listdir(args['images'])

# Shuffling images
random.shuffle(img_list)

split = args['testsize']
print('# Test split size:', split)

# Creating split directory
train_images_path = os.path.join(args['name'], 'train', 'images')
train_labels_path = os.path.join(args['name'], 'train', 'labels')
val_images_path = os.path.join(args['name'], 'val', 'images')
val_labels_path = os.path.join(args['name'], 'val', 'labels')
os.makedirs(train_images_path, exist_ok = True)
os.makedirs(train_labels_path, exist_ok = True)
os.makedirs(val_images_path, exist_ok = True)
os.makedirs(val_labels_path, exist_ok = True)

img_len = len(img_list)
print("# Images in total: ", img_len)

train_images = img_list[: int(img_len - (img_len*split))]
val_images = img_list[int(img_len - (img_len*split)):]
print("# Training images: ", len(train_images))
print("# Validation images: ", len(val_images))

for img_name in train_images:
    base_name, ext = os.path.splitext(img_name)

    # Copy image
    og_path = os.path.join(args['images'], img_name)
    target_path = os.path.join(train_images_path, img_name)
    shutil.copyfile(og_path, target_path)

    # Copy bounding box txt file
    og_txt_path = os.path.join(args['labels'], base_name + '.txt')
    target_txt_path = os.path.join(train_labels_path, base_name + '.txt')
    shutil.copyfile(og_txt_path, target_txt_path)

for img_name in val_images:
    base_name, ext = os.path.splitext(img_name)

    # Copy image
    og_path = os.path.join(args['images'], img_name)
    target_path = os.path.join(val_images_path, img_name)
    shutil.copyfile(og_path, target_path)

    # Copy bounding box txt file
    og_txt_path = os.path.join(args['labels'], base_name + '.txt')
    target_txt_path = os.path.join(val_labels_path, base_name + '.txt')
    shutil.copyfile(og_txt_path, target_txt_path)

print("# Done!")
