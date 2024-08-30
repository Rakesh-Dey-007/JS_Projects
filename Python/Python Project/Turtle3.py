import turtle

tt = turtle.Turtle()

tt.screen.bgcolor("black")
tt.pensize(2)
tt.color("green")
tt.left(90)

tt.backward(100)
tt.speed(200)
tt.shape("turtle")

def tree(i):
    if i < 10:
        return
    else:
        tt.forward(i)
        tt.color("orange")
        tt.circle(2)
        tt.color("brown")
        tt.left(30)
        tree(3*i/4)
        tt.right(60)
        tree(3*i/4)
        tt.left(30)
        tt.backward(i)

tree(100)
turtle.done()
