#!/usr/bin/env python3

""" Unittest class ActorFramework. """

import ActorFramework
import Actor
import unittest


class TestActor(Actor.Actor):

    def __init__(self, numberOfStepsToFinish):
        Actor.Actor.__init__(self)
        self.counter = 0
        self.numberOfStepsToFinish = numberOfStepsToFinish
        if numberOfStepsToFinish == 0:
            self.state = Actor.AS_NOT_READY
        else:
            self.state = Actor.AS_READY

    def step(self):
        self.counter += 1
        if self.counter == self.numberOfStepsToFinish:
            self.state = Actor.AS_NOT_READY
        else:
            self.state = Actor.AS_READY


class TestActorTest(unittest.TestCase):

    def test_init_ifNumberOfStepsIsZeroStateIsNotReady(self):

        actor = TestActor(0)

        self.assertEqual(actor.state, Actor.AS_NOT_READY)

    def test_init_ifNumberOfStepsIsOneStateIsReady(self):

        actor = TestActor(1)

        self.assertEqual(actor.state, Actor.AS_READY)

    def test_step_ifNumberOfStepsIsOneStateIsNotReadyAfterStep(self):
        actor = TestActor(1)

        actor.step()

        self.assertEqual(actor.state, Actor.AS_NOT_READY)

    def test_init_ifNumberOfStepsIsTwoStateIsReadyAfterStep(self):
        actor = TestActor(2)

        actor.step()

        self.assertEqual(actor.state, Actor.AS_READY)

    def test_init_ifNumberOfStepsIsTwoStateIsNotReadyAfterSecondStep(self):
        actor = TestActor(2)
        actor.step()

        actor.step()

        self.assertEqual(actor.state, Actor.AS_NOT_READY)


class ActorFrameworkTest(unittest.TestCase):

    def setUp(self):
        self.fw = ActorFramework.ActorFramework()

    def test_step_ifNoActorsRetunTrue(self):

        r = self.fw.step()

        self.assertTrue(r)

    def test_step_ifNumberOfStepsIsOneReturnFalse(self):
        numberOfSteps = 1
        self.fw.addActor(TestActor(numberOfSteps))

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifNumberOfStepsIsOneReturnTrueAfterSecondCall(self):
        numberOfSteps = 1
        self.fw.addActor(TestActor(numberOfSteps))
        self.fw.step()

        r = self.fw.step()

        self.assertTrue(r)

    def test_step_ifTwoActorsAreAddedAndNumberOfStepsIsOneReturnFalse(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(1))

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifTwoActorsAreAddedAndNumberOfStepsIsOneReturnFalseAfterSecondCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(1))
        self.fw.step()

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifTwoActorsAreAddedAndNumberOfStepsIsOneReturnTrueAfterThirdCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(1))
        self.fw.step()
        self.fw.step()

        r = self.fw.step()

        self.assertTrue(r)

    def test_step_stepsCountIsOneAfterCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.step()

        self.assertEqual(self.fw.stepsCount, 1)

    def test_step_stepsCountIsTwoAfterSecondCall(self):
        self.fw.addActor(TestActor(2))
        self.fw.step()

        self.fw.step()

        self.assertEqual(self.fw.stepsCount, 2)

    def test_step_ifThreeStepsAreRequiredReturnFalseAfterFirstCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(2))

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifThreeStepsAreRequiredReturnFalseAfterSecondCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(2))
        self.fw.step()

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifThreeStepsAreRequiredReturnFalseAfterThirdCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(2))
        self.fw.step()
        self.fw.step()

        r = self.fw.step()

        self.assertFalse(r)

    def test_step_ifThreeStepsAreRequiredReturnTrueAfterForthCall(self):
        self.fw.addActor(TestActor(1))
        self.fw.addActor(TestActor(2))
        self.fw.step()
        self.fw.step()
        self.fw.step()

        r = self.fw.step()

        self.assertTrue(r)

    def test_run_ifNoActorsStepsCountIsOne(self):

        self.fw.run()

        self.assertTrue(self.fw.stepsCount, 1)

    def test_run_ifOneStepIsRequiredStepsCountIsTwo(self):
        self.fw.addActor(TestActor(1))

        self.fw.run()

        self.assertTrue(self.fw.stepsCount, 2)

    def test_run_ifNStepsAreRequiredStepsCountIsNPlusOne(self):
        n1 = 6
        n2 = 9
        n = n1 + n2
        self.fw.addActor(TestActor(n1))
        self.fw.addActor(TestActor(n2))

        self.fw.run()

        self.assertTrue(self.fw.stepsCount, n + 1)

    def test_steps_ifNoActorsAndArgumentIsZeroReturnFalse(self):

        r = self.fw.steps(0)

        self.assertFalse(r)

    def test_steps_ifOneStepIsRequiredAndArgumentIsOneReturnFalse(self):
        self.fw.addActor(TestActor(1))

        r = self.fw.steps(1)

        self.assertFalse(r)

    def test_steps_ifOneStepIsRequiredAndArgumentIsTwoReturnTrue(self):
        self.fw.addActor(TestActor(1))

        r = self.fw.steps(2)

        self.assertTrue(r)


if __name__ == '__main__':
    unittest.main()

