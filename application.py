from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from com_in_ineuron_ai_utils.utils import decodeImage
from predict import dogcat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

application = Flask(__name__)
CORS(application)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = dogcat(self.filename)

#When i talk about web Api, they can't be excecuted on local machine.
#We need a server for that.



#For all the base url backslash is called defaultly
#
@application.route("/", methods=['GET'])   #route- url
@cross_origin() #It will allow us interact with http and https--
#means it does not block request -> to access from each other.
def home():
    return render_template('index.html')

@application.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image'] #transfering image in string format using base64
    decodeImage(image, clApp.filename) #base64 is  used to encode binary data (image,sound) for embedding into HTML,CSS,TXT DOCS
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


clApp = ClientApp()
# #port = int(os.getenv("PORT"))
if __name__ == "__main__":
    # clApp = ClientApp()
    # app.run(host='0.0.0.0', port=port)
    application.run(debug=True)
