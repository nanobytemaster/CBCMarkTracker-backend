from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = MDBoxLayout(
            orientation='vertical',
            padding=40,
            spacing=30,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=400
        )

        title = MDLabel(
            text="CBC Mark Tracker",
            halign="center",
            font_style="H5"
        )

        self.username = MDTextField(
            hint_text="Username",
            size_hint_x=1
        )

        self.password = MDTextField(
            hint_text="Password",
            password=True,
            size_hint_x=1
        )

        login_button = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5},
            on_release=self.login_user
        )

        layout.add_widget(title)
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(login_button)

        self.add_widget(layout)

    def login_user(self, instance):
        self.manager.current = 'class_selection'


