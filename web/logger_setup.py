# import logging


# stream_logger = logging.basicConfig(level=logging.DEBUG)

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")    
# logging.error("This is an error message")
# logging.critical("This is a critical message")



# import logging


# stream_logger = logging.getLogger("stream_logger")
# stream_logger.setLevel(logging.DEBUG)

# stream_logger.handlers = []
# stream_logger = logging.StreamHandler()

# stream_logger.setLevel(logging.DEBUG)

# stream_logger.debug("This is a debug message")
# stream_logger.info("This is an info message")
# stream_logger.warning("This is a warning message")    
# stream_logger.error("This is an error message")
# stream_logger.critical("This is a critical message")

# Handlers are advanced ways to manage and route logs. Handlers define the output 
# destinations for log messages, allowing you to control where the log data 
# goes, such as writing to files, sending emails, or printing to the console. 

import logging


# stream_logger = logging.getLogger("stream_logger")
# stream_logger.setLevel(logging.DEBUG)

# stream_logger.handlers = []
# stream_logger = logging.StreamHandler()

# stream_logger.setLevel(logging.DEBUG)

# stream_logger.debug("This is a debug message")
# stream_logger.info("This is an info message")
# stream_logger.warning("This is a warning message")    
# stream_logger.error("This is an error message")
# stream_logger.critical("This is a critical message")

# Handlers are advanced ways to manage and route logs. Handlers define the output 
# destinations for log messages, allowing you to control where the log data 
# goes, such as writing to files, sending emails, or printing to the console. 

stream_logger = logging.getLogger('stream_logger')

stream_logger.setLevel(logging.DEBUG)  # Set logger to capture all messages from DEBUG level and above

# Ensure no previous handlers are attached

stream_logger.handlers = []

# Creating a StreamHandler

stream_handler = logging.StreamHandler()

stream_handler.setLevel(logging.INFO)  # Set handler to display only messages from INFO level and above

# Adding handler to logger

stream_logger.addHandler(stream_handler)

# Logging messages at different levels

stream_logger.debug("This is a DEBUG message for stream_logger.")

stream_logger.info("This is an INFO message for stream_logger.")

stream_logger.warning("This is a WARNING message for stream_logger.")

stream_logger.error("This is an ERROR message for stream_logger.")

stream_logger.critical("This is a CRITICAL message for stream_logger.")