# config.py

import logging
import logging.config
import os

def configure_logging():
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    
    log_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': log_level,
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'stock_market.log',
                'formatter': 'default',
                'level': log_level,
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': log_level,
            },
        },
    }

    logging.config.dictConfig(log_config)
