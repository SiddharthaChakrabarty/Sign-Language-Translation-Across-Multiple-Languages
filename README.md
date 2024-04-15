# Sign-Language-Translation-Across-Multiple-Languages

## Overview
This project aims to provide a real-time sign language translation system using deep learning. The system recognizes hand gestures captured by a webcam and translates them into text, displaying the corresponding meaning in the chosen language.
![image](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/119057806/015cede5-4949-45bf-8036-583095a56274)
![image](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/119057806/16c7a978-0e0e-488c-b8f8-9d03312f5cad)
![image](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/119057806/6a9851da-3be9-4ca6-98cb-b36ce11a288d)
![WhatsApp Image 2024-02-06 at 8 22 46 PM](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/126079866/30116616-2e6c-4c90-bc40-577eea585756)
![WhatsApp Image 2024-02-06 at 8 22 46 PM (1)](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/126079866/9cd10392-5df0-4173-8684-1a472765e0c9)
![WhatsApp Image 2024-02-06 at 8 22 47 PM](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages/assets/126079866/b656ada8-8dff-4d7d-ac76-bcc4c0276000)




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

### 2. `Training/ASL.py`
   - Script for training the American Sign Language (ASL) model.
   - Uses TensorFlow and Keras for deep learning.
   - CNN architecture for recognizing hand gestures.
   - Data augmentation and preprocessing are applied using ImageDataGenerator.
   - The trained model is saved as `asl_model.h5`.

### 3. `Training/ISL.ipynb`
   - Script for training the Indian Sign Language (ISL) model.
   - Similar structure to ASL training script.
   - The trained model is saved as `isl_model.h5`.

### 4. `Training/Gestures.ipynb`
   - Script for training a model to recognize general hand gestures.
   - The model can identify gestures like "Bye," "Call Me," "Dislike," "Good Job," "Good Luck," "Peace," "Praying," and "Rock On."
   - The trained model is saved as `model.h5`.

### 5. `Training/createdataset.py`
   - Script for capturing and creating a dataset for training.
   - Uses webcam input to capture hand gestures.
   - Segments the hand region and saves images for training.

## How to Run
1. Execute `Final_deployement.py` to launch the application.
2. Choose the target language and click "Submit" to start real-time sign language translation.
3. Use the buttons to select the sign language model for translation.

## Dependencies
- TensorFlow
- Keras
- OpenCV
- Numpy
- Googletrans
- Tkinter
- PIL

## Contact

For any questions or feedback, feel free to reach out:

- Siddhartha Chakrabarty - [GitHub](https://github.com/SiddharthaChakrabarty) | [LinkedIn](www.linkedin.com/in/siddharthachakrabarty)
- Sneha Jain - [GitHub](https://github.com/JainSneha6) | [LinkedIn](https://www.linkedin.com/in/sneha-jain-473357261/)
- [Project Repository](https://github.com/SiddharthaChakrabarty/Sign-Language-Translation-Across-Multiple-Languages)


## Acknowledgments
This project was developed as part of a deep learning and computer vision exploration.

Feel free to contribute and improve this project!

 
