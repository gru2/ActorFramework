""" Actor """


class Actor:

    def __init__(self):
        self.inbox = []
        self.finished = False
        self.framework = None

    # Put a new message in the inbox.
    def receive(self, message):
        self.inbox.append(message)

    # Does a single chunk of work.
    # Returns True if there is no more work to do - all messages are processed
    # and the inbox is empty.
    def step(self):
        return True
