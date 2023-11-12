import os
import random
import keyboard

class PacManGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pacman = {'x': width // 2, 'y': height // 2}
        self.ghost = {'x': random.randint(0, width - 1), 'y': random.randint(0, height - 1)}
        self.score = 0
        self.game_over = False

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                if x == self.pacman['x'] and y == self.pacman['y']:
                    print('P', end=' ')
                elif x == self.ghost['x'] and y == self.ghost['y']:
                    print('G', end=' ')
                else:
                    print('.', end=' ')
            print()
        print(f"Score: {self.score}")

    def move_pacman(self, direction):
        if direction == 'left' and self.pacman['x'] > 0:
            self.pacman['x'] -= 1
        elif direction == 'right' and self.pacman['x'] < self.width - 1:
            self.pacman['x'] += 1
        elif direction == 'up' and self.pacman['y'] > 0:
            self.pacman['y'] -= 1
        elif direction == 'down' and self.pacman['y'] < self.height - 1:
            self.pacman['y'] += 1

    def move_ghost(self):
        if self.ghost['x'] < self.pacman['x']:
            self.ghost['x'] += 1
        elif self.ghost['x'] > self.pacman['x']:
            self.ghost['x'] -= 1

        if self.ghost['y'] < self.pacman['y']:
            self.ghost['y'] += 1
        elif self.ghost['y'] > self.pacman['y']:
            self.ghost['y'] -= 1

    def check_collision(self):
        if self.pacman['x'] == self.ghost['x'] and self.pacman['y'] == self.ghost['y']:
            self.game_over = True
            print("Game Over! Your final score:", self.score)

    def play(self):
        while not self.game_over:
            self.display()
            self.check_collision()
            self.move_ghost()

            key = keyboard.read_event(suppress=True).name
            if key in ['up', 'down', 'left', 'right']:
                self.move_pacman(key)
            elif key == 'esc':
                break

            self.score += 1

if __name__ == "__main__":
    game = PacManGame(10, 5)
    game.play()
