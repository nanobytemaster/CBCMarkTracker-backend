from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu


class ClassSelectionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDBoxLayout(
            orientation='vertical',
            padding=40,
            spacing=30,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=300
        )

        label = MDLabel(
            text="Select Class",
            halign="center",
            font_style="H5"
        )

        # Sample class list
        self.class_list = ['Grade 7', 'Grade 8', 'Grade 9']

        # Dropdown setup
        self.menu_items = [
            {
                "text": class_name,
                "on_release": lambda x=class_name: self.set_class(x)
            }
            for class_name in self.class_list
        ]
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4
        )

        self.class_button = MDRaisedButton(
            text="Choose Class",
            pos_hint={"center_x": 0.5},
            on_release=self.open_menu
        )
        
        proceed_button = MDRaisedButton(
            text="Proceed",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_entry)

        self.layout.add_widget(label)
        self.layout.add_widget(self.class_button)
        self.layout.add_widget(proceed_button)

        self.add_widget(self.layout)
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu


class ClassSelectionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDBoxLayout(
            orientation='vertical',
            padding=40,
            spacing=30,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=300
        )

        label = MDLabel(
            text="Select Class",
            halign="center",
            font_style="H5"
        )

        # Sample class list
        self.class_list = ['Grade 7', 'Grade 8', 'Grade 9']

        # Dropdown setup
        self.menu_items = [
            {
                "text": class_name,
                "on_release": lambda x=class_name: self.set_class(x)
            }
            for class_name in self.class_list
        ]
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4
        )

        self.class_button = MDRaisedButton(
            text="Choose Class",
            pos_hint={"center_x": 0.5},
            on_release=self.open_menu
        )

        proceed_button = MDRaisedButton(
            text="Proceed",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_entry
        )

        self.layout.add_widget(label)
        self.layout.add_widget(self.class_button)
        self.layout.add_widget(proceed_button)

from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu


class ClassSelectionScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = MDBoxLayout(
            orientation='vertical',padding=40,
            spacing=30,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.8, None),
            height=300
        )

        label = MDLabel(
            text="Select Class",
            halign="center",
            font_style="H5"
        )
        self.class_list = ['Grade 7', 'Grade 8', 'Grade 9']

        # Dropdown setup
        self.menu_items = [
            {
                "text": class_name,
                "on_release": lambda x=class_name: self.set_class(x)
            }
            for class_name in self.class_list
        ]
        self.menu = MDDropdownMenu(
            caller=None,
            items=self.menu_items,
            width_mult=4
        )

        self.class_button = MDRaisedButton(
            text="Choose Class",
            pos_hint={"center_x": 0.5},
            on_release=self.open_menu)
        proceed_button = MDRaisedButton(
            text="Proceed",
            pos_hint={"center_x": 0.5},
            on_release=self.go_to_entry
        )

        self.layout.add_widget(label)
        self.layout.add_widget(self.class_button)
        self.layout.add_widget(proceed_button)

        self.add_widget(self.layout) 
    
    def open_menu(self, instance):
        self.menu.caller = instance
        self.menu.open()

    def set_class(self, class_name):
        self.class_button.text = class_name
        self.menu.dismiss()

    def go_to_entry(self, instance):
        if self.class_button.text != "Choose Class":
            # Later, we can store selected class in app state
            self.manager.current = 'learner_entry'
