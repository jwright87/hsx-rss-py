import json
import feedparser
import time
import logging as log
import re

log.basicConfig(level=log.DEBUG)


def get_reddit_posts(request):
    """Parses the request json for a reddit rss url and returns the feed, also in json format"""
    request_dict = request  # json.loads(request)
    log.debug(f"Getting Reddit Posts for {request_dict['symbol']}")
    url = _get_url(request_dict)
    feed = _get_feed(url)
    out_feed_list = _convert_feed_to_output(feed)
    result = _map_result(request_dict, out_feed_list)
    return json.dumps(result)


def _map_result(request_dict, out_feed_list):
    result = {}
    result["symbol"] = request_dict["symbol"]
    result["name"] = request_dict["name"]
    result["feed"] = out_feed_list
    return result


def _get_url(dict):
    return dict["feeds"][0]["url"]


def _get_feed(url):
    return feedparser.parse(url)


def _convert_feed_to_output(feed):
    output = []
    for item in feed["items"]:
        out_item = {}
        out_item["title"] = item["title"]
        out_item["content"] = re.escape(item["content"][0]["value"])
        out_item["date_time"] = time.mktime(item["updated_parsed"])
        out_item["time_string"] = item["updated"]
        output.append(out_item)
    return output
