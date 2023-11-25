# Sign-Language-Translation-Across-Multiple-Languages

## Overview
This project aims to provide a real-time sign language translation system using deep learning. The system recognizes hand gestures captured by a webcam and translates them into text, displaying the corresponding meaning in the chosen language.

## Features
- **Language Selection:** Users can choose their desired language from a list of options, including Hindi, Marathi, Gujarati, Kannada, Tamil, Telugu, Bengali, and Malayalam.
- **Translation:** The system translates recognized sign language gestures into the selected language.
- **Font Customization:** The translated text is displayed using custom fonts suitable for each language.
- **Sign Language Models:** The project includes three different sign language models for American Sign Language (ASL), Indian Sign Language (ISL), and general hand gestures.

## Components
### 1. `Final_deployement.py`
   - Main script for the graphical user interface (GUI) and real-time sign language translation.
   - Utilizes the Tkinter library for GUI development.
   - Implements a webcam interface for capturing hand gestures.
   - Allows users to choose the target language and submit their selection for translation.
   - Includes buttons to choose between ASL, ISL, and general gestures for translation.

### 2. `training/asl.py`
   - Script for training the American Sign Language (ASL) model.
   - Uses TensorFlow and Keras for deep learning.
   - CNN architecture for recognizing hand gestures.
   - Data augmentation and preprocessing are applied using ImageDataGenerator.
   - The trained model is saved as `asl_model.h5`.

### 3. `training/isl.ipynb`
   - Script for training the Indian Sign Language (ISL) model.
   - Similar structure to ASL training script.
   - The trained model is saved as `isl_model.h5`.

### 4. `training/gestures.ipynb`
   - Script for training a model to recognize general hand gestures.
   - The model can identify gestures like "Bye," "Call Me," "Dislike," "Good Job," "Good Luck," "Peace," "Praying," and "Rock On."
   - The trained model is saved as `model.h5`.

### 5. `createdataset.py`
   - Script for capturing and creating a dataset for training.
   - Uses webcam input to capture hand gestures.
   - Segments the hand region and saves images for training.

## How to Run
1. Run `createdataset.py` to capture and create datasets for training.
2. Run each training script (`asl.py`, `isl.ipynb`, `gestures.ipynb`) to train the corresponding models.
3. Execute `final_deployement.py` to launch the application.
4. Choose the target language and click "Submit" to start real-time sign language translation.
5. Use the buttons to select the sign language model for translation.

## Dependencies
- TensorFlow
- Keras
- OpenCV
- Numpy
- Googletrans
- Tkinter
- PIL

## Acknowledgments
This project was developed as part of a deep learning and computer vision exploration.

Feel free to contribute and improve this project!

 
