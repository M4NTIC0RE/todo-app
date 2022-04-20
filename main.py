import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Window.fullscreen = 'auto'

global armebeendet
global bauchbeendet
global beinebeendet

global armeeins
global armezwei
global armedrei
global armevier

global baucheins
global bauchzwei

global beineeins
global beinezwei
global beinedrei

global klavierbeendet
global programmierenbeendet
global schulebeendet
global sportbeendet

armebeendet = False
bauchbeendet = False
beinebeendet = False
sportbeendet = False

armeeins = False
armezwei = False
armedrei = False
armevier = False

klavierbeendet = False
programmierenbeendet = False
schulebeendet = False

Builder.load_string("""
<vordererBereich>
	GridLayout:
		cols: 1
		size: root.width, root.height
		Button: 
			text: "Todo's"
			background_color: (0.93, 0.93, 0.93, 1.0)
			id: btn
			font_size: 180
			on_release: 
				root.manager.current = 'hinten'
				root.manager.transition.direction = 'left'
		Button:
    		id:btnExit
    		background_color: (0.0, 0.0, 0.0, 0.0)
    		text:"Exit"
    		font_size: 180
    		on_press: app.Exit()

<hintererBereich>:
	knopfnull: btnnull
	knopfeins: btneins
	knopfzwei: btnzwei
	knopfdrei: btndrei
	GridLayout:
		cols: 1
		size: root.width, root.height
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			text: 'Sport'
			id: btnnull
			font_size: 30
			on_release:
				root.manager.current = 'spEins'
				root.manager.transition.dorection = 'right'
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			text: 'Klavier'
			id: btneins
			font_size: 30
			on_release:
				root.manager.current = 'klavier'
				root.manager.transition.dorection = 'right'
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			text: 'Programmieren'
			id: btnzwei
			font_size: 30
			on_release:
				root.manager.current = 'programmieren'
				root.manager.transition.dorection = 'right'
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			text: 'Schule'
			id: btndrei
			font_size: 30
			on_release:
				root.manager.current = 'schule'
				root.manager.transition.dorection = 'right'
		Button:
			text: 'Aktualisieren'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.ueberpruefen()

		Button:
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'vorne'
				root.manager.transition.dorection = 'right'
<sportEins>:
	knopfeins: btneins
	knopfzwei: btnzwei
	knopfdrei: btndrei
	GridLayout:
		cols: 1
		size: root.width, root.height
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			id: btneins
			text: 'Arme'
			font_size: 30
			on_release:
				root.manager.current = 'arme'
				root.manager.transition.dorection = 'right'
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			id: btnzwei
			text: 'Bauch'
			font_size: 30
			on_release:
				root.manager.current = 'bauch'
				root.manager.transition.dorection = 'right'
		Button:
			background_color: (0.93, 0.93, 0.93, 1.0)
			id: btndrei
			text: 'Beine'
			font_size: 30
			on_release:
				root.manager.current = 'beine'
				root.manager.transition.dorection = 'right'
		Button:
			text: 'Aktualisieren'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.ueberpruefen()
		Button:
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'hinten'
				root.manager.transition.dorection = 'right'
<arme>
	eins: erst.text
	zwei: zweit.text
	drei: dritt.text
	vier: viert.text
	knopfeins: btneins
	knopfzwei: btnzwei
	knopfdrei: btndrei
	knopfvier: btnvier
	GridLayout:
		cols: 1
		size: root.width, root.height
		GridLayout:
			cols:2
			Button:
				id: btneins
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Liegestütze - 15'
				font_size: 30
			TextInput:
				id: erst
				multiline: False
				font_size: 30
			Button:
				id: btnzwei
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Über den Kopf - 15'
				font_size: 30
			TextInput:
				id: zweit
				multiline: False
				font_size: 30
			Button:
				id: btndrei
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Stehend auf Brusthöhe - 20'
				font_size: 30
			TextInput:
				id: dritt
				multiline: False
				font_size: 30
			Button:
				id: btnvier
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Kniend auf Bank - 20'
				font_size: 30
			TextInput:
				id: viert
				multiline: False
				font_size: 30
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'spEins'
				root.manager.transition.dorection = 'right'
<bauch>
	eins: erst.text
	zwei: zweit.text
	knopfeins: btneins
	knopfzwei: btnzwei
	GridLayout:
		cols: 1
		size: root.width, root.height
		GridLayout:
			cols:2
			Button:
				id: btneins
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Sit ups - 30'
				font_size: 30
			TextInput
				id: erst
				multiline: False
				font_size: 30
			Button:
				id: btnzwei
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Kniebeuge - 20'
				font_size: 30
			TextInput:
				id: zweit
				multiline: False
				font_size: 30
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'spEins'
				root.manager.transition.dorection = 'right'
<beine>
	eins: erst.text
	zwei: zweit.text
	drei: dritt.text
	knopfeins: btneins
	knopfzwei: btnzwei
	knopfdrei: btndrei
	GridLayout:
		cols: 1
		size: root.width, root.height
		GridLayout:
			cols:2
			Button:
				id: btneins
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Fahrrad - 30km'
				font_size: 30
			TextInput
				id: erst
				multiline: False
				font_size: 30
			Button:
				id: btnzwei
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Step ups - 20'
				font_size: 30
			TextInput
				id: zweit
				multiline: False
				font_size: 30	
			Button:
				id: btndrei
				background_color: (1.0, 1.0, 1.0, 0.5)
				disabled: True
				text: 'Ausfallschritte - 20'
				font_size: 30
			TextInput
				id: dritt
				multiline: False
				font_size: 30		
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'spEins'
				root.manager.transition.dorection = 'right'
<klavier>
	antwort: antw.text
	knopf: btn
	GridLayout:
		cols: 1
		size: root.width, root.height	
		GridLayout:
			cols: 2
			Button:
				background_color: (1.0, 1.0, 1.0, 0.5)
				id: btn
				disabled: True
				text: 'Klavier - 1h'
				font_size: 30
			TextInput
				id: antw
				multiline: False
				font_size: 30
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'hinten'
				root.manager.transition.dorection = 'right'
<programmieren>
	antwort: antw.text
	knopf: btn
	GridLayout:
		cols: 1
		size: root.width, root.height	
		GridLayout:
			cols: 2
			Button:
				background_color: (1.0, 1.0, 1.0, 0.5)
				id: btn
				disabled: True
				text: 'Programmieren - 1h'
				font_size: 30
			TextInput
				id: antw
				multiline: False
				font_size: 30
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'hinten'
				root.manager.transition.dorection = 'right'
<schule>
	antwort: antw.text
	knopf: btn
	GridLayout:
		cols: 1
		size: root.width, root.height	
		GridLayout:
			cols: 2
			Button:
				background_color: (1.0, 1.0, 1.0, 0.5)
				id: btn
				disabled: True
				text: 'Lernen'
				font_size: 30
			TextInput
				id: antw
				multiline: False
				font_size: 30
		Button:
			size_hint: (1.,0.25)
			text: 'Bestätigen'
			background_color: (0.0, 1.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.beendet()
		Button:
			size_hint: (1.,0.25)
			text: 'Zurück'
			background_color: (1.0, 0.0, 0.0, 1.0)
			font_size: 30
			on_release:
				root.manager.current = 'hinten'
				root.manager.transition.dorection = 'right'
""")
class vordererBereich(Screen):
	pass
class hintererBereich(Screen):
	knopfnull = ObjectProperty()
	knopfeins = ObjectProperty()
	knopfzwei = ObjectProperty()
	knopfdrei = ObjectProperty()
	def ueberpruefen(self):
		global klavierbeendet
		global programmierenbeendet
		global schulebeendet
		global sportbeendet
		if sportbeendet == True:
			self.knopfnull.background_color = [0.,1.,0.,1.]
		else:
			self.knopfnull.background_color = [0.93,0.93,0.93,1.]
			sportbeendet == False
		if klavierbeendet == True:
			self.knopfeins.background_color = [0.,1.,0.,1.]
		else:
			self.knopfeins.background_color = [0.93,0.93,0.93,1.]
			klavierbeendet == False
		if programmierenbeendet == True:
			self.knopfzwei.background_color = [0.,1.,0.,1.]
		else:
			self.knopfzwei.background_color = [0.93,0.93,0.93,1.]
			programmierenbeendet == False
		if schulebeendet == True:
			self.knopfdrei.background_color = [0.,1.,0.,1.]
		else:
			self.knopfdrei.background_color = [0.93,0.93,0.93,1.]
			schulebeendet == False
		if sportbeendet == True and klavierbeendet == True and programmierenbeendet == True and schulebeendet == True:
			popup = Popup(title="Fertig",
			content = Label(text="Du hast alle Aufgaben erledigt!\n Für heute...", text_size=("20sp")),
			size_hint=(None,None), size=(400,400))
			popup.open()
class sportEins(Screen):
	knopfeins = ObjectProperty()
	knopfzwei = ObjectProperty()
	knopfdrei = ObjectProperty()
	def ueberpruefen(self):
		global sportbeendet
		global armebeendet
		global bauchbeendet
		global beinebeendet
		if armebeendet == True:
			self.knopfeins.background_color = [0.,1.,0.,1.]
		else:
			self.knopfeins.background_color = [0.93,0.93,0.93,1.]
			armebeendet == False
		if bauchbeendet == True:
			self.knopfzwei.background_color = [0.,1.,0.,1.]
		else:
			self.knopfzwei.background_color = [0.93,0.93,0.93,1.]
			bauchbeendet == False
		if beinebeendet == True:
			self.knopfdrei.background_color = [0.,1.,0.,1.]
		else:
			self.knopfdrei.background_color = [0.93,0.93,0.93,1.]
			beinebeendet == False
		if armebeendet == True and bauchbeendet == True and beinebeendet == True:
			sportbeendet = True
		else:
			sportbeendet = False
class arme(Screen):
	eins = StringProperty()
	zwei = StringProperty()
	drei = StringProperty()
	vier = StringProperty()
	knopfeins = ObjectProperty()
	knopfzwei = ObjectProperty()
	knopfdrei = ObjectProperty()
	knopfvier = ObjectProperty()
	def beendet(self):
		global armeeins
		global armezwei
		global armedrei
		global armevier
		global armebeendet
		if self.eins.lower() == 'ja':
			self.knopfeins.background_color = [0.,1.,0.,1.]
			armeeins = True
		else:
			self.knopfeins.background_color = [0.93,0.93,0.93,1.]
			armeeins = False
		if self.zwei.lower() == 'ja':
			self.knopfzwei.background_color = [0.,1.,0.,1.]
			armezwei = True
		else:
			self.knopfzwei.background_color = [0.93,0.93,0.93,1.]
			armezwei = False
		if self.drei.lower() == 'ja':
			self.knopfdrei.background_color = [0.,1.,0.,1.]
			armedrei = True
		else:
			self.knopfdrei.background_color = [0.93,0.93,0.93,1.]
			armedrei = False
		if self.vier.lower() == 'ja':
			self.knopfvier.background_color = [0.,1.,0.,1.]
			armevier = True
		else:
			self.knopfvier.background_color = [0.93,0.93,0.93,1.]
			armevier = False
		if armeeins == True and armezwei == True and armedrei == True and armevier == True:
			armebeendet = True
		else: 
			armebeendet = False
class bauch(Screen):
	eins = StringProperty()
	zwei = StringProperty()
	knopfeins = ObjectProperty()
	knopfzwei = ObjectProperty()
	def beendet(self):
		global baucheins
		global bauchzwei
		global bauchbeendet
		if self.eins.lower() == 'ja':
			self.knopfeins.background_color = [0.,1.,0.,1.]
			baucheins = True
		else:
			self.knopfeins.background_color = [0.93,0.93,0.93,1.]
			baucheins = False
		if self.zwei.lower() == 'ja':
			self.knopfzwei.background_color = [0.,1.,0.,1.]
			bauchzwei = True
		else:
			self.knopfzwei.background_color = [0.93,0.93,0.93,1.]
			bauchzwei = False
		if baucheins == True and bauchzwei == True:
			bauchbeendet = True
		else: 
			bauchbeendet = False
class beine(Screen):
	eins = StringProperty()
	zwei = StringProperty()
	drei = StringProperty()
	knopfeins = ObjectProperty()
	knopfzwei = ObjectProperty()
	knopfdrei = ObjectProperty()
	def beendet(self):
		global beineeins
		global beinezwei
		global beinedrei
		global beinebeendet
		if self.eins.lower() == 'ja':
			self.knopfeins.background_color = [0.,1.,0.,1.]
			beineeins = True
		else:
			self.knopfeins.background_color = [0.93,0.93,0.93,1.]
			beineeins = False
		if self.zwei.lower() == 'ja':
			self.knopfzwei.background_color = [0.,1.,0.,1.]
			beinezwei = True
		else:
			self.knopfzwei.background_color = [0.93,0.93,0.93,1.]
			beinezwei = False
		if self.drei.lower() == 'ja':
			self.knopfdrei.background_color = [0.,1.,0.,1.]
			beinedrei = True
		else:
			self.knopfdrei.background_color = [0.93,0.93,0.93,1.]
			beinedrei = False
		if beineeins == True and beinezwei == True and beinedrei == True:
			beinebeendet = True
		else: 
			beinebeendet = False
class klavier(Screen):
	knopf = ObjectProperty()
	antwort = StringProperty()
	def beendet(self):
		global klavierbeendet
		if self.antwort.lower() == 'ja':
			self.knopf.background_color = [0.,1.,0.,1.]
			klavierbeendet = True
		else:
			self.knopf.background_color = [1.,1.,1.,0.5]
			klavierbeendet = False
class programmieren(Screen):
	knopf = ObjectProperty()
	antwort = StringProperty()
	def beendet(self):
		global programmierenbeendet
		if self.antwort.lower() == 'ja':
			self.knopf.background_color = [0.,1.,0.,1.]
			programmierenbeendet = True
		else:
			self.knopf.background_color = [1.,1.,1.,0.5]
			programmierenbeendet = False
class schule(Screen):
	knopf = ObjectProperty()
	antwort = StringProperty()
	def beendet(self):
		global schulebeendet
		if self.antwort.lower() == 'ja':
			self.knopf.background_color = [0.,1.,0.,1.]
			schulebeendet = True
		else:
			self.knopf.background_color = [1.,1.,1.,0.5]
			schulebeendet = False
ms = ScreenManager()
ms.add_widget(vordererBereich(name="vorne"))
ms.add_widget(hintererBereich(name="hinten"))
ms.add_widget(sportEins(name="spEins"))
ms.add_widget(arme(name="arme"))
ms.add_widget(bauch(name="bauch"))
ms.add_widget(beine(name="beine"))
ms.add_widget(klavier(name="klavier"))
ms.add_widget(programmieren(name="programmieren"))
ms.add_widget(schule(name="schule"))

class StartApp(App):
	def build(self):
		return ms

if __name__=='__main__':
	StartApp().run()