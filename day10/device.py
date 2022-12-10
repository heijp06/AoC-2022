class Device:
    def __init__(self) -> None:
        self.x_register = 1
        self.cycle = 1
        self.sum_of_signal_strengths = 0

    def execute(self, instructions: list[str]) -> None:
        for instruction in instructions:
            match instruction.split():
                case ["noop"]:
                    self.tick()
                case ["addx", value]:
                    self.tick()
                    self.tick()
                    self.x_register += int(value)

    def tick(self):
        if self.cycle % 40 == 20:
            self.sum_of_signal_strengths += self.cycle * self.x_register
        self.cycle += 1
