from django.core.urlresolvers import set_script_prefix

class ScriptPrefixMiddleware(object):
    """
    Set the script prefix for all requests.

    Essentially this adds the current request host to all calls to
    get_absolute_url().  Much more convenient than adding the schema and
    domain manually everywhere.

    """

    def process_request(self, request):
        schema = 'http://'
        if request.is_secure():
            schema = 'https://'
        host = request.get_host()
        if host:
            set_script_prefix('%s%s' % (schema, host))
