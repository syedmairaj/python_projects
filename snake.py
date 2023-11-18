import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("400x400")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"

        self.food = self.create_food()

        self.master.bind("<Key>", self.change_direction)

        self.update()

    def create_food(self):
        x = random.randint(1, 19) * 20
        y = random.randint(1, 19) * 20
        self.food_item = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="red")
        return x, y

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and not self.direction == "Down":
            self.direction = "Up"
        elif key == "Down" and not self.direction == "Up":
            self.direction = "Down"
        elif key == "Left" and not self.direction == "Right":
            self.direction = "Left"
        elif key == "Right" and not self.direction == "Left":
            self.direction = "Right"

    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= 20 
        elif self.direction == "Down":
            y += 20
        elif self.direction == "Left":
            x -= 20
        elif self.direction == "Right":
            x += 20

        self.snake.insert(0, (x, y))

        if x == self.food[0] and y == self.food[1]:
            self.canvas.delete(self.food_item)
            self.food = self.create_food()
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

    def check_collision(self):
        x, y = self.snake[0]
        if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in self.snake[1:]:
            return True
        return False

    def update(self):
        if not self.check_collision():
            self.move()
            self.draw()
            self.master.after(100, self.update)
        else:
            self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Helvetica", 16))

    def draw(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")

        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + 20, self.food[1] + 20, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
