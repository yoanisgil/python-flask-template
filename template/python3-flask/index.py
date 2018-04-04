# Copyright (c) Alex Ellis 2017. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import json

from flask import Flask, Response, request
from function import handler
from utils import FunctionContext, FunctionEvent

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main_route():
    function_event = FunctionEvent(request)
    function_context = FunctionContext()

    handler.handle(function_event, function_context)

    if function_context.failed:
        response_body = function_context.error_message
        status_code = 500
    else:
        status_code = function_context.status()

        try:
            response_body = json.dumps(function_context.result)
        except TypeError:
            response_body = str(function_context.result)

    response = Response(response_body)
    response.status_code = status_code

    for header, value in function_context.headers().items():
        response.headers[header] = value

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
