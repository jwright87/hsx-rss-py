from unittest import TestCase
from hsx_rss_reddit import *
import json


class RedditRssTest(TestCase):
    def test_get_reddit_posts(self):
        test_file = open("hsx-rss-py/resources/sample-request.json", "r")
        json_request = test_file.read()
        result = get_reddit_posts(json_request)
        self.assertEqual(type(result), str)
        dict_result = json.loads(result)
        self.assertEqual(dict_result["symbol"], "BTC")
        feed = dict_result["feed"][0]
        self.assertEqual(type(feed["date_time"]), float)
        test_file.close()
