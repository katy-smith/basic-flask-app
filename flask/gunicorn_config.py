bind = "0.0.0.0:9090"  # Specify the IP address and port to bind to
workers = 4  # Number of Gunicorn worker processes
timeout = 120  # Timeout value in seconds

# Logging configuration
accesslog = "-"  # Print access logs to stdout
errorlog = "-"  # Print error logs to stdout
loglevel = "info"  # Log level: debug, info, warning, error, critical
