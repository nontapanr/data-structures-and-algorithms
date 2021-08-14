# class Stack:
#     def __init__(self, items=None):
#         if items != None:
#             self.items = items
#         else:
#             self.items = []

#     def push(self, dataInput):
#         self.items.append(dataInput)

#     def pop(self):
#         return self.items.pop()
    
#     def top(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

#     def isEmtry(self):
#         return self.items == []

#     def __str__(self):
#         return str(self.items)

class Stack:
    def __init__(self, items = None):
        if self.items != None:
            self.items = items
        else:
            self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)