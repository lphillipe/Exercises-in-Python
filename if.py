is_male = False  
is_tall = True



if is_male and is_tall:
    print("Você é um homem alto.")

elif is_male and not is_tall:
    print("Você é um homem baixo.")

elif not is_male and is_tall:
    print("Voçê não é homem, mas é alto")

else:
    print("Você não é homem e nem alto.")