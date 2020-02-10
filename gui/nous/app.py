# --- IMPORTS ---

# --- KIVY ---
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

# --- LOCAL ---
from heresy import www


# --- CONFIG ---



# --- APP ---

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        # --- GRID LAYOUT --- 
        self.cols = 2

        # --- URL LABEL ---
        self.add_widget(Label(text="URL"))

        # --- URL INPUT ---
        self.url = TextInput(multiline=False)
        self.add_widget(self.url)

        # --- BUTTON ---
        self.button = Button(text="Show")
        self.button.bind(on_press=self.show)
        self.add_widget(self.button)

        # --- OUTPUT ---
        self.output = Label()
        self.add_widget(self.output)

    def show(instance, value):
        url = instance.url.text

        try:
            urls = www.lsurl(url)
        except ValueError as error:
            output = str(error)
        else:
            output = "\n".join(urls)

        instance.output.text = output 


class NousApp(App):
    def build(self):
        return Screen()


# --- MAIN ---

if __name__ == "__main__":
    app = NousApp()
    app.run()
