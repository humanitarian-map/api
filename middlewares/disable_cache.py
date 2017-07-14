class DisableCacheMiddleware(object):
    def process_response(self, req, resp, resource):
        resp.cache_control = ['private', 'max-age=0', 'no-cache']
