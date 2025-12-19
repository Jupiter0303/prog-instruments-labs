import logging.config


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'detailed': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
        }
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout'
        },


        'debug_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': 'crypto_debug.log',
            'encoding': 'utf-8'
        },


        'error_file': {
            'class': 'logging.FileHandler',
            'level': 'WARNING',
            'formatter': 'detailed',
            'filename': 'crypto_errors.log',
            'encoding': 'utf-8'
        }
    },

    'loggers': {
        'CryptoApp': {
            'level': 'DEBUG',
            'handlers': ['console', 'debug_file', 'error_file'],
            'propagate': False
        }
    },

    'root': {
        'level': 'WARNING',
        'handlers': []
    }
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger('CryptoApp')