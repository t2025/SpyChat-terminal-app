from datetime import datetime
#Creating class spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#Creating class chatmessage to read chat history
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('John Terry', 'Mr.', 4.9, 27)
friend_two = Spy('David Hedison', 'Ms.', 4.39, 21)
friend_three = Spy('Watson', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]


