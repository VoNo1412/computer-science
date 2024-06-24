import random

class HangMan():
    def __init__(self, max_attemps = 10, num_attemps = 0, guess_letter = ""):
        self.hyphenLower = []
        self.word = self.randomWord()
        self.max_attemps = max_attemps
        self.num_attemps = num_attemps
        self.guessLetter = guess_letter


    def randomWord(self):
        someWords = '''apple banana mango strawberry  
        orange grape pineapple apricot lemon coconut watermelon 
        cherry papaya berry peach lychee muskmelon'''
        
        someWords = someWords.split(' ') 
        fruits = [fruit.strip().replace("'", "") for fruit in someWords if fruit.strip() != '' and fruit.strip() != '\n']

        # randomly choose a secret word from our "someWords" LIST. 
        return random.choice(fruits);


    def hyphen_letter(self):
        guessLetter = input("\n\nEnter to letter to guess: ");
        self.guessLetter = guessLetter;
        self.num_attemps += 1;

        if guessLetter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guessLetter and self.hyphenLower[i] == "_":
                    self.hyphenLower[i] = guessLetter;
                    break;
    
            print(" ".join(self.hyphenLower))
            
        else:
            print(guessLetter + " not letter in word")


    def play(self):
        txt = ""
        print('Guess the word! HINT: word is a name of a fruit');
        for i in range(len(self.word)): txt += " _ "
        print(txt)
        for i in range(len(self.word)): self.hyphenLower.append("_");


        while True:
            if self.max_attemps == self.num_attemps:
                print("You over time guess word! You lose");
                print("The word was: ", self.word)

                break;

            if "".join(self.hyphenLower) == self.word:
                print("Congratulations, You won!");
                break;
    
            if len(self.guessLetter) > 1: 
                print("Please guess word is one letter!!")

            self.hyphen_letter();


if __name__ == "__main__":
    obj = HangMan();
    obj.play();