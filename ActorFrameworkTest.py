#!/usr/bin/env python2

""" Unittest class ActorFramework. """

import ActorFramework
import Actor
import unittest


class TestActor01(Actor.Actor):

    def __init__(self):
        Actor.Actor.__init__(self)
        self.counter = 0

    def step(self):
        self.counter += 1
        if self.counter == 3:
            return True
        return False


class ActorFrameworkTest(unittest.TestCase):

    def test01(self):
        fw = ActorFramework.ActorFramework()
        fw.addActor(TestActor01())
        r = fw.step()
        self.assertEqual(r, False)
        r = fw.step()
        self.assertEqual(r, False)
        r = fw.step()
        self.assertEqual(r, True)


if __name__ == '__main__':
    unittest.main()

