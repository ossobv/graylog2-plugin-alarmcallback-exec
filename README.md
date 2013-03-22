graylog2-plugin-alarmcallback-exec
==================================

A graylog-server plugin that executes a command.
The command is configurable in the graylog plugin system settings.

The alarm topic and description are passed to the process environment.

| Variable name       | Contents                | 
| ------------------- | ----------------------- |
| GL2\_TOPIC          | The alarm topic         |
| GL2\_DESCRIPTION    | The alarm description   |

Examples
--------

[Python example](examples/graylog-email-alert.py) script that retrieves the stream id from the mongo database using the alarm topic and queries elasticsearch for the last 25 log messages on that stream. The log messages are sent to the email addresses specified on the command line.
Plugin configuration: graylog-email-alert.py alert@example.com more@example.com

Prebuilt Download
-----------------

For your convenience a prebuilt jar is available for [download](https://code.osso.nl/projects/graylog2-plugin-alarmcallback-exec/org.graylog2.execalarmcallback.callback.ExecAlarmCallback_gl2plugin.jar) which can be placed in the /plugin/alarm\_callbacks/ directory of your graylog2 server.
