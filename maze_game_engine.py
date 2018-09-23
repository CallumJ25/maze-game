class Map:
    def __init__(self, XCords, YCords):
        self.X = XCords
        self.Y = YCords
        self.YCords_list = []
        self.XCords_list = []
        for q in range (self.X):
            self.XCords_list.append(q)
            if q == (self.X - 1):
                break
        for q in range (self.Y):
            self.YCords_list.append(q)
            if q == (self.Y - 1)
                
