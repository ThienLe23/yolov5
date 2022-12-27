import glob
import os
import numpy as np
import shutil

dataset_folder = "..\\yolo_plate_dataset"

images_path = glob.glob(dataset_folder + "/*.jpg")

# Split train and val dataset
val_ratio = 0.2
data_num = len(images_path)
random_idx = np.random.permutation(data_num)
print("random_idx:", random_idx)
val_num = int(val_ratio*data_num)
val_idx = random_idx[:val_num]
train_idx = random_idx[val_num:]
data = {"train": train_idx, "val": val_idx}
# Copy images and labels to train and val folder

for folder in ["train", "val"]:
    folder_path = dataset_folder + "\\" + folder
    image_folder = folder_path + "\\" + "images"
    label_folder = folder_path + "\\" + "labels"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.mkdir(image_folder)
        os.mkdir(label_folder)
    for idx in data[folder]:
        image_path = images_path[idx]
        label_path = image_path[:-3] + "txt"
        new_image_path = image_folder + "\\" + image_path.split("\\")[-1]
        new_label_path = label_folder + "\\" + label_path.split("\\")[-1]
        print(image_path, new_image_path)
        print(label_path, new_label_path)
        shutil.move(image_path, new_image_path)
        shutil.move(label_path, new_label_path)

