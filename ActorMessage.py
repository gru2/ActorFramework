""" ActorMessage """

AMT_NONE = "NONE"
AMT_QUIT = "QUIT"
AMT_REQUEST = "REQUEST"
AMT_REPLY = "REPLY"


class ActorMessage:

    def __init__(self):
        self.type = AMT_NONE
        self.sender = None
        self.data = None
