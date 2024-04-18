class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
    
maria = Person(['마리아', 20, '서울시 서초구 반포동'])