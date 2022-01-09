"""
A DSL
"""


class Main:
    def __init__(self, doc: str):
        super(Main, self).__init__()
        self.file = doc.split('\n')
        self.things = {}
        try:
            for s in self.file:
                self.things[s.split(':')[0]] = s.split(':')[1]
        except IndexError:
            pass

    def interrupt(self, meaning: dict):
        try:
            for key, values in self.things.items():
                meaning[key](values)
        except IndexError:
            pass
        except KeyError:
            return 1
