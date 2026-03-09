class person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")

p1=person("Alice")
p1.say_hello()