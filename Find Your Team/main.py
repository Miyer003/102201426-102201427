from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # 创建一个按钮，当被点击时，会调用self.on_button_click方法
        button = Button(text='Click Me')
        button.bind(on_press=self.on_button_click)

        return button

    def on_button_click(self, instance):
        # 创建一个标签显示消息
        label = Label(text='Hello, Find Your Team!')
        label.center = self.root.center
        self.root.add_widget(label)

if __name__ == '__main__':
    MyApp().run()