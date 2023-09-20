class HelloClass:
    def __init__(self, msg):
        self.msg = msg

    def output(self):
        print(self.msg)

hello = HelloClass('Hello World')
hello.output()