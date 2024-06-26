import arcade

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = ''


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT,WINDOW_TITLE)



def main():
    window = MyGame()
    arcade.run()



if __name__ == '__main__':
    main()
