class DevOps:

    def __init__(self, listNames=[]):
        self.listNames = listNames

    def add_names(self, name):
        return self.listNames.append(name)

    def display_names(self):
        return self.listNames

    def counter(self):
        return len(self.listNames)

while True:

    newDevOps = DevOps()

    name = input("Enter learner name: ")

    newDevOps.add_names(name)

    print(newDevOps.display_names())

    cont = input("Do you wish to add more names: ")

    if cont != 'y':
        break
    else: 
        pass