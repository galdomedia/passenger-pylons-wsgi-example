"""Setup the passenger-pylons-wsgi-example application"""
import logging

from passengerpylonswsgiexample.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup passengerpylonswsgiexample here"""
    load_environment(conf.global_conf, conf.local_conf)
