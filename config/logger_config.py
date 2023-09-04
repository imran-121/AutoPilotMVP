def get_log_config(log_file_suffix: str = "") -> dict:
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console_formatter": {
                "format_old": "%(levelname)s - %(message)s",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "file_formatter": {
                "format_old": "%(asctime)s - %(levelname)s - %(message)s",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console_handler": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "console_formatter",
                "stream": "ext://sys.stdout"
            },
            "debug_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "file_formatter",
                "filename": f"info{'_' + log_file_suffix if log_file_suffix else ''}.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            },
            "error_file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "file_formatter",
                "filename": f"error{'_' + log_file_suffix if log_file_suffix else ''}.log",
                "maxBytes": 10485760,
                "backupCount": 20,
                "encoding": "utf8"
            }
        },
        "root": {
            "level": "INFO",
            "handlers": [
                "console_handler",
                "debug_file_handler",
                "error_file_handler"
            ]
        }
    }
