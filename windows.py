from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__painter = Canvas(self.__root, height=self.__height, width=self.__width)
        self.__painter.pack()
        self.__is_open = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_open = True
        while self.__is_open:
            self.redraw()
        
    def close(self):
        self.__is_open = False
    

def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()


