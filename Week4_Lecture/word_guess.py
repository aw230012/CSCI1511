import random

word_bank = ['Apple', 'Chair', 'House', 'Book', 'Light', 'Ball', 'Tree', 'Fish', 'Cat', 'Dog']

print('Welcome to Word Guess!');
print('The object of the game is to guess 3 random words from the word bank.')
print('You have 10 total guesses to guess all 3 words and the guess words do not repeat.')
print('The guess words do not repeat.\n')
print('Your guesses start...now!\n')

guesses_correct = 0
guess_word = word_bank[random.randrange(0, len(word_bank))]
word_bank.remove(guess_word) 

for round in range(1, 11):
  print(f"Round {round}\nWords left in bank: {word_bank}.\n")

  print(f"\n{guess_word}\n")  
  guess = input("Enter your guess: ")

  if guess.lower() == guess_word.lower():
    guesses_correct += 1
    print("Correct!\n")

    # user guessed correctly, select the next word
    guess_word = word_bank[random.randrange(0, len(word_bank))]
    word_bank.remove(guess_word) 
  else:
    print("Incorrect! Please try again.")

  if guesses_correct == 3:
    print("Congratulations! You've guessed all 3 words correctly!")
    break
  

if guesses_correct < 3:
  print("You've run out of guesses. Better luck next time!")
