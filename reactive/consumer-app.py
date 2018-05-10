#!/usr/bin/python

import pwd
import os
from subprocess import call
from charmhelpers.core import host
from charmhelpers.core.hookenv import log, status_set, config
from charmhelpers.core.templating import render
from charms.reactive import when, when_not, set_flag, clear_flag, when_file_changed, endpoint_from_flag
from charms.reactive import Endpoint

###########################################################################
#                                                                         #
# Installation of apache + waiting for generic-database (provider) charm  #
#                                                                         #
###########################################################################

@when('apache.available')
def finishing_up_setting_up_sites():
    host.service_reload('apache2')
    set_flag('apache.start')


@when('apache.start')
@when_not('endpoint.generic-database.connected')
def waiting_for_db():
    host.service_reload('apache2')
    status_set('maintenance', 'Waiting for generic database relation')


########################################################################
#                                                                      #
# Request of database technology to generic-database (provider charm)  #
#                                                                      #
########################################################################


@when('endpoint.generic-database.joined')
def request_db():
    endpoint = endpoint_from_flag('endpoint.generic-database.joined')
    endpoint.request('postgresql')
    status_set('maintenance', 'Requesting postgresql')


##################################################
#                                                #
# Request successful, get data and render config # 
#                                                #
##################################################


@when('endpoint.generic-database.postgresql.available')
def pgsql_render_config():
    """
    The generic-database represents a pgsql database. This function will render the config file in order to use the pgsql database.
    Configuration details: host(), port(), databasename(), user(), password() 
    """
    
    pgsql = endpoint_from_flag('endpoint.generic-database.postgresql.available')

    render_template('pgsql-config.j2', '/var/consumer-app/test.html', {
        'gdb_host' : pgsql.host(),
        'gdb_port' : pgsql.port(),
        'gdb_dbname' : pgsql.databasename(),
        'gdb_user' : pgsql.user(),
        'gdb_password' : pgsql.password(),
    })
    set_flag('endpoint.generic-database.connected')
    set_flag('restart-app')


@when('restart-app')
def restart_app():
    host.service_reload('apache2')
    clear_flag('restart-app')
    status_set('active', 'App ready')
