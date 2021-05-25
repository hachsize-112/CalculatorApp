from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import math

Config.set('graphics', 'resizable', 0)

Config.set('graphics', 'width', 321)

Config.set('graphics', 'height', 531)

class CalculatorApp(App):
	def update_label(self):
		self.lbl.text = self.formula		

	def number(self, instance):
		if(self.formula == "0"):

		   self.formula = ""

		elif (self.formula) == "None":
			self.formula = ""


		self.formula += str(instance.text)
		self.update_label()


	def operation(self, instance):
		if( str(instance.text).lower() == "x" ):
			self.formula += "*"

			
		elif( str(instance.text).lower() == "√" ):
			try:
				self.formula = math.sqrt(float(self.formula))
			except TypeError:
				self.formula = "None"
			except SyntaxError:
				self.formula = "0"
			except ValueError:
				self.formula = "0"
	
		elif( str(instance.text).lower() == "÷" ):
			self.formula += "/"

		elif( str(instance.text).lower() == "c" ):
			self.formula = ""

		elif( str(instance.text).lower() == "y" ):#3a-3a371і                                                                                                                  
			self.formula += "**"

		else:
		    self.formula += str(instance.text)

		self.update_label()

	def result(self, instance ):

		try:
			self.lbl.text = str(eval(self.lbl.text ))
			self.formula = ""
		except SyntaxError:
			self.formula = ""
		except ValueError:
			self.formula = ""

		except NameError:
			self.formula = ""

		except TypeError:
			self.formula = ""
		except ZeroDivisionError:
			self.formula = ""



	def build(self):
		self.formula = "0"
		#front_ccolor= [1,0,0,1]
		bl = BoxLayout(orientation = 'vertical', padding=7)

		gl = GridLayout(cols = 4,  size_hint = (1, .6),spacing=2,)
		                                  #колір вводу#FFFFFF#FFFFFF
		self.lbl = Label(text="0",color= [209/255,14/255,235/255 , 250/255], font_size = 30,halign ="right", valign = "center", size_hint = (1, .4), text_size=(321 - 5, 531 * .5 - 5))

		bl.add_widget( self.lbl )

		gl.add_widget( Button(text="y", on_press = self.operation,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
		gl.add_widget( Button(text="(", on_press = self.number,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
		gl.add_widget( Button(text=")", on_press = self.number,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
		gl.add_widget( Button(text="÷", on_press = self.operation,background_color = [19/255,19/255,19/255 , 255/255],background_normal =""))

		gl.add_widget( Button(text="7", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="8", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="9", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal =""))
		gl.add_widget( Button(text="x", on_press = self.operation,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )

		#gl.add_widget( Button(text="f", on_press = self.add_operation) ) gl.add_widget( Button(text="xn", on_press = self.add_operation) )#√
		
		gl.add_widget( Button(text="4", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="5", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="6", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="-", on_press = self.number,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )

	     #gl.add_widget( Button(text="xn", on_press = self.add_operation) )#√

		gl.add_widget( Button(text="1", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="2", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 ,200/255],background_normal ="") )
		gl.add_widget( Button(text="3", on_press = self.number ,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text="+", on_press = self.number ,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )

		gl.add_widget( Button(text="C", on_press = self.operation,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
		gl.add_widget( Button(text="0", on_press = self.number,color= [0,0,0,1],background_color = [209/255,14/255,235/255 , 200/255],background_normal ="") )
		gl.add_widget( Button(text=".", on_press = self.number,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
		gl.add_widget( Button(text="=", on_press = self.result,background_color = [19/255,19/255,19/255 , 255/255],background_normal ="") )
        
		bl.add_widget( gl )
		return bl

if __name__=="__main__":

	CalculatorApp().run()
