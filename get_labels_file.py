import glob
import os
import shutil

# gán địa chỉ của file để load
# train_image_file_path = "images_train"
# train_image_labels_path = "data_new/labels_train"

labels_path_train = "labels/train/"
labels_path_valid = "labels/val/"

images_path_train = "images/train/"
images_path_valid = "images/val/"


# Hàm để lấy địa chỉ
def load_data_training(directory):
    list_data = glob.glob(directory + "/*")
    return list_data


def get_file_name(path):
    return path.split("\\")[-1].split('.')[0]


labels_data_train = load_data_training(labels_path_train)
labels_data_val = load_data_training(labels_path_valid)
print(len(labels_data_train))
print(len(labels_data_val))

failcheck_1 = []
failcheck_2 = []


# for i in labels_data_train:
#     f = open(i, "r").read()
#     if len(f.split(" ")) > 9:
#         failcheck_1.append(i)
#         print("FAILED : " + i)
#
# print("******************************************************************************")


def get_bounding_scale(path):
    f = open(path, "r")
    labels, x1, y1, x2, y2, x3, y3, x4, y4 = f.read().split()
    minX = float(min([x1, x2, x3, x4]))
    minY = float(min([y1, y2, y3, y4]))
    maxX = float(max([x1, x2, x3, x4]))
    maxY = float(max([y1, y2, y3, y4]))
    return (minX, minY, maxX, maxY)


targets_train = []
targets_val = []
for j in labels_data_train:
    try:
        targets_train.append(get_bounding_scale(j))
    except:
        failcheck_1.append(j)
        print("FAILED: " + j)
print("******************************************************************************")
for j in labels_data_val:
    try:
        targets_val.append(get_bounding_scale(j))
    except:
        failcheck_2.append(j)
        print("FAILED: " + j)
print("******************************************************************************")
print(len(failcheck_1))
print(len(failcheck_2))
fail_data_train = []
fail_data_valid = []

for i in failcheck_1:
    fail_data_train.append(get_file_name(i))
    os.remove(i)
for i in failcheck_2:
    fail_data_valid.append(get_file_name(i))
    os.remove(i)

print(fail_data_train)
print(fail_data_valid)
print("******************************************************************************")
for i in fail_data_train:
    path = images_path_train + i + ".png"
    os.remove(path)
    print(path)
print("******************************************************************************")
for i in fail_data_valid:
    path = images_path_valid + i + ".png"
    os.remove(path)
    print(path)
