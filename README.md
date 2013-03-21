graylog2-plugin-alarmcallback-exec
==================================

A graylog-server plugin that executes a command.

The alarm topic, description and message count are passed to the process in the environment.

| Variable name       | Contents                | 
| ------------------- | ----------------------- |
| GL2\_TOPIC          | The alarm topic         |
| GL2\_DESCRIPTION    | The alarm description   |
| GL2\_MESSAGE\_COUNT | The alarm message count |
