MARKDOWN

# NLP App with Tkinter

This project is a GUI-based NLP application built using Python's Tkinter library. The app includes features for performing **Sentiment Analysis**, **Named Entity Recognition (NER)**, and **Emotion Analysis** on user-provided text.

## Features

1. **User Authentication**: 
   - Register new users and log in with an existing account.
   - Data is stored in a simple JSON-based database.

2. **Sentiment Analysis**: 
   - Uses TextBlob to evaluate the polarity and subjectivity of the input text.

3. **Named Entity Recognition (NER)**: 
   - Employs NLTK to recognize and extract named entities (such as people, locations, etc.).

4. **Emotion Prediction**: 
   - Matches words in the text to predefined categories of emotions (Happy, Sad, Angry, Surprised).

## Installation

### Prerequisites
- Python 3.x
- The following Python libraries are required:
  ```bash
  pip install textblob nltk


Steps
Clone the repository:
git clone https://github.com/your-username/nlp-app.git


Download necessary NLTK data files:
python -m nltk.downloader punkt averaged_perceptron_tagger maxent_ne_chunker words


Run the application:
python nlp_app.py


Usage
Launch the app by running nlp_app.py.
Use the GUI to register a new user or log in with existing credentials.
Once logged in, you can perform the following NLP tasks:
Sentiment Analysis: Evaluate the sentiment of any given text.
NER: Extract named entities from the text.
Emotion Prediction: Detect emotions in the text based on predefined categories.



Technologies Used
Python
Tkinter for GUI
TextBlob for Sentiment Analysis
NLTK for NER and other NLP functionalities
Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have suggestions or find any bugs.

License
This project is licensed under the MIT License.
