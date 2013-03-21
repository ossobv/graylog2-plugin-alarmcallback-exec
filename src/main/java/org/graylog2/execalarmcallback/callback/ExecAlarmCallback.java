package org.graylog2.execalarmcallback.callback;

import java.util.HashMap;
import java.util.Map;
import org.graylog2.plugin.alarms.Alarm;
import org.graylog2.plugin.alarms.callbacks.AlarmCallback;
import org.graylog2.plugin.alarms.callbacks.AlarmCallbackConfigurationException;
import org.graylog2.plugin.alarms.callbacks.AlarmCallbackException;

/**
 * @author Harm Geerts <hgeerts@osso.nl>
 */
public class ExecAlarmCallback implements AlarmCallback {

    public static final String NAME = "Exec alarm callback";
    
    private String cmd;
    
    public void initialize(Map<String, String> config) throws AlarmCallbackConfigurationException {
        if (config == null || !config.containsKey("cmd") || config.get("cmd").isEmpty()) {
            throw new AlarmCallbackConfigurationException("Required config parameter cmd is missing.");
        }
        
        this.cmd = config.get("cmd");
    }

    public void call(Alarm alarm) throws AlarmCallbackException {
	ExecTrigger trigger = new ExecTrigger(this.cmd);
	trigger.trigger(alarm);
    }

    public Map<String, String> getRequestedConfiguration() {
        Map<String, String> config = new HashMap<String, String>();
        config.put("cmd", "Executable command with arguments");
        return config;
    }
    
    public String getName() {
        return NAME;
    }
}

// vim: set ts=8 sw=4 sts=4 et ai:
