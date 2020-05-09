from flask import Flask, request
from hsx_rss_reddit import get_reddit_posts
import logging as log

log.basicConfig(level=log.DEBUG)

app = Flask(__name__)


@app.route('/rss', methods=['POST'])
def process_request():
    content = request.json
    log.debug(type(content))
    return get_reddit_posts(content)


if __name__ == '__main__':
    app.run(debug=True)
