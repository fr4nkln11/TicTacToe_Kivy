from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex as hexColor 
    
Window.clearcolor = hexColor('#ffffff')

class tictactoeApp(App):
    colors = {
        'white': hexColor('#ffffff'),
        'red': hexColor('#ff0000'),
        'green': hexColor('#00ff00'),
        'blue': hexColor('#0000ff'),
        'grey': hexColor('#cccccc'),
        'black': hexColor('#000000')
    }
    
    Xpc = "X"
    Opc = "O"
    cpc = Xpc
    
    #cords = "a1,b1,c1,a2,b2,c2,a3,b3,c3".split(',')
        
    def check_board(self):
        cells = {
        "a1":self.root.ids.a1.text,
        "b1":self.root.ids.b1.text,
        "c1":self.root.ids.c1.text,
        "a2":self.root.ids.a2.text,
        "b2":self.root.ids.b2.text,
        "c2":self.root.ids.c2.text,
        "a3":self.root.ids.a3.text,
        "b3":self.root.ids.b3.text,
        "c3":self.root.ids.c3.text
        }

        def full():
            return "" not in cells.values()

        if full():
            self.root.ids.status.text = "DRAW!"
            self.root.ids.reset.disabled = False

        def win():
            combs = ["a1,b1,c1","a2,b2,c2","a3,b3,c3","a1,a2,a3","b1,b2,b3", "c1,c2,c3", "a1,b2,c3", "c1,b2,a3"]

            for combination in combs:
                wcells = combination.split(',')

                if all(cells[c] == "X" for c in wcells) or all(cells[c] == "O" for c in wcells):
                    winner = cells[wcells[0]]
                    self.root.ids.status.text = f"{winner} WINS the game"
                    return True

        if win():
            for child in reversed(self.root.ids.grid.children):
                child.disabled = True
            self.root.ids.reset.disabled = False
    
    
    def switchTurn(self):
        if self.cpc == self.Xpc:
            self.cpc = self.Opc
        elif self.cpc == self.Opc:
            self.cpc = self.Xpc
        
        self.root.ids.status.text = f"It's {self.cpc}'s turn"
            
    def play(self, btn):
        btn.text = self.cpc
        if self.cpc == self.Xpc:
            btn.disabled_color = self.colors['red']
        elif self.cpc == self.Opc:
            btn.disabled_color = self.colors['blue']
            
        btn.disabled = True
        self.switchTurn()
        self.check_board()
        
    def reset(self):
        for child in reversed(self.root.ids.grid.children):
            child.text = ""
        
        for child in reversed(self.root.ids.grid.children):
            child.disabled = False
        
        self.root.ids.status.text = "X plays first"
        self.cpc = self.Xpc
        self.root.ids.reset.disabled = True


if __name__ == '__main__':
    from kivy.core.text import LabelBase
        
    LabelBase.register(name="Roboto",
    fn_regular="fonts/Roboto-Thin.ttf",
    fn_bold="fonts/Roboto-Medium.ttf")
    
    tictactoeApp().run()