import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

#setting the target folder for saving images.
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target_folder = APP_ROOT + "/images/"
if not os.path.isdir(target_folder):
    os.mkdir(target_folder)
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    #saving the image from the user to target folder.
    img_file = request.files['file']
    filename = img_file.filename
    destination = target_folder + filename
    print ("Accepting incoming file:", filename)
    print ("Saving to:", destination)
    img_file.save(destination)
    
    import numpy as np
    from tensorflow.keras.preprocessing import image
    from tensorflow.keras.models import load_model
    
    #loading and running the model.
    new_model = load_model('models/chamasifier_1.h5')
    test_image = image.load_img('images/'+filename,target_size=(150,150))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = new_model.predict(test_image)

    if result[0][0] == 0:
        prediction = "This is a JackFruit"
    elif result[0][0] == 1:
        prediction = "This is a Mango"
    else:
        prediction = "Sorry,I don't recognize this fruit"
		
    return render_template("result.html",image_name=filename, text=prediction)

#function for loading image from the directory.
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True)
