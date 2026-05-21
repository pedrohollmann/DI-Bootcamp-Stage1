#Exercise 5: Let’s Create Some Personalized Shirts!

# #1

def make_shirt(size, text):
    print(f'Size: {size}, Text: {text}')

make_shirt('XXL', 'I love Israel')

# #2

def make_shirt(size ='Large', text ='I love Python'):
    print(f'Size: {size}, Text: {text}') 

make_shirt()

# #3

def make_shirt(size = 'medium', text = 'I love Pyhton'):
    print(f'Your size is {size} and the text is {text}, correct?')

make_shirt()

# #4

def make_shirt(size, text):
    print(f'My size is {size}, and the text is {text}')

make_shirt('XXL', 'Shalom')

#5

def make_shirt(size='small', text='Hi'):
    print(f'Text: {text}, Size: {size}')

make_shirt(size="small", text="Hello!")