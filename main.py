from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.clock import Clock


KV = """
ScreenManager:
    PreloaderScreen:
    MainScreen:

<PreloaderScreen>:
    name: "preloader"
    Image:
        source: "./assets/images/logo-cog.png"
        anim_delay: 0.1
        allow_stretch: True
        keep_ratio: True
        size_hint_y: None
        height: root.height
        width: root.width

<MainScreen>:
    name: "main"
    MDLabel:
        text: "Iniciar sesión"
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .5}
    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
        callback: app.callback
        pos_hint: {"right": 1, "bottom": 1}

"""


class PreloaderScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = {
            'Registrar maestro': 'account-plus',
        }

    def build(self):
        self.theme_cls.colors["primary"] = [0, 110, 182, 1]
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def on_start(self):
        self.root.current = "preloader"
        self.root.transition.direction = "left"
        self.root.transition.duration = 0.2
        self.root.transition.fade = True
        self.root.transition.sine_out = True
        self.root.transition.sine_in = True
        Clock.schedule_once(self.change_to_main, 2)  # Cambia a MainScreen después de 2 segundos

    def change_to_main(self, *args):
        self.root.current = "main"


    def callback(self, instance):
        self.dialog = MDDialog(
            title="Confirmation",
            text="Are you sure?",
            buttons=[
                MDFlatButton(
                    text="CANCEL", text_color=self.theme_cls.primary_color
                ),
                MDFlatButton(
                    text="ACCEPT", text_color=self.theme_cls.primary_color
                ),
            ],
        )
        self.dialog.open()


Test().run()
