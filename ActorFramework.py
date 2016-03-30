""" ActorFramework """

import Actor


class ActorFramework:

    def __init__(self):
        self.actors = []
        self.actorIndex = 0
        self.stepsCount = 0

    def removeFinishedActors(self):
        pass

    def findNextReadyActor(self):
        if len(self.actors) == 0:
            return None

        n = len(self.actors)
        if self.actorIndex >= n:
            self.actorIndex = 0

        i = 0
        while True:
            if i == n:
                return None
            actor = self.actors[self.actorIndex]
            self.actorIndex += 1
            if self.actorIndex >= n:
                self.actorIndex = 0
            if actor.state == Actor.AS_READY:
                return actor
            i += 1

    def step(self):
        self.stepsCount += 1
        actor = self.findNextReadyActor()
        if actor is None:
            return True
        actor.step()
        return False

    def steps(self, numberOfSteps):
        finalStepsCount = self.stepsCount + numberOfSteps
        while True:
            if self.stepsCount == finalStepsCount:
                return False
            r = self.step()
            if r:
                return True

    def run(self):
        while True:
            r = self.step()
            if r:
                return

    def addActor(self, actor):
        actor.framework = self
        self.actors.append(actor)

