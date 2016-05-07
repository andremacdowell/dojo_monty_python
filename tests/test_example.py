import unittest
import coelhos_controller

class TestExample(unittest.TestCase):
    
    #def __init__(self):
        #self.coelhosController = None
        
    def setUp(self):
        self.coelhosController = coelhos_controller.CoelhosController()
        #self.coelhosController.coelhos = [(1,2),(2,3),(3,2),(1,1),(5,7)]
        
    def test_raise_if_no_coelhos(self):
        self.assertRaises(Exception,coelhos_controller.CoelhosController().run)

    def test_must_return_0(self):
        coelhos = [[1,2]]
        result  = self.coelhosController.run(coelhos)
        self.assertEqual(0, result) 
       
    def test_calc_multa_empty(self):
        result = self.coelhosController.calc_multa([])
        self.assertEqual(0, result)
        
    def test_calc_multa(self):
        coelhos = [[2, 3], [2, 3]]
        result = self.coelhosController.calc_multa(coelhos)
        self.assertEqual(6, result)
        
    def test_calc_multa_coelho(self):
        coelho = [2, 2]
        result = self.coelhosController.calc_multa_coelho(coelho)
        self.assertEqual(2, result)
        
    def test_decision_coelho(self):
        coelhos = [[2, 2]]
        result = self.coelhosController.decision(coelhos)
        self.assertEqual(coelhos[0], result)
        
    def test_decision_coelhos(self):
        coelhos = [[2,2], [1,1000]]
        result = self.coelhosController.decision(coelhos)
        self.assertEqual(coelhos[1], result)
        
    def test_decision_coelhos_difficult(self):
        coelhos = [[2,2], [1,100], [500,10]]
        result = self.coelhosController.decision(coelhos)
        self.assertEqual(coelhos[1], result)
        
    def test_validation1(self):
        coelhos = [[2, 8], [2, 10]]
        result = self.coelhosController.run(coelhos)
        self.assertEqual(10, result)
        
    def test_validation2(self):
        coelhos = [[4,1],[3,4],[1,1000],[2,2],[5,6]]
        result = self.coelhosController.run(coelhos)
        self.assertEqual(2060, result)
        
        
# 4 1
# 3 4
# 1 1000
# 2 2
# 5 6