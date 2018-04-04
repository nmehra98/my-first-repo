
#####class for storing details
from datetime import datetime
class Spy:
    def __init__(self, Name, Salutation, age, Rating):
        self.Name = Name
        self.Salutation = Salutation
        self.age = age
        self.Rating = Rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#####for an existing user
spy = Spy("Neeti", "Ms.", 21, 4.5)

#####existing friends
friend_one = Spy("Kriti", "Ms.", 21, 4.1)
friend_two = Spy("Jake", "Mr.", 21, 4.2)
friend_three = Spy("Ryan", "Mr.", 20, 4)

Friends = [friend_one, friend_two, friend_three]

#####chat class
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me