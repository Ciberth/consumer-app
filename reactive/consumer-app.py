#!/usr/bin/python

import pwd
import os
from subprocess import call
from charmhelpers.core import host
from charmhelpers.core.hookenv import log, status_set, config
from charmhelpers.core.templating import render
from charms.reactive import when, when_not, set_flag, clear_flag, when_file_changed

# todo here @when_not('generic-database.concrete')
# for when a new consumer app connects to a generic database that is not generic anymore
@when('generic-database.joined')
def request_db():
    endpoint = endpoint_from_flag('gneric-database.joined')
    endpoint.request('postgresql')
    status_set('maintenance', 'Requesting postgresql')



@when('generic-database.pgsql.available')
def pgsql_render_config():
    """
    The generic-database represents a pgsql database. This function will render the config file in order to use the pgsql database.
    Configuration details: host(), port(), databasename(), user(), password() 
    """
    
    pgsql = endpoint_from_flag('generic-database.pgsql.available')

    render_template('pgsql-config.j2', '/var/consumer-app/test.html', {
        'gdb_host' : pgsql.host(),
        'gdb_port' : pgsql.port(),
        'gdb_dbname' : pgsql.databasename(),
        'gdb_user' : pgsql.user(),
        'gdb_password' : pgsql.password(),
    })
    set_flag('restart-app')


@when('restart-app')
def restart_app():
    host.service_reload('apache2')
    clear_flag('restart-app')
    status_set('active', 'App ready')
