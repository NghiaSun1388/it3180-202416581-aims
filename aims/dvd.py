# TODO: implement search by title.
class DigitalVideoDisc:
    """Một đĩa DVD trong cửa hàng AIMS."""

    def __init__(self, title, category="", director="", length=0, cost=0.0):
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = cost

    def __str__(self):
        return (f"DVD - {self.title} - {self.category} - "
                f"{self.director} - {self.length}: {self.cost:.2f} $")


def search_by_title(dvds, title):
    """Tìm kiếm DVD theo tiêu đề (Không phân biệt chữ hoa / chữ thường)."""
    keyword = title.lower().strip()
    return [dvd for dvd in dvds if keyword in dvd.title.lower()]