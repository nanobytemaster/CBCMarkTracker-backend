from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

from screens.login_screen import LoginScreen
from screens.class_selection import ClassSelectionScreen
from screens.learner_entry import LearnerEntryScreen  # leave for later


class CBCMarkApp(MDApp):
    def build(self):
        sm = MDScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(ClassSelectionScreen(name="class_selection"))
        sm.add_widget(LearnerEntryScreen(name="learner_entry"))  # dummy for now
        return sm


if __name__ == '__main__':
    CBCMarkApp().run()

