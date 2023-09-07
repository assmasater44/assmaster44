from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.clock import Clock
from kivy.core.window import Window

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Window.clearcolor = (0, 0, 0, 0)  # Set background color to transparent

class ShakeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Shake your phone to replicate swipe gestures")
        self.layout.add_widget(self.label)
        self.shake_count = 0

        # Initialize accelerometer and set its callback function
        from plyer import accelerometer
        accelerometer.enable()
        accelerometer.set_sensor("accelerometer")
        accelerometer.buffersize = 1
        accelerometer.set_frequency(1 / 60.0)
        accelerometer.bind(on_shake=self.on_shake)

        return self.layout

    def on_shake(self, instance, acceleration):
        # Detect shakes based on accelerometer data
        if acceleration['magnitude'] > 20:
            self.shake_count += 1
            if self.shake_count == 1:
                self.label.text = "Shake detected! Swipe Down"
            elif self.shake_count == 2:
                self.label.text = "Two shakes detected! Swipe Up"
            else:
                self.shake_count = 0
                self.label.text = "Shake your phone to replicate swipe gestures"

if __name__ == '__main__':
    ShakeApp().run()
