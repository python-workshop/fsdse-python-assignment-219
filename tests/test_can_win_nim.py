from unittest import TestCase


class TestCan_win_nim(TestCase):
    def test_can_win_nim(self):
        try:
            from build import can_win_nim
        except ImportError:
            self.assertFalse("no function found")
        self.assertRaises(TypeError, can_win_nim, None)
        self.assertEqual(can_win_nim(1), True)
        self.assertEqual(can_win_nim(2), True)
        self.assertEqual(can_win_nim(3), True)
        self.assertEqual(can_win_nim(4), False)
        self.assertEqual(can_win_nim(7), True)
        self.assertEqual(can_win_nim(40), False)
