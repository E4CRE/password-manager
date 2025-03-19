##### Libraries #####

import random as rd
import string
import secrets

##### Variables #####

symbols = string.punctuation
numbers = string.digits
letters = string.ascii_letters
characters = symbols + numbers + letters



##### Functions ######

def psdgen(l:int):
    """Generate a secured password, l = length >11"""

    if l < 12:
        return "The password length must be at least 12 characters."

    psd = [secrets.choice(characters) for i in range(l)]
    rd.shuffle(psd)
    print("your password :",''.join(psd))
    
    return ''.join(psd)
