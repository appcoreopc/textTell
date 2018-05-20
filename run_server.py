from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io
from gensim.models import Word2Vec
import json
from flask import Flask, request, jsonify
from gensim.models import Word2Vec

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)



class TextSet(object):
  def __init__(self, j):
   self.__dict__ = json.loads(j)

def load_model():
	model = Word2Vec.load(jargons)
	#model = ResNet50(weights="imagenet")

def prepare_image(image, target):
	# if the image mode is not RGB, convert it
	if image.mode != "RGB":
		image = image.convert("RGB")

	# resize the input image and preprocess it
	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)
	# return the processed image
	return image

#
#  {
#     query : 
#     trainingSet : 
#  }
#

@app.route("/predict", methods=["POST", "GET"])
def get():	
   textQuery = request.args.get("text")
   nextWord = request.args.get("next")
   print(textQuery)
   similiarity = model.wv.similarity(textQuery, nextWord)
   return flask.jsonify(similiarity)
   

@app.route("/train", methods=["POST"])
def predict(): 
 global jargons 
 jargons = []
 data = {"success": False}

 if flask.request.method == "POST":
  jsonData = request.json
  trainingSet = request.json["trainingSet"]
  print(trainingSet)

  word_to_vec(trainingSet)
  global model
  print(jargons)
  model = Word2Vec(jargons, min_count=1)
  data["success"] = True
  print("training done.")

 # return the data dictionary as a JSON response
 return flask.jsonify(data)


def word_to_vec(lines):
 print(lines)
 # split data into an array
 #for wordPart in lines:
 jargons.append(lines.split())


 
 


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	#load_model()
	app.run()