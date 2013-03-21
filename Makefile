.PHONY: all install clean

PKG = target/graylog2-alarmcallback-exec-0.10.0.jar
SOURCES = src/main/java/org/graylog2/execalarmcallback/callback/ExecAlarmCallback.java src/main/java/org/graylog2/execalarmcallback/callback/ExecTrigger.java
DEST = /usr/share/graylog2-server

all: $(PKG)

clean:
        $(RM) -r target

install: $(PKG)
        $(RM) $(DEST)/plugin/alarm_callbacks/org.graylog2.execalarmcallback.callback.ExecAlarmCallback_gl2plugin.jar
        cp -a $(PKG) $(DEST)/plugin/alarm_callbacks/org.graylog2.execalarmcallback.callback.ExecAlarmCallback_gl2plugin.jar

$(PKG): $(SOURCES)
        mvn package
