import argparse

from imageai.Detection.Custom import CustomObjectDetection

def detection():
	detector = CustomObjectDetection()
	detector.setModelTypeAsYOLOv3()
	model_name = './model/'+parse.model_name
	detector.setModelPath(model_name)
	detector.setJsonPath("detection_config.json")
	detector.loadModel()
	input_file = './input_folder/'+parse.input_file
	output_file = './output_folder/'+parse.output_file
	detections = detector.detectObjectsFromImage(input_image=input_file, output_image_path=output_file, minimum_percentage_probability=parse.match_percentage)
	print(detections)

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str, help='input_file_name')
parser.add_argument('--output_file', type=str, help='output_file_name')
parser.add_argument('--model_name', default="detection_model-ex-024--loss-0025.553.h5",type=str, help='output_file_name')
parser.add_argument('--match_percentage', type=int,default = 50,help='percentage of match')

parse = parser.parse_args()
detection()