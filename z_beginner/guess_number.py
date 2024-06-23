import random

class GuessNumber():
    def __init__(self, begin, end):
        self.random = random.randrange(begin, end)
    
    def get_number(self):
        if self.number > self.random:
            print("Higher");
            self.show();
        elif self.number < self.random:
            print("Lower");
            self.show();
        else:
            print("You are lucky!")
            

    def set_number(self, val):
        self.number = val;
        
    def initData(self, val):
        self.set_number(val);
        self.get_number();

    def show(self):
        x = int(input("Enter you guess number: "));
        self.initData(x);

obj = GuessNumber(1, 10);
obj.show();