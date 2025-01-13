from windows import *

def main():
    win = Window(800, 600)
    l = Line(Point(20, 20), Point(200, 200))
    l2 = Line(Point(200, 200), Point(500, 500))
    win.draw_line(l, "black")
    win.draw_line(l2, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()