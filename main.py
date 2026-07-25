from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class JarvisApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        label = Label(
            text="नमस्ते 🙏\nमैं Deepak Sir द्वारा बनाया गया Jarvis हूँ 🤖",
            font_size=24
        )

        button = Button(
            text="Hello Jarvis",
            font_size=20
        )

        layout.add_widget(label)
        layout.add_widget(button)

        return layout

JarvisApp().run()
