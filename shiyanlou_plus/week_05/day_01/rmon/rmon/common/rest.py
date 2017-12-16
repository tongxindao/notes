class RestException(Exception):

    def __init__(self, code, message):
        """
        args:
            code (int): http code
            message (str): err info
        """
        self.code = code
        self.message = message
        super(RestException, self).__init__()
