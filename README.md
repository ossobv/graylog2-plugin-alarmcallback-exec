graylog2-plugin-alarmcallback-exec
==================================

A graylog-server plugin that executes a command.

The alarm topic and description are passed to the process in the environment.

| Variable name       | Contents                | 
| ------------------- | ----------------------- |
| GL2\_TOPIC          | The alarm topic         |
| GL2\_DESCRIPTION    | The alarm description   |

Examples
--------

[Python example](/examples/graylog-fancy.py) script that retrieves the stream id from the mongo database using the alarm topic and queries elasticsearch for the last 25 log messages on that stream.
