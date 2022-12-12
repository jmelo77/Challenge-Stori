import unittest
import os

class FunctionTest(unittest.TestCase):

    def test_file_exist(self):
        file_exists = os.path.exists('txns.csv')
        self.assertTrue(file_exists)
        
    def test_file_is_not_empty(self):
        file_size = os.path.getsize('txns.csv')
        assert file_size > 0
    
    def test_calculate_total_balance(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]
        totalBalance = self.calculate_totals(debitAmounts, creditAmounts)[0]

        assert totalBalance == 3

    def test_calculate_debit_average(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]        
        debitAverage = self.calculate_totals(debitAmounts, creditAmounts)[1] 
        
        assert debitAverage == -2.0

    def test_calculate_debit_average(self):
        debitAmounts = [-1,-3]
        creditAmounts = [2,5]        
        creditAverage = self.calculate_totals(debitAmounts, creditAmounts)[2] 
        print(creditAverage)
        assert creditAverage == 3.5

    def calculate_totals(self, debitAmounts, creditAmounts):
        global debitAverage
        debitAverage = 0
        debitTotal = 0
        debitCount = 0

        global creditAverage
        creditAverage = 0
        creditTotal = 0
        creditCount = 0
        totalBalance = 0

        for debitAmount in debitAmounts:
            totalBalance += debitAmount
            debitTotal += debitAmount
            debitCount = debitCount + 1

        for creditAmount in creditAmounts:
            totalBalance += creditAmount
            creditTotal += creditAmount
            creditCount = creditCount + 1

        debitAverage = debitTotal / debitCount
        creditAverage = creditTotal / creditCount

        return [totalBalance, debitAverage, creditAverage]
    
        
if __name__ == '__main__':
    unittest.main()
