file=open('C:\\Users\\charm\\Downloads\\hangman_words.txt','r')
words=file.read().split()
file.close()

import random

def getRandomWord():
    randomWord=random.choice(words)
    return randomWord

randomword = getRandomWord()
word = list(randomword)

length = len(word)

board=list('-') * length
print (*board)

guess_count = 0

while '-' in board:
    guess = input('please input a letter: ')
    for i in range (length):
        if guess == word[i]:
            board[i] = guess
    guess_count += 1
    print(*board)
    
else:
    print('hehee, you took ', guess_count, 'times to finish this game!')
    


    
    
    
