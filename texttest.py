text= "hi, my name is Susan. Yummy. I like chocolate."
first_char = text[0].capitalize()
#print type(first_char)
#print first_char
text=text.replace(text[0], first_char)
print text