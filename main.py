a = "GAME START"
b = "GAME END"
answers = 'агбгаббабб'
print(a.center(50, '-'))
listt = []


def question(file_name, correct):
    score = 0
    with open(file_name) as file:
        print(file.read())
        answer = input('Відповідь: ')
        if answer == correct:
            print('Вірно!')
            score += 1
            listt.append(score)
        else:
            print('Не вірно :(')


for i in range(1, 11):
    question1 = str(i) + '.txt'
    question(question1, answers[i - 1])
    print(' ')

print(f'ваша кількість балів: {sum(listt)}')
print(b.center(50, '-'))
