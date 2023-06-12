from calculator import Calculator, add, multiply

class TestSuitCalc:

    calc_obj = Calculator()

    def test_add(self):
        self.calc_obj.set_function(add)
        assert self.calc_obj.calc(4, 3) == 7
        assert self.calc_obj.calc(-5, -5) == -10
        assert self.calc_obj.calc(2.5, 2.5) == 5

    
    def test_multiply(self):
        self.calc_obj.set_function(multiply)
        assert self.calc_obj.calc(4, 3) == 12
        assert self.calc_obj.calc(5, -5) == -25
        assert self.calc_obj.calc(2, 2.5) == 5
        
