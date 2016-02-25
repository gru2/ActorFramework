""" Actor """

AS_NOT_READY = "NOT_READY"
AS_READY = "READY"
AS_FINISHED = "FINISHED"

class Actor:

    def __init__(self):
        self.inbox = []
        self.state = AS_NOT_READY
        self.framework = None

    # Put a new message in the inbox.
    def receive(self, message):
        if self.state == AS_FINISHED:
            return
        self.inbox.append(message)
        self.state = AS_READY

    # Does a single chunk of work.
    # Returns True if there is no more work to do - all messages are processed
    # and the inbox is empty.
    def step(self):
        return True
