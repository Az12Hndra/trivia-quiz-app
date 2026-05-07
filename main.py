import requests
import random
import html

def get_questions(amount=10):
    url = f'https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple'
    response = requests.get(url)
    data = response.json()

    if data['response_code'] != 0:
        print('Failed to fetch questions. Check your internet connection.')
        return []
    
    return data['results']