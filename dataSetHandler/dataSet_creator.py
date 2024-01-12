import os
import shutil


DATA_ALL_DIR = os.path.join('..', 'test001IMGS\\')
DATA_OUT_DIR = os.path.join('..', 'data\\')

if not(os.path.exists(DATA_OUT_DIR)):
    os.mkdir(DATA_OUT_DIR)

for set_ in ['train', 'validation', 'test']:
    for dir_ in [os.path.join(DATA_OUT_DIR, set_),
                 os.path.join(DATA_OUT_DIR, set_, 'images'),
                 os.path.join(DATA_OUT_DIR, set_, 'labels')]:
        if os.path.exists(dir_):
            shutil.rmtree(dir_)
        os.mkdir(dir_)


tempIDs = {'/m/01r546': 0, '/m/0k1tl': 1, '/m/024d2': 2, '/m/018xm': 3, '/m/01lsmm': 4} # -> earringsID, pen, calculator, ball, scissors
train_bboxes_filename = os.path.join('..', 'OData\\oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('..', 'OData\\validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('..', 'OData\\test-annotations-bbox.csv')


for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
    set_ = ['train', 'validation', 'test'][j]
    print(filename)
    with open(filename, 'r') as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
            for tempID in tempIDs:
                if class_name == tempID:
                    label = tempIDs[tempID]
                    if not os.path.exists(os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id))):
                        shutil.copy(os.path.join(DATA_ALL_DIR, '{}.jpg'.format(id)), os.path.join(DATA_OUT_DIR, set_, 'images', '{}.jpg'.format(id)))
                    with open(os.path.join(DATA_OUT_DIR, set_, 'labels', '{}.txt'.format(id)), 'a') as f_ann:
                        x1, x2, y1, y2 = [float(j) for j in [x1, x2, y1, y2]]
                        xc = (x1 + x2) / 2
                        yc = (y1 + y2) / 2
                        w = x2 - x1
                        h = y2 - y1
                        f_ann.write('{} {} {} {} {}\n'.format(label, xc, yc, w, h))
                        f_ann.close()
            line = f.readline()
