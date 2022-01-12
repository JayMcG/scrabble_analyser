# Text file containing valid words to compare against
with open("wordlist.txt") as words:
  wording = words.read()

# Letters and points per letter:
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combined list:
letters_to_points = {
  key: value
  for key, value
  in zip(letters, points)
}

letters_to_points[" "] = 0

# User input for word analysis:
print("Hello, welcome to the \"Scrabble Word Analyser\".")
user_input = input("Please provide your word for analysis: ")
word_raw = []
word_raw.append(user_input.upper())
word = word_raw[0]

# Word analyser function:
def score_word(user_word):
  points_total = 0
  for letter in user_word:
    points_total += letters_to_points.get(letter, 0)
  return points_total

score = score_word(word)

# Function to check if word entered by user is valid
def word_check(word):
  if word.lower() in wording:
    
    print("The word you provided is {}".format(word))
    print("Your word is valid, {word} has a total score of {score}".format(word=word, score=score))
  else:
    print("The word you provided is {}".format(word))
    print("That is not a valid word.")

word_check(word)

