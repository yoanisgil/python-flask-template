from utils import FunctionContext, FunctionEvent


def handle(event: FunctionEvent, context: FunctionContext) -> None:
    result = {"message": "message accepted", "input_headers": event.headers}

    context.status(202).headers({'X-Process-By': 'my-function'}).succeed(result)
