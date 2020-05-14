def make_division_by(n):
    def division(x):
        assert type(x) == int, 'Solo puedes dividir números'
        return x/n
    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def test_closure_make_division_by(self):
            division_by_2 = make_division_by(2)
            self.assertEqual(5, division_by_2(10))
    
    
    #unittest.main()
    run()
