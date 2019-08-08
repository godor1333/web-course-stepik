def application(environ, start_response):
    """Simplest possible application object"""
    # data = 'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, response_headers)
    return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]