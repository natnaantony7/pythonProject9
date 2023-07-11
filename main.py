import json


def fr():
    with open('questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)
def print_question(question):
    print(
        f"Вопрос: {question['q']}?\n"
        f"Сложность: {question['d']} из 5."
    )
def check_user_answer(question):
    for i in range(3, 0, -1):
        if input(': ').lower() == question['a'].lower():
            return True
        print(f"Осталось попыток {i-1}.")
        print_question(question)
    return False

def print_results(score, questions):
    max_score = sum(
        [item['d']
         for item in questions]
    )
    print(f"Конец! Вы заработали {score} из {max_score}")
def main():
    score = 0
    for question in fr():
        print_question(question)
        if check_user_answer(question):
            score += question['d']
            print(f"Правильно, вы заработали {question['d']} баллов")
        else:
            print(f"Неправильно, правильный ответ: {question['a']}.")
if __name__ == '__main__':
    main()
