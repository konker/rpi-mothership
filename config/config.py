import os

config = {
    # paths relative from this config file
    "logfile": os.path.realpath(os.path.join(os.path.dirname(__file__),
                                '..', 'log', 'rpi-mothership.log')),
    "datafile": os.path.realpath(os.path.join(os.path.dirname(__file__),
                                 '..', 'data', 'rpi-mothership.db')),

    #[TODO]
    "debug": True,

    "http_host": "0.0.0.0",
    "http_port": 9500,

    #[TODO]
    "ssl_cert": None,
    "ssl_key": None,
}

