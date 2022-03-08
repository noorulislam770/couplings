class Drive:
    def __init__(self,files,owner):
        self.files = files
        self.owner = owner
        self.gui = GUI();

    def deleteFile(,self, filename):
        if (gui.confirmDelete() == True):
            print("file Deleted ")


class GUI ():
    def __init__(self):
        pass
    
    def confirmDelete (self):
        return True 


drive = Drive(['abc.txt', 'def.txt'], 'noor')
drive.deleteFile("abc.txt")

print (" class GUI is passing control flag to class Drive Hence control coupling..")