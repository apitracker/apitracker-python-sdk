import http.client

class Patcher:
    def __init__(self, config):
        self.config = config
        self.original_http_gethostport = http.client.HTTPConnection._get_hostport

    def patch(self):
        def patched_get_hostport(s, host, port):
            (host, port) = self.original_http_gethostport(s, host, port)
            if host in self.config:
                return self.config[host]['url'], 443
            return host, port
        http.client.HTTPConnection._get_hostport = patched_get_hostport

    def unpatch(self):
        http.client.HTTPConnection._get_hostport = self.original_http_gethostport