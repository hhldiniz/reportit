from json import JSONEncoder


class JSONEncoderUtil(JSONEncoder):
    def __init__(self):
        super().__init__()

    def default(self, o):
        return o.__dict__
