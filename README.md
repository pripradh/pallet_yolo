DETECT PALLETS IN NEW IMAGE
----------------------------------------------------
clone or download repo https://github.com/sai544042/pallet.git<br/>
cd dectect<br/>
If pretrained model exists place model in model folder else download it from https://drive.google.com/file/d/1-YC3uNKbYsvH6O7A1UuX1RMoZV_xHKF4/view?usp=sharing<br/>
run command<br/>
python detect.py --input_file  <file_name>  --output_file  <file_name>  --model_name <model_name> --match_percentage <number><br/>
model_name is optional it has a default model downloaded from https://drive.google.com/file/d/1-YC3uNKbYsvH6O7A1UuX1RMoZV_xHKF4/view?usp=sharing<br/>
match_percentage is optional it has by default of 50%<br/>


---------------------------------------------------------------------------------------------------------------------------------------------------------------
TRAINING A MODEL
________________________________________________________________________
CREATE A DIRECTECTORY STRUCTURE<br/>
pallet-train-images and annotations<br/>

____________________________________________________________________________________________________________________________________________________________________

requirements:-<br/>
_________________________

pip install tensorflow-gpu==1.15.0<br/>
pip install labelImg<br/>
pip install imageai<br/>

