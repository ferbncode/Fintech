from kivy.app import App
import requests
from kivy.properties import StringProperty 
from kivy.properties import NumericProperty
from kivy.uix.listview import ListItemButton
import ast
from kivy.uix.floatlayout import FloatLayout

class fintech(App):
    pass

class List_screen(FloatLayout):

    def show_current_stocks(self,company):
        r = requests.get('http://finance.google.com/finance/info?client=ig&q=NSE:{}'.format(company))
        global details
        details = r.text 
        details = details.encode()
        details = details.replace("\n","")
        details = details.replace("//","")
        details = details.replace("[","")
        details = details.replace("]","")
        details = details.replace(" ","")
        details = ast.literal_eval(details)
        self.clear_widgets()
        self.add_widget(stocksAtGlance())





class showCurrentSituation(ListItemButton):
    pass
class stocksAtGlance(FloatLayout):
    company = StringProperty()
    l_fix = StringProperty()
    l_cur = StringProperty()
    Dep = StringProperty()
    def fill_details(self):
        pass
    


if __name__=='__main__':
    fintech().run()
