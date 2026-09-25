def word_length(word1, word2):
    word = word1 + word2
    return len(word)
    print("This never gets printed")

length1 = word_length("Rob", "Banks")                     
length2 = word_length("Barbie", "Kenn")                   
length3 = word_length("Holly", "Jolley")                  

print("One name is", length1, "letters long.")            
print("Another name is", length2, "letters long.")        
print("The final name is", length3, "letters long.") 