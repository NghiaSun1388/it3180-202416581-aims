import unittest
from aims.dvd import DigitalVideoDisc, search_by_title

class TestSearch(unittest.TestCase):
    def test_search_by_title_case_insensitive(self):
        # 1. Tạo danh sách DVD mẫu
        dvds = [
            DigitalVideoDisc("The Lion King"),
            DigitalVideoDisc("Star Wars"),
            DigitalVideoDisc("Aladdin")
        ]
        
        # 2. Truyền đủ 2 tham số: danh sách dvds và từ khóa 'lion'
        results = search_by_title(dvds, "lion")
        
        # 3. Kiểm tra kết quả tìm thấy đúng 1 đĩa
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

if __name__ == '__main__':
    unittest.main()