from kivy.app import App
import requests
import json
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.floatlayout import FloatLayout

class fintech(App):
    pass

class List_screen(FloatLayout):
    company = StringProperty()
    l_fix = StringProperty()
    l_cur = StringProperty()
    Dep = StringProperty()


    def show_current_stocks(self,company):
        r = requests.get('http://finance.google.com/finance/info?client=ig&q=NSE:{}'.format(company))
        global details
        details = r.text
        details = json.loads(details[3:])[0]
        self.clear_widgets()
        self.add_widget(stocksAtGlance())
        self.company = details["t"]
        self.l_fix = details["l_fix"]
        self.l_cur = details["l_cur"]
        self.Dep = details["e"]



class showCurrentSituation(ListItemButton):
    pass
class stocksAtGlance(FloatLayout):
    def fill_details(self):
        pass



if __name__=='__main__':
    fintech().run()
