import os, glob
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
#loading and running the model
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,static_url_path='/static', 
            static_folder=os.path.join(APP_ROOT,'templates/static'))

#setting the target folder for saving images



classes = ['This is a JackFruit','This is a Mango','Sorry, I don\'t recognize this']

target_folder = APP_ROOT + "/images/"
if not os.path.isdir(target_folder):
    os.mkdir(target_folder)
    
target = os.path.join(APP_ROOT, 'images')


@app.route("/")
def index():
    filelist = glob.glob(os.path.join(target, "*"))
    for f in filelist:
        os.remove(f)
    return render_template("index.html")
#saving the image from the user to target folder.
@app.route("/upload", methods=["POST"])
def upload():
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        new_model = load_model(os.path.join(APP_ROOT, 'models/chamasifier_1.h5'))
        new_model.summary()
        test_image = image.load_img(os.path.join(APP_ROOT,'images/'+filename),target_size=(150,150))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = new_model.predict(test_image)
        if result[0][0] == 0:
            prediction = classes[0]
        elif result[0][0] == 1:
            prediction = classes[1]
        else:
            prediction = classes[2]


    return render_template("result.html",image_name=filename, text=prediction)
#function for loading image from the directory.
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=False)