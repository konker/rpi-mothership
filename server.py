#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#
# rpi-mothership
#
# Copyright 2012 Konrad Markus
#
# Author: Konrad Markus <konker@gmail.com>
#

import sys

import pathhack
import logging
from optparse import OptionParser
import daemon

# NOTE: edit config.rb as appropriate
from config.config import config
from http.http import HttpServer
from util.pidfile import PidFile


def main():
    parser = OptionParser()
    parser.add_option('--debug', '-d', action='store_true', default=False,
                      help='log debugging messages too')

    parser.add_option('--log-stderr', '-l', dest='log_stderr',
                      action='store_true', default=False,
                      help='force log messages to stderr')

    parser.add_option('--foreground', '-f', dest='foreground',
                      action='store_true', default=False,
                      help='do not run as daemon')

    options, args = parser.parse_args()
    if args:
        parser.error('incorrect number of arguments')

    if options.foreground:
        server(options)
    else:
        # NOTE: the pidfile path must be the same as $PIDFILE in the init.d script
        with daemon.DaemonContext(pidfile=PidFile('/var/run/rpi-mothership.pid')):
            server(options)


def server(options):
    # configure logging
    if options.debug or config.get('debug', False):
        if options.log_stderr:
            logging.basicConfig(level=logging.DEBUG,
                                stream=sys.stderr,
                                format='%(asctime)s [%(threadName)s] %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        else:
            logging.basicConfig(level=logging.DEBUG,
                                filename=config['logfile'],
                                format='%(asctime)s [%(threadName)s] %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
    else:
        if options.log_stderr:
            logging.basicConfig(level=logging.INFO,
                                stream=sys.stderr,
                                format='%(asctime)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        else:
            logging.basicConfig(level=logging.INFO,
                                filename=config['logfile'],
                                format='%(asctime)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')

    # start http server
    http_server = HttpServer(config)
    http_server.start(config['http_host'], config['http_port'])


if __name__ == '__main__':
    main()


