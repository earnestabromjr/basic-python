class Logger(object):
    """A file-based message logger with the following properties
    
    Attributes:
        filename (str): The name of the file to which the logger is written.
        level (str): The severity level of the messages to be logged.
        format (str): The format of the message to be logged.
    """
    def __init__(self, file_name):
        """Returns a Logger object whose file_name is *file_name*"""
        self.file_name = file_name

    def _write_log(self, level, msg):
        """Writes a message to the file."""
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}] {msg}\n")

    def critical(self, level, msg):
        self._write_log("CRITICAL", msg)

    def error(self, level, msg):
        self._write_log("ERROR", msg)

    def warn(self, level, msg):
        self._write_log("WARN", msg)

    def info(self, level, msg):
        self._write_log("INFO", msg)

    def debug(self, level, msg):
        self._write_log("DEBUG", msg)
