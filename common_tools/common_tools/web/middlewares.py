import time


def measure_time_middleware(get_response):
    def middleware(request, *args, **kwargs):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()
        print(f'Executed in {end_time - start_time}s')
        return response
    return middleware


def last_viewed_books_middleware(get_response):
    def middleware(request, *args, **kwargs):
        request.books = request.session.get('last_viewed_books', [])
        return get_response(request)
    return middleware


def active_user_middleware(get_response):
    def middleware(request, *args, **kwargs):
        if request.user.is_authenticated():
            pass
    return middleware