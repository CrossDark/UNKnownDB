"""
A DSL
"""


class Main:
    def __init__(self, doc: str):
        super(Main, self).__init__()
        self.file = doc.split('\n')
        self.things = {}
        for s in self.file:
            self.things[s.split(':')[0]] = s.split(':')[1]
            print(self.things)
