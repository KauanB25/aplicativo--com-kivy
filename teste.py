from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.label = Label(text="Texto inicial")
        self.add_widget(self.label)

        # Agendar uma atualização do texto do Label a cada 2 segundos
        Clock.schedule_interval(self.update_label, 2)

    def update_label(self, dt):
        # Atualizar o texto do Label
        self.label.text = "Texto atualizado"

class MyApp(MDApp):
    def build(self):
        return MyBoxLayout()

MyApp().run()