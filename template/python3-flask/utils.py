class FunctionEvent(object):
    def __init__(self, request):
        self.headers = {key: value for key, value in request.headers}

        self.method = request.method
        self.body = request.get_data()
        self.query = request.args


class FunctionContext(object):
    def __init__(self):
        self.status_code = 200
        self.failed = False
        self.headers_dict = {}
        self.result = self.error_message = None

    def status(self, value=None):
        if not value:
            return self.status_code

        self.status_code = value

        return self

    def headers(self, headers: dict = None):
        if not headers:
            return self.headers_dict

        self.headers_dict = headers

        return self

    def succeed(self, result: object):
        self.failed = False
        self.result = result

    def fail(self, error_message: str):
        self.failed = True
        self.error_message = error_message
