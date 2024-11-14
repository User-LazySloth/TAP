import mysql.connector
from datetime import datetime
import ollama
import json
from fpdf import FPDF

def workDescriptionsSummarizer(work_descriptions):
    response = ollama.chat(model = 'llama3.2', messages = [
    {
        'role': 'user',
        'content': f'Please summarize all the work done by a certain Teaching Assistant given the work done by the day everytime he is on the clock: {work_descriptions}. Please ensure that the summary is provided in a json format: "Summary: [point1, point2, ..]"',
    },
    ])
    return response['message']['content']


