import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('C:/Users/APURAV/Desktop/project-dog-classification/sample_images/beaglier.jpg','rb')})