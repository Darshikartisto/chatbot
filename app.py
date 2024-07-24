from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('chatbotdatset.csv')

# Extract unique sections
sections = dataset['Section'].unique()

@app.route('/')
def home():
    return render_template('home.html', sections=sections)

@app.route('/questions/<section>')
def questions(section):
    section_questions = dataset[dataset['Section'] == section]['Question'].tolist()
    return render_template('questions.html', section=section, questions=section_questions)

@app.route('/answer/<section>/<question>')
def answer(section, question):
    answer = dataset[(dataset['Section'] == section) & (dataset['Question'] == question)]['Answer'].values[0]
    return render_template('answer.html', section=section, question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)


