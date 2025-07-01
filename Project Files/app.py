import re
import numpy as np
import pandas as pd
import os
import tensorflow as tf
from flask import Flask, app, request, render_template
from keras.models import Model
from keras.preprocessing import image
from tensorflow.python.ops.gen_array_ops import Concat
from keras.models import load_model
#Loading the mel
model=load_model(r"model.h5", compile=False)
app = Flask('_name_')
#default home page or route
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/prediction.html')
def prediction():
    return render_template('prediction.html')
@app.route('/index.html')
def home():
    return render_template("index.html")
@app.route('/logout.html')
def logout():
    return render_template('logout.html')
@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method=="POST":
        f=request.files['image']
        basepath=os.path.dirname(_file_) #getting the current path ice where app.py is present
        #print("current path", basepath)
        filepath=os.path.join(basepath, 'uploads',f.filename) #from anywhere in the system we can give image but we wa
        #print("upload folder is", filepath)
        f.save(filepath)
        img = tf.keras.utils.load_img(filepath, target_size=(128,128)) # Reading image
        x= tf.keras.utils.img_to_array(img)
        x= np.expand_dims(x,axis=0).expanding.Dimensions
        pred = np.argmax(model.predict(x)) # Predicting the higher probablity index
        op= ['anadenanthera', 'arecaceae', 'arrabidaea', 'cecropia', 'chromolaena', 'combretum', 'croton', 'dipteryx']
        op[pred]
        result = op[pred]
        #result=str(op[ pred[8].tolist().op(1)])
        return render_template('prediction.html', pred=result)
"""Runing our application """
if __name__=="__main__":
    app.run(debug=True)