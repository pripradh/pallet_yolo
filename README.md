DETECT PALLETS IN NEW IMAGE
----------------------------------------------------
clone or download repo https://github.com/sai544042/pallet.git
cd dectect
If pretrained model exists place model in model folder else download it from https://drive.google.com/file/d/1-YC3uNKbYsvH6O7A1UuX1RMoZV_xHKF4/view?usp=sharing
run command
python detect.py --input_file <filename> --output_file <filename> --model_name <model_name> --match_percentage <number>
model_name is optional it has a default model downloaded from https://drive.google.com/file/d/1-YC3uNKbYsvH6O7A1UuX1RMoZV_xHKF4/view?usp=sharing
match_percentage is optional it has by default of 50%
