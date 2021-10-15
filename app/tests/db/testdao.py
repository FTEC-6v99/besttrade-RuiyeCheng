import unittest
import app.src.db.dao as dao

class Testdao(unittest.TestCase):
    def test_select_investors(self):
        investors = dao.get_all_investor()
        for investor in investors:
            print(investor.name)
        self.assertEquals(2,len(investors))
        