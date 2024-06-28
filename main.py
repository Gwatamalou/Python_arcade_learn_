import arcade
import arcade.gui

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = 'P_Arcade'


class StartButton(arcade.gui.UIFlatButton):
        pass

class SettingsButton(arcade.gui.UIFlatButton):
    pass

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class Window(arcade.Window):
    def __init__(self, window_width = WINDOW_WIDTH, window_height = WINDOW_HEIGHT, window_title = WINDOW_TITLE):
        super().__init__(window_width, window_height, window_title)
        self.window = arcade.gui.UIManager()
        self.window.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)



class MyGame(Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.window = Window()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        self.b_v_box = arcade.gui.UIBoxLayout()

        start_button = StartButton(text='Start', width=200)
        self.b_v_box.add(start_button.with_space_around(bottom=20))

        settings_button = SettingsButton(text='Settings', width=200)
        self.b_v_box.add(settings_button.with_space_around(bottom=20))

        quit_button = QuitButton(text='Quit', width=200)
        self.b_v_box.add(quit_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.b_v_box))

    def on_draw(self):
        self.clear()
        self.manager.draw()


def main():
    window = MyGame()
    arcade.run()


if __name__ == '__main__':
    main()
