from question import question

questions_prompt = [
    "Qual cor é a cor da maçã?\n(a) Vermelha\n(b) Verde\n(c) Laranja\n",
    "Qual é a cor da banana?\n(a) Azul\n(b) Amarela\n(c) Roxa\n",
    "Qual é a cor do morango?\n(a) Amarela\n(b) Azul\n(c) Vermelha\n"
]

questions = [
    question(questions_prompt[0], "a"),
    question(questions_prompt[1], "b"),
    question(questions_prompt[2], "c")
]

def run_test(perguntas):
    score = 0
    for question in questions:
        answer = input(questions_prompt)
        if answer == questions_prompt:
            score += 1
    print("Você acertou" + str(score) + "/" + str(len(questions)))