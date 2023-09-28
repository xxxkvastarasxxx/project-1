from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (330, 550)

class MyApp(MDApp):
    title = 'Imperium Roma'
    pass

if __name__ == '__main__':
    MyApp().run()