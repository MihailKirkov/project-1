from multiprocessing import freeze_support
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os
from os import path
from zipfile import ZipFile
from shutil import copyfileobj
from bokeh.plotting import figure, output_file, show
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
import time
import sys
from pyicloud import PyiCloudService
import shutil


freeze_support()

class childApp(BoxLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__()
        self.orientation = 'vertical'
        self.cols = 2
        self.add_widget(Label(text = 'Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text = 'Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text = 'Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.button1 = Button(text = 'Save')
        self.button1.bind(on_press = self.save)
        self.add_widget(self.button1)
    
    def save(self, instance):
        print("Name of Student is " + self.s_name.text)
        print("Marks of Student is " + self.s_marks.text)
        print("Gender of Student is " + self.s_gender.text)
        print()


        


class parentApp(App):
    def build(self):
        return childApp()


if __name__=="__main__":
    parentApp().run()
