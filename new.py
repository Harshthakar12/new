import turtle, math, time, random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Glowing Heart Animation ❤️")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Text turtle
text_t = turtle.Turtle()
text_t.hideturtle()
text_t.color("white")

# Heart equations
def heart_x(t): return 16 * (math.sin(t) ** 3)
def heart_y(t): return 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)

# Draw heart outline
def draw_heart(scale, color, pensize):
    t.color(color)
    t.pensize(pensize)
    for angle in range(0, 360, 2):   # smaller steps → smoother heart
        t.penup()
        t.goto(0, 0)
        t.pendown()
        rad = math.radians(angle)
        x = heart_x(rad) * scale
        y = heart_y(rad) * scale
        t.goto(x, y)

# Draw sparkles around heart
def draw_sparkles():
    sparkle = turtle.Turtle()
    sparkle.hideturtle()
    sparkle.speed(0)
    sparkle.penup()
    for _ in range(8):  # few sparkles each frame
        angle = random.uniform(0, 2*math.pi)
        radius = random.uniform(180, 230)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        sparkle.goto(x, y)
        sparkle.dot(random.randint(2,5), random.choice(["white", "#ffcccc", "#ffe6e6"]))

# Display text below heart
def show_text(message, size, color):
    text_t.clear()
    text_t.color(color)
    text_t.penup()
    text_t.goto(0, -200)  # slightly below heart center
    text_t.write(message, align="center", font=("Arial", size, "bold"))

# Colors for glowing effect
colors = ["#ff4d4d", "#ff1a1a", "#ff3333", "#ff6666", "#ff8080"]
text_colors = ["#ffffff", "#ffe6e6", "#ffcccc", "#ff9999"]

# Animation loop
while True:
    for size in range(15, 25, 2):   # expand
        draw_heart(size, colors[size % len(colors)], 2)
        draw_sparkles()
        show_text("For You Visha ❤️ ", 24, text_colors[size % len(text_colors)])
        time.sleep(0.1)
        t.clear()
    for size in range(25, 15, -2):  # shrink
        draw_heart(size, colors[size % len(colors)], 2)
        draw_sparkles()
        show_text("For You Visha ❤️", 24, text_colors[size % len(text_colors)])
        time.sleep(0.1)
        t.clear()
