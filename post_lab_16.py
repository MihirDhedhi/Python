import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
class CounterApp(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(text=f'Count: {self.count}', font_size='48sp')
        button = Button(text='Increment', font_size='36sp')
        button.bind(on_press=self.on_button_press)
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout
    def on_button_press(self, instance):
        self.count += 1
        self.label.text = f'Count: {self.count}'
if __name__ == '__main__':
    CounterApp().run()
    
    
    
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TextInputApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # TextInput field
        self.text_input = TextInput(
            text='',
            font_size=32,
            size_hint=(1, 0.3),
            multiline=False
        )
        
        # Button
        button = Button(
            text='Display Text',
            font_size=32,
            size_hint=(1, 0.3)
        )
        button.bind(on_press=self.on_button_press)
        
        # Label to display text
        self.output_label = Label(
            text='Your text will appear here.',
            font_size=32,
            size_hint=(1, 0.3)
        )
        
        # Add widgets to layout
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(button)
        self.layout.add_widget(self.output_label)
        
        return self.layout

    def on_button_press(self, instance):
        input_text = self.text_input.text
        self.output_label.text = input_text

if __name__ == '__main__':
    TextInputApp().run()

    
    
    
    
    
    
    
    
    
    
    
    
    