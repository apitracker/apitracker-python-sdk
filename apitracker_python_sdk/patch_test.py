from apitracker_python_sdk import Patcher
import unittest
import http.client


class TestPatcher(unittest.TestCase):
    def test_patch(self):
        proxy_host = 'axxxxxsdwxaaaadfw.apitracker.net'
        original_host = 'example.com'
        apitracker_config = {}
        apitracker_config[original_host] = {
            'url': proxy_host
        }
        patcher = Patcher(apitracker_config)
        patcher.patch()

        self.assertEqual(http.client.HTTPConnection(original_host, 80).host, proxy_host)
        self.assertEqual(http.client.HTTPConnection(original_host, 80).port, 443)

        patcher.unpatch()

        self.assertEqual(http.client.HTTPConnection(original_host, 80).host, original_host)
        self.assertEqual(http.client.HTTPConnection(original_host, 80).port, 80)
