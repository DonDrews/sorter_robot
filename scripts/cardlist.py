import threading
import hashlib
import json

#an instance of a card
#TODO: can add more properties later
class Card(dict):
    def __init__(self, n, s):
        super().__init__(name=n, set=s)

#Keeps track of the cards already scanned, and stores a sessionid to ensure clients
#are requesting delta updates from the correct state
#Contains an internal mutex for asynchronous reads and writes
class CardList:
    def __init__(self):
        self.mutex = threading.Lock()
        self.cards = []
        self.session_id = 0

    #blocking function called from robot side
    def add_card(self, n, s):
        self.mutex.acquire()
        self.cards.append(Card(n, s))
        self.mutex.release()

    #blocking function called from http requests
    #returns json text of all cards this index and newer
    #if index is invalid (wrong session), returns all cards along with a was_reset flag
    def get_cards_since(self, index):
        self.mutex.acquire()
        if index > self.session_id and index < self.session_id + len(self.cards):
            j = json.dumps({ \
                "cards" : self.cards[index - self.session_id:len(self.cards)], \
                "was_reset" : False, \
                "session_head" : self.session_id + len(self.cards) - 1})
        else:
            j = json.dumps({
                "cards" : self.cards, \
                "was_reset" : True, \
                "session_head" : self.session_id + len(self.cards) - 1})

        self.mutex.release()
        return j

    #resets the scanned cards and assigns a new session_id
    def do_reset(self):
        self.mutex.acquire()
        self.session_id = self.session_id + len(self.cards) + 100 #easier to see for testing
        self.cards = []
        self.mutex.release()
