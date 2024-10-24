import json
from tkinter import *
from tkinter import messagebox
from textblob import TextBlob
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import re

# Ensure the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


class Api:

    def sentiment_analysis(self, text):
        blob = TextBlob(text)
        return blob.sentiment

    def named_entity_recognition(self, text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        chunks = ne_chunk(pos_tags)

        entities = []
        for chunk in chunks:
            if isinstance(chunk, Tree):
                entity_name = " ".join([word for word, pos in chunk.leaves()])
                entity_type = chunk.label()
                entities.append((entity_name, entity_type))
        return entities

    def emotion_analysis(self, text):
        emotions = {
            "happy": ["happy", "joyful", "cheerful", "delighted"],
            "sad": ["sad", "unhappy", "sorrowful", "depressed"],
            "angry": ["angry", "mad", "furious", "irritated"],
            "surprised": ["surprised", "shocked", "astonished"],
        }

        emotion_counts = {emotion: 0 for emotion in emotions.keys()}

        for word in text.split():
            for emotion, keywords in emotions.items():
                if word.lower() in keywords:
                    emotion_counts[emotion] += 1

        return emotion_counts


class Database:
    def __init__(self, db_file='db.json'):
        self.db_file = db_file

    def _load_database(self):
        try:
            with open(self.db_file, 'r') as rf:
                return json.load(rf)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_database(self, database):
        with open(self.db_file, 'w') as wf:
            json.dump(database, wf, indent=4)

    def _validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def add_data(self, name, email, password):
        if not self._validate_email(email):
            return "Invalid email format"

        database = self._load_database()

        if email in database:
            return 0  # Email already exists
        else:
            database[email] = [name, password]
            self._save_database(database)
            return 1  # Registration successful

    def search(self, email, password):
        database = self._load_database()

        if email in database and database[email][1] == password:
            return 1  # Login successful
        else:
            return 0  # Login failed


class Nlp:
    def __init__(self):
        self.dbo = Database()
        self.apio = Api()

        # login GUI
        self.root = Tk()
        self.root.configure(bg='#b3b6b7')
        self.root.title('NLP App')
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry('500x600')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        label1 = Label(self.root, text='EMAIL')
        label1.pack(pady=(30, 30))
        label1.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='PASSWORD')
        label2.pack(pady=(30, 30))
        label2.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        self.password_input = Entry(self.root, width=40, show="#")
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root, text='Login', height=2, width=20, command=self.perform_login)
        login_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Not a Member?')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        redirect_btn = Button(self.root, text='Register now', height=2, width=20, command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        label0 = Label(self.root, text='NAME')
        label0.pack(pady=(20, 20))
        label0.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='EMAIL')
        label1.pack(pady=(20, 20))
        label1.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='PASSWORD')
        label2.pack(pady=(20, 20))
        label2.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        self.password_input = Entry(self.root, width=40, show="#")
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', height=2, width=20, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?')
        label3.pack(pady=(20, 10))
        label3.configure(font=('verdana', 24, 'italic'), bg='#b3b6b7', fg='black')

        redirect_btn = Button(self.root, text='Login now', height=2, width=20, command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response == 1:
            messagebox.showinfo('Success', 'Registration successful')
        elif response == 0:
            messagebox.showerror('Error', 'Email already exists')
        else:
            messagebox.showerror('Error', response)  # Invalid email format

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect information')

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text='NLPAPP', bg='#b3b6b7', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'italic'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', height=2, width=20, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='NER', height=2, width=20, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', height=2, width=20, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', height=4, width=10, command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text='NLP App', bg='#b3b6b7', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'italic'))

        text_input = Text(self.root, height=10, width=40)
        text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze Sentiment', command=lambda: self.perform_sentiment_analysis(text_input.get("1.0", END)))
        analyze_btn.pack(pady=(10, 10))

    def perform_sentiment_analysis(self, text):
        sentiment = self.apio.sentiment_analysis(text)
        messagebox.showinfo('Sentiment Analysis', f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")

    def ner_gui(self):
        self.clear()
        heading = Label(self.root, text='NER', bg='#b3b6b7', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'italic'))

        text_input = Text(self.root, height=10, width=40)
        text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze NER', command=lambda: self.perform_ner(text_input.get("1.0", END)))
        analyze_btn.pack(pady=(10, 10))

    def perform_ner(self, text):
        entities = self.apio.named_entity_recognition(text)
        messagebox.showinfo('NER', str(entities))

    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text='Emotion Analysis', bg='#b3b6b7', fg='black')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'italic'))

        text_input = Text(self.root, height=10, width=40)
        text_input.pack(pady=(10, 10))

        analyze_btn = Button(self.root, text='Analyze Emotion', command=lambda: self.perform_emotion_analysis(text_input.get("1.0", END)))
        analyze_btn.pack(pady=(10, 10))

    def perform_emotion_analysis(self, text):
        emotion = self.apio.emotion_analysis(text)
        messagebox.showinfo('Emotion Analysis', str(emotion))


nlp = Nlp()