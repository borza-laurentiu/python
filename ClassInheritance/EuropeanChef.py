from Chef import *

#or you can do it this way:

class EuropeanChef:

    def __init__(self, name='Jamie', style = 'european'):
        super().__init__()
        self.name = name
        self.style = style
        
    def cook(self):
        return 'true'