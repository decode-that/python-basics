# Repetition of Print Statement Demo

import pyjokes 
joke = pyjokes.get_joke(language='en', category='all')

n = 10 # number of repetitions
print(f"{joke}\n" * n)