class Controls:
    def __init__(self):
        self.valid = [100, 119, 115, 97]
        self.x, self.y = 10, 0
        self.prev_ = [-10, 0]

    def get_next(self, key):
        if key not in self.valid:
            return

        controls_ = {
            119: [0, -10], #Up
            115: [0, 10], #Down
            97: [-10, 0], #left
            100: [10, 0] #Right
        }

        prev_ = {
            119: [0, 10], #Up
            115: [0, -10], #Down
            97: [10, 0], #left
            100: [-10, 0] #Right
        }

        if self.prev_ == controls_[key]:
            return

        self.prev_ = prev_[key]
        self.x, self.y = controls_[key]
