class MyList(list):
    def index(self, value):
        #result = super().index(value)
        #return result + 100
        for index, item in enumerate(self):
            if item == value:
                return index + 100
    
lst = MyList([34, 1, 'hello', True])
print(lst.index(1)) #101