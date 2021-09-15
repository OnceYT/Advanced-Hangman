import random 


with open("hangman_words.txt") as f: #Gets a list of words from the included HangmanWords.txt
  words = f.read().splitlines()

guess_list = []  #A list where we store amd compare the user's guesses
lives = 10  #The total lives the user has
word = random.choice(words).upper()  #Chooses a random word from the list
print("Let's see if you can guess the word 👀\n")

def get_masked_word():
  """
  Function to encode the word in a format of dashes (_)
  It'll be ran on every user input to show the current game progression
  The result will also be used to check if the user has guessed all the words successfully (and thus won the game)
  """
  return " ".join([letter if letter in guess_list else '_' for letter in word])

while lives > 0:  #Will loop untill lives are 0
  print(f"{get_masked_word()} | You have {lives} lives remaining!\n")
  guess = input("Enter your guess: ").upper()

  if guess in guess_list:  #Checks if the user already guessed the letter
    print(f"\n❌ You had already guessed {guess}!\n")
    continue

  if guess in word:  #Checks if the letter is in the word
    guess_list.append(guess)
    print(f"\n✔️ Your guess was correct! {guess} is in the word.\n") 
  else:  #The user loses a life if the letter is not in the word
    lives -= 1
    print(f"\n❌ {guess} is not in the word! You lost one life, you have {lives} lives remaining!\n")

  if not "_" in get_masked_word():  #User wins if all letters have been successfully guessed
    print(f"\nCongratulations! You guessed it, the word was '{word.lower()}'!")
    break
    
if lives == 0:  #Shows the correct word if the user fails to guess it and loses all their lives
  print(f"\n{word} was the correct word!")
