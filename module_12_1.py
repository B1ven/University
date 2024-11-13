from Runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_run(self):
        r = Runner('Fred')
        for i in range(10):
            r.run()
        self.assertEquals(r.distance, 100)

    def test_walk(self):
        r = Runner('Garry')
        for i in range(10):
            r.walk()
        self.assertEquals(r.distance, 50)

    def test_challenge(self):
        r1 = Runner('Garry')
        r2 = Runner('Scotty')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEquals(r1.distance, r2.distance)


if __name__ == "__main__":
    unittest.main()

