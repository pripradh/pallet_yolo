from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="pallet")
trainer.setTrainConfig(object_names_array=["pallet"], batch_size=10, num_experiments=150, train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()
