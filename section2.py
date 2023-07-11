# Section 2: Concept Questions [19 marks]

# 2.1 Write a function that takes in an input and checks to see if it’s an isogram. The function should return True or False.
# An isogram is a word where no letter is repeated. Examples include:
# ● "isogram"
# ● "uncopyrightable" ● “ambidextrously”
def is_isogram(word):
    if not isinstance(word, str):
        raise ValueError('Your input need to be a string.')
    word = word.lower()  
    return len(word) == len(set(word)) 

