class Controls:
    def __init__(self):
        self.controls_ = {
            119: [0, -10], #Up
            115: [0, 10], #Down
            97: [-10, 0], #left
            100: [10, 0] #Right
        }

        self.prev_ = {
            119: [0, 10], #Up
            115: [0, -10], #Down
            97: [10, 0], #left
            100: [-10, 0] #Right
        }

        self.x = 10
        self.y = 0

    def get_next(self, key):
        if key not in self.controls_:
            return
        self.x, self.y = self.controls_[key]
