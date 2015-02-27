graylog2-plugin-alarmcallback-exec
==================================

THIS CODE IS UNMAINTAINED
-------------------------

*WARNING: This code works on Graylog 0.10, not on 0.20 or any later version.*

Please see
[biz.dfch.j.graylog2.plugin.alarm.execscript](https://github.com/dfch/biz.dfch.j.graylog2.plugin.alarm.execscript)
for an up to date version that works -- as of this writing -- with Graylog 1.0.

See graylog2-plugin-alarmcallback-exec github issue #4.

Your old exec scripts won't work with the the _dfch_ version,
but you should be able to quickly get something started with
something like this:

    runCommand('/path/to/some-script.py',
               {env: {GL2_STREAM: (''+stream.getTitle()),
                      GL2_DESCRIPTION: (''+result.getResultDescription())}})


Readme
------

A graylog-server plugin that executes a command.
The command is configurable in the graylog plugin system settings.

The alarm topic and description are passed to the process environment.

| Variable name       | Contents                | 
| ------------------- | ----------------------- |
| GL2\_TOPIC          | The alarm topic         |
| GL2\_DESCRIPTION    | The alarm description   |

Examples
--------

[Python example](examples/graylog-email-alert.py) script that retrieves
the stream id from the mongo database using the alarm topic and queries
elasticsearch for the last log messages on that stream. The log messages
are sent to the email addresses specified on the command line.  Plugin
configuration: graylog-email-alert.py alert@example.com more@example.com

Prebuilt Download
-----------------

For your convenience a prebuilt jar is available for
[download](https://downloads.osso.nl/Graylog2/graylog2-plugin-alarmcallback-exec-0.10/org.graylog2.execalarmcallback.callback.ExecAlarmCallback_gl2plugin-2.jar)
which can be placed in the /plugin/alarm\_callbacks/ directory of your
graylog2 server.

*There have been reports that you need to remove the "-2" from the
filename before graylog2 detects it.*
