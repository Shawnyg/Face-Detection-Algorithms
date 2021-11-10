from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

#Define different screens
class MainWindow(Screen):
    def spinner_clicked(self, value):
        self.ids.mainlabel_id.text = f'Selected algorithm: {value}'
        
class HelpWindow(Screen):
    pass

class SingleImageWindow(Screen):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass

class HaarWindow(Screen):
    pass



class RetinaWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('new_window.kv')

class Test(App):
    def build(self):
        self.title = "Face Detection Algorithms"
    #     self.window = GridLayout()
    #     self.window.cols = 1
    #     self.window.size_hint = (0.6, 0.7)
    #     self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
    #     #add widgets to window

    #     # image widget
    #     self.title = "Face Detection Algorithms"
    #     self.introMessage = Label(text="Choose an algorithm!")
    #     self.window.add_widget(self.introMessage)
    #     self.choice1 = Button(text="MTCNN")
    #     self.choice2 = Button(text="RetinaFace")
    #     self.choice3 = Button(text="Haar-cascade")

    #     self.choice1.bind(on_press=self.callback)
    #     self.choice2.bind(on_press=self.callback)
    #     self.choice3.bind(on_press=self.callback)


    #     self.window.add_widget(self.choice1)
    #     self.window.add_widget(self.choice2)
    #     self.window.add_widget(self.choice3)
        
    #     return self.window
        return kv
    # def callback(self, instance):
    #      self.introMessage.text = "Algorithm selected: " + instance.text
        

if __name__ == "__main__":
    Test().run()
