import os

tempIDs = ['/m/01r546', '/m/0k1tl', '/m/024d2', '/m/018xm', '/m/01lsmm'] # -> earrings, pen, calculator, ball, scissors

train_bboxes_filename = os.path.join('..', 'OData\\oidv6-train-annotations-bbox.csv')
validation_bboxes_filename = os.path.join('..', 'OData\\validation-annotations-bbox.csv')
test_bboxes_filename = os.path.join('..', 'OData\\test-annotations-bbox.csv')
image_list_file_path = os.path.join('..', 'listOfImages')


def create_image_file(tempIDs):
    image_list_file_list = []
    for j, filename in enumerate([train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]):
        print(filename)
        with open(filename, 'r') as f:
            line = f.readline()
            while len(line) != 0:
                id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(',')[:13]
                for tempID in tempIDs:
                    if (class_name in [tempID]) and (id not in [image_list_file_list]):
                        image_list_file_list.append(id)
                        with open(image_list_file_path, 'a') as fw:
                            fw.write('{}/{}\n'.format(['train', 'validation', 'test'][j], id))
                line = f.readline()
            f.close()


create_image_file(tempIDs)
