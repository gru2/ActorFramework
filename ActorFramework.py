""" ActorFramework """


class ActorFramework:

    def __init__(self):
        self.actors = []
        self.actorIndex = 0
        self.moreWorkRequired = True

    def step(self):
        if self.actorIndex >= len(self.actors):
            self.actorIndex = 0
            if self.moreWorkRequired:
                return True
            self.moreWorkRequired = True
        actor = self.actors[self.actorIndex]
        r = actor.step()
        if actor.finished:
            del self.actors[self.actorIndex]
        else:
            self.actorIndex += 1
            if not r:
                self.moreWorkRequired = False
        return r

    def steps(self, numberOfSteps):
        count = 0
        while True:
            r = self.step()
            count += 1
            if r:
                return True
            if count == numberOfSteps:
                return False

    def run(self):
        count = 0
        while True:
            r = self.step()
            count += 1
            if r:
                return True

    def addActor(self, actor):
        self.actors.append(actor)

