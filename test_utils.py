import unittest

import utils


class TestStates(unittest.TestCase):
    def setUp(self):
        self.states = [
            utils.State('S1', [
                (1.0, 2.5),
                (12.5, 2.5),
                (11.8, 20.3),
                (5.3, 22.4),
                (3.0, 17.9),
                (0.3, 15.4),
            ]),
            utils.State('S2', [
                (4.3, -3.3),
                (6.0, -2.1),
                (7.1, -3.3),
                (6.2, 3.9),
                (5.1, 0.7),
                (4.9, 4.2),
                (1.0, 3.8),
            ])
        ]

    def test_contained(self):
        contained = [
            # Points contained in state 1
            [
                (3.0, 5.0),
                (5.3, 22.39),
                (5.2, 17.9),
                (2.9, 17.5),
            ],
            # Points contained in state 2
            [
                (4.3, -3.2),
                (4.2, 2.0),
                (6.2, 0.0),
            ]
        ]
        for state, state_points in zip(self.states, contained):
            for point in state_points:
                print point
                self.assertTrue(state.contains(*point))

    def test_not_contained(self):
        not_contained = [
            # Points not contained in state 1
            [
                (0.9, 2.5),
                (1.1, 2.2),
                (0.0, 0.0),
                (11.9, 20.3),
                (12.9, 20.4),
                (12.9, 10.0),
            ],
            # Points not contained in state 2
            [
                (0.0, 0.0),
                (1.0, 3.6),
            ]
        ]
        for state, state_points in zip(self.states, not_contained):
            for point in state_points:
                self.assertFalse(state.contains(*point))


if __name__ == "__main__":
    unittest.main()
