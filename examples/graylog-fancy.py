#!/usr/bin/env python
# vim: set ts=8 sw=4 sts=4 et ai:

# configurables
FROM_EMAIL = 'noreply@example.com'
ELASTICSEARCH_URL = 'http://localhost:9200/graylog2_recent/message/_search'
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'graylog2'

from collections import namedtuple
from email.mime.text import MIMEText
import json
import httplib2
import os
from pymongo import Connection
import smtplib
import sys
import time
import urllib

LogMessage = namedtuple('LogMessage', 'message, level, host, facility, file, histogram_time, full_message, created_at, line, streams')

def fancymessage(to, topic, description):
    try:
        stream = get_stream(topic)
    except:  # XXX catch explicit errors
        stream = None

    if stream is not None:
        messages = get_messages(stream['_id'])
    else:
        messages = []

    body = []
    if description is not None:
        body.append(description)
        body.append('')

    for message in messages:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(message.created_at))
        body.append('%s %s' % (timestamp, message.message))

    if not stream:
        body.append('Unable to load messages for this topic, I could not identify the stream')

    msg = MIMEText('\n'.join(body))
    msg['To'] = ', '.join(to)
    msg['From'] = 'noreply@voipgrid.nl'
    msg['Subject'] = topic
    s = smtplib.SMTP('localhost')
    s.sendmail(FROM_EMAIL, to, msg.as_string())
    s.quit()


def get_messages(stream_id, size=25):
    params = urllib.urlencode({
        'size': size,
        'q': 'streams:%s' % stream_id,
    })
    http = httplib2.Http(timeout=10)
    url = '%s?%s' % (ELASTICSEARCH_URL, params)
    response, content = http.request(url)
    assert response.status == 200
    return [LogMessage(**hit['_source']) for hit in json.loads(content)['hits']['hits']]


def get_stream(topic):
    # get the stream title from the alarm topic
    title = topic[29:-1]
    connection = Connection(MONGO_URI)
    db = connection[MONGO_DB]
    streams = db['streams']
    stream = streams.find_one({'title': title})
    return stream


if __name__ == '__main__':
    topic = os.environ.get('GL2_TOPIC')
    description = os.environ.get('GL2_DESCRIPTION')
    if topic is not None and len(sys.argv) > 1:
        fancymessage(sys.argv[1:], topic, description)