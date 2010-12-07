class DeferredRenderingMiddleware(object):
    def process_response(self, request, response):
        # If the response supports deferred rendering, apply template
        # response middleware and the render the response
        if hasattr(response, 'render') and callable(response.render):
            return response.render()
        return response

