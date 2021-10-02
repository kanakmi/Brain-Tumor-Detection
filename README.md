# Brain Tumor Detection

## 💡 Inspiration
We wanted to reduce the time that a doctor would require to identify Tumor in Brain MRI Scans so we built a tool that could assist doctors in this task.

## 💻 What it does
Brain Tumor Detection first classifies a Brain MRI image as Tumor/Non-Tumor using a simple Convolutional Neural Network.<br>
If tumor is found, it further tries to localize it using a UNet CNN model.<br>
Both the models are built from scratch.

## ⚙️How we built it

- ML: Python, TensorFlow
- Frontend: HTML, CSS, JS
- Backend: Django
- Database: CockroachDB
- Authentication: Auth0
- Sending results: Twilio

### About the Model

#### Classifier Model-
- Dataset had 3929 total Brain MRI images
- 2556 images belonged to the category of No Tumor
- 1373 images belonged to the category of Tumor
- The model was designed using 6 Convolutional Layers, 1 Dense Layers and 1 output layer (with 2 neurons)
- Accuracy Achived - 96.27%

#### Localization Model-
- Dataset had 1373 total Brain MRI images
- 1167 images were used to train the model
- 103 images were used for Validation and Testing Respectively
- The model has a typical UNet Architecture with
  - 4 Downsampling Convolutional Blocks
  - A Bottle-neck Convolutional Block (without Maxpooling)
  - 4 Upsampling Convolutional Blocks with skip connections attached
  - 1 seperate Conv2D layer
  - Conv2D Output layer 
- Accuracy Achived - 97%

## Use of Twilio

- For sending the result from the model to mobile number.

## Use of CockroachDB

- We have used CockroachDB as a primary database because it is an easy-to-use, open-source and indestructible SQL database.

## 🔑 Auth0

- We have used Auth0 for secure user authentication

## 🧠 Challenges we ran into
This was the first time we were working with image segmentation task and the problem with UNet is that since you have to manage those "skip connections" and add them later on, the dimentions of image matrices on both the sides should be equal. We had to cover a lot of math to finally get those dimentions right and it took most of our time.

## 🏅 Accomplishments that we're proud of
We are elated that we were able to cover new grounds and learn something new in a matter of just few hours and completing our project always gives us great pleasure.<br>
Achieving around 97% accuracy on both the tasks was a cherry on the top.

## 📖 What we learned
We learned all about the UNet Architecure of Neural Networks that is primarily used for pixel level image segmentation, collaboration and team work.

## 🚀 What's next for Brain Tumor Detection

Improving the accuracy of the model.
