class Youtube:
    def __init__(self, username, subcribers=0, subscriptions=0):
        self.username = username
        self.subcribers = subcribers
        self.subscriptions = subscriptions

    def subcribe(self, user):
        user.subscribers += 1
        self.subscriptions +=1