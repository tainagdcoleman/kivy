import kivy
kivy.require('1.0.6')

from kivy.app import App
from kivy.uix.label import Label #holds the user interface elements
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout): # heritage is made like that

    #def build(self): #Root Widget
    #    return Label(text='Hello World')
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()


