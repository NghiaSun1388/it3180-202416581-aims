import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_limit(self):
        cart = Cart()
        
        # Thêm 20 đĩa đầu tiên (phải thành công và trả về True)
        for i in range(20):
            dvd = DigitalVideoDisc(title=f"Test DVD {i+1}")
            result = cart.add_dvd(dvd)
            self.assertTrue(result, f"Không thể thêm đĩa thứ {i+1}")
        
        # Thử thêm đĩa thứ 21 (phải thất bại và trả về False)
        dvd_21 = DigitalVideoDisc(title="Test DVD 21")
        result_21 = cart.add_dvd(dvd_21)
        self.assertFalse(result_21, "Lỗi Bug: Giỏ hàng vẫn cho phép thêm đĩa thứ 21!")
    def test_total_cost_with_discount(self):
        cart = Cart()
        dvd = DigitalVideoDisc(title="Test DVD", cost=100.0)
        cart.add_dvd(dvd)
        # Với 100$, giảm 20% thì tổng tiền phải còn 80$
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
    def test_search_by_title_case_insensitive(self):
        results = search_by_title([DigitalVideoDisc('The Lion King')], 'lion')
        self.assertEqual(len(results), 1)
if __name__ == '__main__':
    unittest.main()

    