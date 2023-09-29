import unittest
from game import Job, FirstJob, SecondJob


class TestPlayer(unittest.TestCase):
    def test_player_str(self):
        # Test that the __str__ method returns the expected string
        player1 = Job(FirstJob.KING, SecondJob.SPADE)
        self.assertEqual(str(player1), "King♠")

        player2 = Job(FirstJob.JOKER, SecondJob.CLUB)
        self.assertEqual(str(player2), "Joker")

    def test_all_jobs(self):
        jobs = Job.all_jobs()
        self.assertTrue(len(jobs) == 13)

    def test_counter_by(self):
        # Test that the counter_by method returns the expected result for all job combinations
        player1 = Job(FirstJob.KING, SecondJob.SPADE)
        player2 = Job(FirstJob.QUEEN, SecondJob.HEART)
        player3 = Job(FirstJob.JACK, SecondJob.CLUB)

        expected = Job.all_jobs_of(FirstJob.JACK, SecondJob.all())
        expected.append(Job(FirstJob.JOKER, None))
        self.assertListEqual(expected, player1.counter_by())

        expected = Job.all_jobs_of(FirstJob.KING, SecondJob.all())
        expected = expected + Job.all_jobs_of(FirstJob.QUEEN, player2.second_job.counter_by())
        expected.append(Job(FirstJob.JOKER, None))
        self.assertListEqual(expected, player2.counter_by())

        expected = Job.all_jobs_of(FirstJob.QUEEN, SecondJob.all())
        expected = expected + Job.all_jobs_of(player3.first_job, player3.second_job.counter_by())
        expected.append(Job(FirstJob.JOKER, None))
        self.assertListEqual(expected, player3.counter_by())

    def test_is_counter(self):
        # Test that the is_counter method returns the expected result for all job combinations
        player1 = Job(FirstJob.KING, SecondJob.SPADE)
        player2 = Job(FirstJob.QUEEN, SecondJob.HEART)
        player3 = Job(FirstJob.JACK, SecondJob.CLUB)
        player4 = Job(FirstJob.KING, SecondJob.HEART)
        player5 = Job(FirstJob.KING, SecondJob.CLUB)
        player6 = Job(FirstJob.KING, SecondJob.DIAMOND)
        player7 = Job(FirstJob.QUEEN, SecondJob.CLUB)
        player8 = Job(FirstJob.JACK, SecondJob.DIAMOND)
        player9 = Job(FirstJob.JOKER, SecondJob.SPADE)

        self.assertTrue(player1.is_counter(player2))
        self.assertFalse(player2.is_counter(player1))

        self.assertTrue(player2.is_counter(player3))
        self.assertFalse(player3.is_counter(player2))

        self.assertTrue(player3.is_counter(player1))
        self.assertFalse(player1.is_counter(player3))

        self.assertTrue(player1.is_counter(player4))
        self.assertFalse(player4.is_counter(player1))

        self.assertTrue(player1.is_counter(player5))
        self.assertFalse(player5.is_counter(player1))

        self.assertTrue(player1.is_counter(player6))
        self.assertFalse(player6.is_counter(player1))

        self.assertTrue(player4.is_counter(player5))
        self.assertFalse(player5.is_counter(player4))

        self.assertTrue(player4.is_counter(player6))
        self.assertFalse(player6.is_counter(player4))

        self.assertTrue(player5.is_counter(player6))
        self.assertFalse(player6.is_counter(player5))

        self.assertTrue(player2.is_counter(player7))
        self.assertFalse(player7.is_counter(player2))

        self.assertTrue(player3.is_counter(player8))
        self.assertFalse(player8.is_counter(player3))

        self.assertTrue(player1.is_counter(player9))
        self.assertTrue(player2.is_counter(player9))
        self.assertTrue(player3.is_counter(player9))
        self.assertTrue(player9.is_counter(player1))
        self.assertTrue(player9.is_counter(player2))
        self.assertTrue(player9.is_counter(player3))


if __name__ == '__main__':
    unittest.main()
