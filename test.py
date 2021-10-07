import cv2
import numpy as np
import time
import argparse

#Get Parameter
#ex) python3 ./test.py -i ./testImg.jpg -m ./mymodel.tflite
parser = argparse.ArgumentParser()
parser.add_argument(
	'-i',
	'--image',
	default='./testImg.jpg',
	help='image to be classified')
parser.add_argument(
	'-m',
	'--model_file',
	default='./mymodel.tflite',
	help='.tflite model to be executed')
args = parser.parse_args()

#Model input size
width = 150
height = 150

#Expected Accuracy
acc = 0.9

#Load Tensorflow Lite
import tflite_runtime.interpreter as tflite
interpreter = tflite.Interpreter(model_path=args.model_file)
interpreter.allocate_tensors()
inputdets = interpreter.get_input_details()
outputdets = interpreter.get_output_details()

print("<br>")

#Read image
img = cv2.imread(args.image)

#Crop Ratio
sli_width = int(img.shape[0] / width);
sli_height = int(img.shape[1] / height);

#SetGray
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Resize Image
resize_Img = cv2.resize(img,(width * sli_width,height * sli_height))
print(resize_Img.shape)
#Initialize time
start_time = time.time()

#Loop -> sli_width * sli_height
for i in range(1, sli_width + 1):
    for j in range(1, sli_height + 1):
        
        #Get X location
        x1 = (j - 1) * width
        x2 = j * width
        
        #Get Y location
        y1 = (i - 1) * width
        y2 = i * width

        #Set input data
        input_img = resize_Img[x1 : x2 , y1 : y2].copy()
        print(input_img.shape)
        input_data = np.array([input_img/255],dtype=np.float32)
        #input_data = np.delete(input_data,0, axis=0)
        #If gray : Set this option
        input_data = input_data[...,np.newaxis]
        
        #Use for debug
        print(input_data.shape)
        
        #Get Result
        interpreter.set_tensor(inputdets[0]['index'], input_data)
        interpreter.invoke()
        result = interpreter.get_tensor(outputdets[0]['index'])
        
        #Compare result and expected accuracy
        print("Result : " + str(result) + "<br>")
        if(result > acc):
            print("( " + str(i) + " ," + str(j) + ") is Crack<br>")
        else:
            print("( " + str(i) + " ," + str(j) + ") is not  Crack<br>")

#Get time
stop_time = time.time()
print('time: {:.3f}ms'.format((stop_time - start_time) * 1000) +"<br>")
