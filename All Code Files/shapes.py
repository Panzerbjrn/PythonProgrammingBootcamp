class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    def get_area(self):
        return int(self.width) * int(self.height)