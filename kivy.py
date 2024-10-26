import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.clearcolor = (0.9,0.9,1,1)

class StartScreen(Screen):
    def init(self,**data):
        super().init(**data)
        layout = BoxLayout(orientation="vertical",padding=20, spacing=20)
        test_name = Label(text="ТЕСТ НА СЛАБОУМИЕ", font_size="80px", color=(0.9,0,0,1))
        test_info = Label(text="Это шуточный тест. Он не претендует на медецинскую точность\n"
                          "Пройдите тест, чтобы узнать свой результат",
                          font_size="30px",
                          color=(0,0,0,1),
                          halign="center")
        start_button = Button(text="Начать тест",
                              background_color=(0.5,1,0.5,1),
                              size_hint=(0.5,0.2),
                              pos_hint={'center_x': 0.5})
        start_button.bind(on_press=self.change_screen)
        layout.add_widget(test_name)
        layout.add_widget(test_info)
        layout.add_widget(start_button)
        self.add_widget(layout)

    def change_screen(self, instanse):
        app = App.get_running_app()
        app.screen_manager.current = 'question_0'

class QuestionScreen(Screen):
    def init(self,data,index,**kwargs):
        super().init(**kwargs)
        self.name = f'question_{index}'
        self.data = data
        self.index = index
        question_label = Label(text=data['question'],
                                font_size="40px",
                                color=(1,0,0,1),
                                halign="center")
        line = BoxLayout(orientation='vertical',padding=20, spacing=20)
        line.add_widget(question_label)
        for option in data['options']:
            button = Button(text=option['text'],
                            background_color=(0.5,0.5,1,1),
                            size_hint=(0.8,0.2),
                            pos_hint={'center_x': 0.5})
            button.bind(on_press = lambda instanse, option=option: self.check_answer(option))
            line.add_widget(button)
        self.add_widget(line)

    def check_answer(self,option):
        app = App.get_running_app()
        app.user_answers.append(option['correct'])
        if self.index < len(app.questions) - 1:
            app.screen_manager.current = f'question_{self.index + 1}'
        else:
            app.screen_manager.current = 'result'

class ResultScreen(Screen):
    def init(self, **kwargs):
        super().init(**kwargs)
        self.result_label = Label(text='', font_size='40px', color=(0,0,0,1))
        self.retry_button = Button(text="Попробовать снова",
                              background_color=(0.5,1,0.5,1),
                              size_hint=(0.8,0.2),
                              pos_hint={'center_x': 0.5})
        self.retry_button.bind(on_press=self.retry_test)
        self.layout = BoxLayout(orientation='vertical', padding=20 , spacing=20)
        self.layout.add_widget(self.result_label)
        self.layout.add_widget(self.retry_button)
        self.add_widget(self.layout)

    def on_enter(self):
        app = App.get_running_app()
        correct_answers = sum(app.user_answers)
        total_questions = len(app.questions)
        result = correct_answers/total_questions
        if result >= 0.90:
            text = 'Вы гений! Наверное . . .'
        elif result >= 0.5:
            text = 'Все в пределах нормы'
        else:
            text = 'Наверное вы сын Ивана Золо'
        self.result_label.text = f'Результат: {text}'
        
    def retry_test(self, instanse):
        app = App.get_running_app()
        self.user_answers = []
        app.screen_manager.current = 'start'

class TestApp(App):
    def build(self):
        with open('questions.json','r',encoding='utf-8') as file:
            self.questions = json.load(file)


        self.user_answers = []
        self.screen_manager = ScreenManager()

        self.screen_manager.add_widget(StartScreen(name="start"))

        for index, data in enumerate(self.questions):
            screen = QuestionScreen(data=data,index=index)
            self.screen_manager.add_widget(screen)

        self.screen_manager.add_widget(ResultScreen(name='result'))
        
        self.screen_manager.current = "start"
        return self.screen_manager
    
app = TestApp()
app.run()




[
    {
        "question": "Какой из этих предметов не может танцевать?",
        "type": "text",
        "options": [
            {"text": "Танцор", "correct": false},
            {"text": "Кошка", "correct": false},
            {"text": "Суп", "correct": true},
            {"text": "Человек", "correct": false}
        ]
    },
    {
        "question": "Что из этого не может летать?",
        "type": "text",
        "options": [
            {"text": "Птица", "correct": false},
            {"text": "Самолет", "correct": false},
            {"text": "Кирпич", "correct": true},
            {"text": "Насекомое", "correct": false}
        ]
    },
    {
        "question": "Что из этого не может говорить?",
        "type": "text",
        "options": [
            {"text": "Папуга", "correct": false},
            {"text": "Человек", "correct": false},
            {"text": "Камень", "correct": true},
            {"text": "Собака", "correct": false}
        ]
    },
    {
        "question": "Какой из этих предметов не имеет ушей?",
        "type": "text",
        "options": [
            {"text": "Слон", "correct": false},
            {"text": "Кот", "correct": false},
            {"text": "Микрофон", "correct": true},
            {"text": "Собака", "correct": false}
        ]
    },
    {
        "question": "Что из этого не может быть съедено на завтрак?",
        "type": "text",
        "options": [
            {"text": "Яйцо", "correct": false},
            {"text": "Хлеб", "correct": false},
            {"text": "Лампочка", "correct": true},
            {"text": "Каша", "correct": false}
        ]
    },
    {
        "question": "Какой из этих фруктов не может быть зеленым?",
        "type": "text",
        "options": [
            {"text": "Яблоко", "correct": false},
            {"text": "Груша", "correct": false},
            {"text": "Апельсин", "correct": true},
            {"text": "Киви", "correct": false}
        ]
    },
    {
        "question": "Что из этого не умеет плавать?",
        "type": "text",
        "options": [
            {"text": "Рыба", "correct": false},
            {"text": "Утка", "correct": false},
            {"text": "Дерево", "correct": true},
            {"text": "Человек", "correct": false}
        ]
    },
    {
        "question": "Какой из этих предметов не носит одежду?",
        "type": "text",
        "options": [
            {"text": "Человек", "correct": false},
            {"text": "Кукла", "correct": false},
            {"text": "Собака", "correct": false},
            {"text": "Кубик", "correct": true}
        ]
    },
    {
        "question": "Что из этого не умеет смеяться?",
        "type": "text",
        "options": [
            {"text": "Человек", "correct": false},
            {"text": "Шут", "correct": false},
            {"text": "Доска", "correct": true},
            {"text": "Клоун", "correct": false}
        ]
    },
    {
        "question": "Какой из этих предметов не может писать?",
        "type": "text",
        "options": [
            {"text": "Ручка", "correct": false},
            {"text": "Карандаш", "correct": false},
            {"text": "Тетрадь", "correct": true},
            {"text": "Мел", "correct": false}
        ]
    }
]
