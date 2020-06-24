import csv
import xml.etree.cElementTree as ET

def csv_to_xml(csv_path, resized_images_path, labels_path, folder):
    f = open(csv_path, 'r')
    reader = csv.reader(f)
    header = next(reader)
    old_filename = None
    for row in reader:
        filename = row[0]
        if filename == old_filename:
            object = ET.SubElement(annotation, 'object')
            ET.SubElement(object, 'name').text = row[3]
            ET.SubElement(object, 'pose').text = 'Unspecified'
            ET.SubElement(object, 'truncated').text = '0'
            ET.SubElement(object, 'difficult').text = '0'
            bndbox = ET.SubElement(object, 'bndbox')
            ET.SubElement(bndbox, 'xmin').text = row[4]
            ET.SubElement(bndbox, 'ymin').text = row[5]
            ET.SubElement(bndbox, 'xmax').text = row[6]
            ET.SubElement(bndbox, 'ymax').text = row[7]
        else:
            if old_filename is not None:
                labels_file = old_filename.replace('.jpg', '.xml')
                tree = ET.ElementTree(annotation)
                tree.write(labels_path + labels_file)

            annotation = ET.Element('annotation')
            ET.SubElement(annotation, 'folder').text = folder
            ET.SubElement(annotation, 'filename').text = filename
            ET.SubElement(annotation, 'path').text =     resized_images_path + filename
            source = ET.SubElement(annotation, 'source')
            ET.SubElement(source, 'database').text = 'Unknown'
            size = ET.SubElement(annotation, 'size')
            ET.SubElement(size, 'width').text = row[1]
            ET.SubElement(size, 'height').text = row[2]
            ET.SubElement(size, 'depth').text = '3'
            ET.SubElement(annotation, 'segmented').text = '0'

            object = ET.SubElement(annotation, 'object')
            ET.SubElement(object, 'name').text = row[3]
            ET.SubElement(object, 'pose').text = 'Unspecified'
            ET.SubElement(object, 'truncated').text = '0'
            ET.SubElement(object, 'difficult').text = '0'
            bndbox = ET.SubElement(object, 'bndbox')
            ET.SubElement(bndbox, 'xmin').text = row[4]
            ET.SubElement(bndbox, 'ymin').text = row[5]
            ET.SubElement(bndbox, 'xmax').text = row[6]
            ET.SubElement(bndbox, 'ymax').text = row[7]
        old_filename = filename
    f.close()
	
csv_to_xml('all_labels.csv', '', '', 'new')