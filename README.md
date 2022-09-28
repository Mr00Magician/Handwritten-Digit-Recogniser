<h1 align = "center"> HANDWRITTEN DIGIT RECOGNISER 
  <h3 align = "center"> Made with ❤️ and <img title = "Python" src = "https://user-images.githubusercontent.com/92143521/166102826-59081947-8e61-4e41-87d6-58ef893f0187.svg" height = "20px"> by Mr00Magician
  </h3>
</h1>
<br>
<br>

## ABOUT THE APP
A standalone application that makes use of Machine Learning to try and recognise a hand-drawn (or rather, mouse-drawn) digit. I also made a web implementation of this app (basically a web app) using Gradio and Hugging face in case you simply want to try it out. Here's the link to it: https://huggingface.co/spaces/Mr00Magician/Handwritten-Digit-Recogniser

## HOW IT WORKS
Upon running, the app will provide you with a blank white interface on which you can draw a digit with your mouse, by clicking and dragging.
The app will then capture an image of the digit drawn and pass it to a neural network which will predict which digit has been drawn.

## HOW TO RUN
To run this app, follow these simple steps:
- See that you have `Python` installed.
- Clone this repository.
- Create a new Python environment and install the dependencies in it. This can be done as follows:
  - Open `command prompt` and `cd` to the directory where you have cloned the repo.
  - Run the command `Python -m venv env` to create a new virtual environment named `env`
  - Activate the enviroment by running the command `env\Scripts\activate.bat`
  - Install depencies by running the command `pip install -r requirements.txt` <br> 

The above steps will create a python virtual environment and install the required depndencies in it. Now whenever you want to run the app, follow these steps:
- Open `command prompt` and `cd` to the directory where you have cloned the repo.
- Activate the python environment by running the command `env\Scripts\activate.bat`.
- Run the app by the command `Python digit_recog_GUI.py`. <br> <br>

## SCREENSHOTS
  |![App Window](https://user-images.githubusercontent.com/92143521/166221413-9aa1a3ce-9021-4898-a354-181cf3196aa3.png)|
  |:--:|
  |Application Window|
  |![Digit 1](https://user-images.githubusercontent.com/92143521/166222673-8ff0bedd-8fc2-488c-bd9f-5a04fb3210d2.png)|
  |:--:|
  |![Digit 5](https://user-images.githubusercontent.com/92143521/166222725-42585cf8-fe83-4b1d-beef-bcf4d943cf88.png)|
  |:--:|

## A GIF TO DEMONSTRATE WORKING OF THE APP
  ![DigitRecogniser Sample](https://user-images.githubusercontent.com/92143521/166222772-0fb2ffaf-aa4d-49ae-902c-f1498c8969dc.gif)
  
