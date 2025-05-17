import requests
import json
#     print(json.dumps(**VARIABELE**, indent=4))

trivia_url = "https://opentdb.com/api.php?amount=1"

print

def get_question():
    response = requests.get(trivia_url)
    if response.status_code == 200:
        response = response.json()
        question = response['results'][0]['question']
        correct_answer = response['results'][0]['correct_answer']
        incorrect_answers = response['results'][0]['incorrect_answers']
        all_answers = incorrect_answers + [correct_answer]
        all_answers.sort(reverse=True)
        # print(question)
        # print(correct_answer)
        # print(all_answers)
        return question, correct_answer, all_answers
    else:
        print(f'Failed to retrieve question: code:{response.status_code} -- {response.text}')
        return None, None, None

def print_question(question, answers):
    print(question)
    i = 1
    for answer in answers:
        print(f'{i}: {answer}')
        i += 1

def get_answer():
    try:
        return int(input('What is your answer"? \n'))
    except ValueError:
        print('Please enter a valid number.')
        return get_answer()

def check_answer(user_answer, correct_answer_index):
    return user_answer == correct_answer_index

def play_that_game():
    input('Hit Enter to get the next question')
    question, correct_answer, all_answers = get_question()
    if question and correct_answer and all_answers:
        print_question(question, all_answers)
        user_answer = get_answer()
        if check_answer(user_answer, all_answers.index(correct_answer) + 1):
            print('Correct!')
        else:
            print('Incorrect, the correct answer is', correct_answer)
            print("")
    else:
        play_that_game()

def main():
    print("Welcome to Trivia Game!")
    play_again = True

    while play_again:
        play_that_game()
        print("Do you want to play another round? (yes/no)")
        response = input()
        play_again = response == "yes" or response == "y"

    print("Thank you for playing!")


main()