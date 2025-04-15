import unittest
from main import main


class TestChess(unittest.TestCase):
    def test_simple(self):
        n = 8
        r_start, c_start = 7, 0
        r_end, c_end = 0, 7
        ans = 6
        with open('input.txt', 'w') as file:
            file.write(str(n)+'\n')
            file.write(str(r_start)+', '+str(c_start)+'\n')
            file.write(str(r_end)+', '+str(c_end)+'\n')
        main()
        with open('output.txt', 'r') as file:
            length = int(file.readline().split()[0])
            self.assertEqual(length, ans)


if __name__ == "__main__":
    unittest.main()
