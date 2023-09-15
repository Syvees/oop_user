class User:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info (self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self
    
    def enroll (self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points (self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"Gold Card Points {self.gold_card_points}")
        else:
            print("Not enough points!")
        return self

harry = User ("Harry", "Potter", "harry.potter@gmail.com", 32) #User 1
hermione = User ("Hermione", "Granger", "hermione.grangerle@gmail.com", 36) #User 2
ron = User ("Ron", "Weasley", "ron.weasley@gmail.com", 30) #User 3

harry.display_info().enroll().spend_points(100).display_info().spend_points(150).display_info()



