#Conditions class by jw2pfd
#http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=25460
#March 2, 2014
init python:
    class Link(store.object):      #It's cool when classes work with rollback
        pass
    class Conditions(Link):
        current = None
        def __init__(self):
            self.clear()
        def addcondition(self, text, condition, tt='', alignment=''):
            Conditions.current = self
            self.conditions[text] = (condition, tt)
        def check(self, caption):
            ret = caption in self.conditions.keys()
            ret = ret and not eval(self.conditions[caption][0])
            return ret
        def clear(self):
            self.conditions = { }
        def text(self, caption):
            return "{0} {1}".format(caption, self.conditions[caption][1])