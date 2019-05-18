import random

class Learning:

    def __init__(self, input_number, step_size=0.1):
        self._ins = input_number
        self._w = [random.random() for _ in range(input_number)] 
        self._eta = step_size

    def predict(self,values):
        weighted_average = sum(w * elm for w, elm in zip(self._w,values))
        if weighted_average > 0:
           return 1
        return 0

    def train(self, values, results):
        
        output = self.predict(values)
        error = results - output
        if error != 0:
            self._w = [w + self._eta * error * x for w, x in
            zip(self._w, values)]
        return error

    def operation(self, data_persons, height):
        instance = Learning(3)
        for _ in range(100):
            for person in data_persons:
                output = person[-1]
                inp = [1] + person[0:-1]
                err = instance.train(inp,output)
        if instance.predict([1,float(height),2]) == 1:
            return 1
        else: 
            return 0
