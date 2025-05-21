from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from database import db_handler
from database.db_handler import get_learners_by_grade, save_mark
from kivymd.uix.spinner import MDSpinner
import requests

class LearnerEntryScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_grade = "Grade 7"  # Default grade
        self.learners = []


        self.layout = MDBoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.9, None)
        )
        self.add_widget(self.layout)

        self.main_layout = MDBoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )
        self.add_widget(self.main_layout)

        self.grade_menu = MDDropdownMenu(
            caller=None,
            items=[
                {"text": grade, "on_release": lambda x=grade: self.set_grade(x)}
                for grade in ['Grade 7', 'Grade 8', 'Grade 9']
            ],
            width_mult=4
        )

        self.grade_button = MDRaisedButton(
            text=self.selected_grade,
            on_release=self.open_grade_menu,
            pos_hint={"center_x": 0.5}
        )
        self.main_layout.add_widget(self.grade_button)

        self.refresh_button = MDRaisedButton(
            text="Load Learners",
            on_release=self.load_learners,
            pos_hint={"center_x": 0.5}
        )
        self.main_layout.add_widget(self.refresh_button)
        self.subjects = ['Math', 'English', 'Kiswahili', 'Science', 'Social Studies']

        self.spinner = MDSpinner(size_hint=(None, None), size=(46, 46), pos_hint={"center_x": 0.5})
        self.main_layout.add_widget(self.spinner)
        self.spinner.active = False
        


        self.subject_menu_items = [
            {
                 "text": subject,
                 "on_release": lambda x=subject: self.set_subject(x),
             } for subject in self.subjects
        ]

        self.subject_menu = MDDropdownMenu(
            caller=None,  # will be set later
            items=self.subject_menu_items,
            width_mult=3
        )

        self.subject_button = MDRaisedButton(
            text="Select Subject",
            pos_hint={"center_x": 0.5},
            on_release=self.open_subject_menu
        )
        self.layout.add_widget(self.subject_button)


        self.learner_widgets = []

    def set_subject(self, subject_name):
        self.selected_subject = subject_name
        self.subject_button.text = subject_name
        self.subject_menu.dismiss()

    def open_subject_menu(self, instance):
        self.subject_menu.caller = instance
        self.subject_menu.open()
    def open_grade_menu(self, instance):
        self.grade_menu.caller = instance
        self.grade_menu.open()
    def set_grade(self, grade):
        self.selected_grade = grade
        self.grade_button.text = grade
        self.grade_menu.dismiss()
    def load_learners(self, instance):
        self.spinner.active = True
        self.clear_learner_entries()
        self.learners = get_learners_by_grade(self.selected_grade)
        if not self.learners:
            toast("No learners found for this grade.")
        for learner in self.learners:
            admission_no, name = learner
            learner_box = MDBoxLayout(orientation="horizontal", spacing=10)
            learner_label = MDLabel(text=f"{admission_no} - {name}", halign="left", size_hint_x=0.6)
            score_input = MDTextField(hint_text="Enter mark", input_filter="int", size_hint_x=0.4)
            learner_box.add_widget(learner_label)
            learner_box.add_widget(score_input)
            self.learner_widgets.append((admission_no, score_input))
            self.main_layout.add_widget(learner_box)
        self.main_layout.add_widget(self.submit_button())
        self.spinner.active = False
    def clear_learner_entries(self):
        for child in self.main_layout.children[:]:
            if isinstance(child, MDBoxLayout) and len(child.children) == 2:
                self.main_layout.remove_widget(child)
        self.learner_widgets.clear()

    def submit_button(self):
        return MDRaisedButton(
            text="Submit Marks",
            on_release=self.save_marks,
            pos_hint={"center_x": 0.5}
        )
    def save_marks(self, instance):
        for admission_no, input_widget in self.learner_widgets:
            score_text = input_widget.text
            if score_text:
                try:
                    score = int(score_text)
                    save_mark(admission_no, "Mathematics", score)
                except ValueError:
                    toast(f"Invalid mark for {admission_no}")
        toast("Marks saved successfully.")
    def submit_marks_to_server(self, admission_no, subject, marks):
        url = "http://172.26.104.235:5000/submit_marks"  # Replace with your PC’s IP address on the LAN
        data = {
            "admission_no": admission_no,
            "subject": subject,
            "marks": marks
        }

        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print("✅ Marks submitted successfully")
            else:
                print("❌ Failed to submit marks:", response.json())
        except Exception as e:
            print("🚫 Error sending marks:", e)

        

