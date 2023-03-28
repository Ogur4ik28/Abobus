import json

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem

class MainWindow(MDBoxLayout):
	pass

class MainApp(MDApp):
	def name_search_and_populate_results_list(self, query):
		words = {}
		with open("data.json", "r", encoding='utf-8') as file:
			d_json = file.read()
			words = json.loads(d_json)
			left=list(words.keys())[0]
			right=list(words.values())[0]
			words[left] = right
		query = query.lower()
		if query in words:
			self.root.ids.search_name.text = words.get(query)
	def build(self):
		# self.icon = "Dictionary.ico"
		self.theme_cls.theme_style_switch_animation = True
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Red"
		return MainWindow()

	def on_start(self):
		with open("data.json", "r", encoding='utf-8') as file:
			d_json = file.read()
			words = json.loads(d_json)
		for i in words.items():
			d = str(i)
			d = d.replace('(','')
			d = d.replace(')','')
			d = d.replace("'",'')
			d = d.replace(',',' -')
			self.root.ids.container.add_widget(OneLineListItem(text=f"{d}"))



if __name__ == "__main__":
	MainApp().run()