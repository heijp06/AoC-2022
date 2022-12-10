class Device:
    def __init__(self) -> None:
        self.x_register = 1
        self.cycle = 1
        self.sum_of_signal_strengths = 0
        self.crt = [" " * 40 for _ in range(6)]

    def execute(self, instructions: list[str]) -> None:
        for instruction in instructions:
            match instruction.split():
                case ["noop"]:
                    self.tick()
                case ["addx", value]:
                    self.tick()
                    self.tick()
                    self.x_register += int(value)

    def tick(self) -> None:
        if self.cycle % 40 == 20:
            self.sum_of_signal_strengths += self.cycle * self.x_register
        self.draw()
        self.cycle += 1

    def draw(self) -> None:
        index = self.cycle - 1
        row = index // 40
        column = index % 40
        pixel = "#" if abs(self.x_register - column) < 2 else "."
        self.draw_pixel(pixel, row, column)

    def draw_pixel(self, pixel, row, column):
        self.crt[row] = self.crt[row][:column] + pixel + self.crt[row][column + 1:]
