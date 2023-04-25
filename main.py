from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_string('''
<Button>
    size_hint: (0.2,0.2)
    background_normal: ""
    background_color: (2/255,10/255,24/255)


<CalculatorWidget>
    BoxLayout:
        orientation: "vertical"
        size: root.width, root.height

        TextInput:
            id: input_box
            text: "0"
            font_size: 43
            multiline: False
            halign: "right"
            size_hint: (1,0.19)
            background_color:(1,1,1,1)

        GridLayout:
            cols: 4
            rows: 5

            #### row 1 ####

            Button:
                text:"%"
                font_size: 32
                on_press: root.signs("%")
            Button:
                text:"C"
                font_size: 32
                on_press: root.clear()

            Button:
                text:u"\u00AB"
                font_size: 32
                on_press: root.remove_last()
            Button:
                text:"/"
                font_size: 32
                background_color:(14/255,73/255,176/255,1)
                on_press: root.signs("/")

            #### row 2 ####
            Button:
                text:"7"
                font_size: 32
                on_press: root.button_value(7)
            Button:
                text:"8"
                font_size: 32
                on_press: root.button_value(8)
            Button:
                text:"9"
                font_size: 32
                on_press: root.button_value(9)
            Button:
                text:"X"
                font_size: 32
                background_color:(14/255,73/255,176/255,1)
                on_press: root.signs("*")

            #### row 3 ####

            Button:
                text:"4"
                font_size: 32
                on_press: root.button_value(4)
            Button:
                text:"5"
                font_size: 32
                on_press: root.button_value(5)
            Button:
                text:"6"
                font_size: 32
                on_press: root.button_value(6)
            Button:
                text:"-"
                font_size: 32
                background_color:(14/255,73/255,176/255,1)
                on_press: root.signs("-")


            #### row 4 ####

            Button:
                text:"1"
                font_size: 32
                on_press: root.button_value(1)
            Button:
                text:"2"
                font_size: 32
                on_press: root.button_value(2)
            Button:
                text:"3"
                font_size: 32
                on_press: root.button_value(3)
            Button:
                text:"+"
                font_size: 32
                background_color:(14/255,73/255,176/255,1)
                on_press: root.signs("+")

            #### row 5 ####

            Button:
                text:"+/-"
                font_size: 32
                on_press: root.positive_negative()
            Button:
                text:"0"
                font_size: 32
                on_press: root.button_value(0)
            Button:
                text:"."
                font_size: 32
                on_press: root.dot()
            Button:
                text:"="
                font_size: 32
                background_color:(1,0,0,1)
                on_press: root.results()
''')

class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input_box.text= "0"

    def button_value(self,number):
        prev_number=self.ids.input_box.text

        if "Wrong Equation" in prev_number:
            prev_number=" "

        if prev_number == "0":
            self.ids.input_box.text=""
            self.ids.input_box.text = f"{number}"
        else:
            self.ids.input_box.text=f"{prev_number}{number}"

    def remove_last(self):
        prev_number=self.ids.input_box.text
        prev_number=prev_number[:-1]
        self.ids.input_box.text=prev_number

    def signs(self,sign):
        prev_number=self.ids.input_box.text
        if prev_number[-1]=="+" or prev_number[-1]=="-" or prev_number[-1]=="*" or prev_number[-1]=="/" :
            self.ids.input_box.text=prev_number
        else:
            self.ids.input_box.text=f"{prev_number}{sign}"

    def results(self):
        prev_number=self.ids.input_box.text
        try:
            result=eval(prev_number)
            self.ids.input_box.text=str(result)
        except:
            self.ids.input_box.text="Wrong Equation"

    def positive_negative(self):
        prev_number=self.ids.input_box.text

        if "-" in prev_number:
            self.ids.input_box.text=f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text=f"-{prev_number}"

    def dot(self):
        prev_number=self.ids.input_box.text
        num_list=re.split("\+|-|\*|/|%",prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1] :
            prev_number=f"{prev_number}."
            self.ids.input_box.text =prev_number

        elif "." in prev_number:
            pass
        else:
            prev_number=f"{prev_number}."
            self.ids.input_box.text =prev_number


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == "__main__":
    CalculatorApp().run()