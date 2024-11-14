class Race:
    def __init__(self, friction):
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)

race = Race(0.1)

current_track = race