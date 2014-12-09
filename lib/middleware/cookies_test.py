__author__ = 'inozemcev'
class TestCookieMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        request.session.set_test_cookie()
        return