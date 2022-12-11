class Test:
    def __init__(self):
        print("A")
    def do_something(self):
        print("B")
        self.do_another(self)
    def do_another(self):
        print("C")
run = Test
run.do_something(run)