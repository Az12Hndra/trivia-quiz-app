import requests
import random
import html

# To fetch the API 
def get_questions(amount=10):
    url = f'https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple'
    response = requests.get(url)
    data = response.json()

    if data['response_code'] != 0:
        print('Failed to fetch questions. Check your internet connection.')
        return []
    
    return data['results']

#questions = get_questions()
#print(questions)

def display_question(question_data, number):
    question = html.unescape(question_data['question'])
    correct_answer = html.unescape(question_data['correct_answer'])
    incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]
    
    # Why correct answer is using bracket is because we want to make it a list 
    # so that we can combine it with incorrect answers list
    all_answers = incorrect_answers + [correct_answer]
    
    # We want to shuffle the answers so that the correct answer is not always in the same position
    random.shuffle(all_answers)

    print(f'Question {number}: {question}')
    print(f"Category: {question_data['category']} | Difficulty: {question_data['difficulty'].capitalize()}")
    for index, answer in enumerate(all_answers, 1):
        print(f'{index}. {answer}')
    
    return correct_answer, all_answers

def get_user_answer(answers):
    valid_choice = [str(i) for i in range(1, len(answers) + 1)]
    while True:
        choice = input('\nYour answer (enter the number): ').strip()
        if choice in valid_choice:
            return int(choice)
        print('Invalid choice. Please enter a number corresponding to your answer.')
    

def play_quiz():
    print('=' * 33)
    print('Welcome to the Trivia Sport Quiz!')
    print('=' * 33)

    print('\nFetching questions...')
    questions = get_questions(amount=10)

    if not questions:
        return
    
    score = 0

    for i, question_data in enumerate(questions, start=1):
        correct, answers = display_question(question_data, i)
        choice = get_user_answer(answers)

        selected_answer = answers[choice - 1]

        if selected_answer == correct:
            print('✅ Correct!')
            score += 1
        else:
            print(f'❌ Wrong! The correct answer was: {correct}')
    
    print('\n' + '=' * 33)
    print(f'Quiz Over! Your score: {score}/{len(questions)}')

    if score == len(questions):
        print('🎉 Perfect score! You are a sports trivia master!')
    elif score >= len(questions) * 0.7:
        print('👍 Great job! You know your sports trivia well!')
    elif score >= len(questions) * 0.5:
        print('🙂 Not bad! You have a decent knowledge of sports trivia.')
    else:
        print('📚 Keep learning! You can do better next time!')

    print('=' * 33)

def main():
    while True:
        play_quiz()
        again = input('\nDo you want to play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing! Goodbye!')
            break

if __name__ == '__main__':
    main()
