from Question import Question

question_prompts = [
    "Qual cor é a cor da maçã?\n(a) Vermelha\n(b) Verde\n(c) Laranja\n",
    "Qual é a cor da banana?\n(a) Azul\n(b) Amarela\n(c) Roxa\n",
    "Qual é a cor do morango?\n(a) Amarela\n(b) Azul\n(c) Vermelha\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Você acertou" + str(score) + "/" + str(len(questions)))

run_test(questions)