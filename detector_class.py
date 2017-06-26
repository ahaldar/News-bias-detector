import result_class
import content_class

class Detector(object):

    def __init__(self):
        self.bias_types = []

    def add_bias_type(self, bias_type):
        self.bias_types.append(bias_type)

    def detect(self, content):
        content = content_class.create(content)
        result = result_class.create()
        for bias_type in self.bias_types:
            result.set_current_bias_type(bias_type)
            bias_type['test'](self, content, result)
            result.clear_current_bias_type()
        return result

def create():
    return Detector()
