class PasswordInfo:

    def __init__(self, info):
        self.should_start_with = info['shouldStartWith']
        self.should_contain    = info['shouldContain']
        self.min_length        = info['minimumLength']
        self.max_length        = info['maximumLength']
