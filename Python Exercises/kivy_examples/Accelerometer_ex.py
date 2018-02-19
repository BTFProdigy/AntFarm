from kivy.app import App # for the main app
from kivy.uix.floatlayout import FloatLayout #the UI layout
from kivy.uix.label import label # a label to show information
from plyer import accelerometer # object to read the accelerometer
from kivy.clock import Clock #clock to schedule method

class Accelerometer_ex(App): # our app
	def build(self):
		ui = UI() # create the UI
		return ui # show it

if __name__ == '__main__':
	Accelerometer_ex.run() # start the app