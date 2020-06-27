# -*- coding: utf-8 -*-

# Handy utility functions for Kodi Addons
# By bossanova808
# Free in all senses....
# VERSION 0.1
# (Matrix on)

import xbmc
import xbmcaddon
import sys
import traceback

ADDON = xbmcaddon.Addon()
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_AUTHOR = ADDON.getAddonInfo('author')
ADDON_VERSION = ADDON.getAddonInfo('version')
ADDON_ARGUMENTS = str(sys.argv)
CWD = ADDON.getAddonInfo('path')
LANGUAGE = ADDON.getLocalizedString
KODI_VERSION = xbmc.getInfoLabel('System.BuildVersion')
USER_AGENT = "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr; rv:1.9.0.1) Gecko/2008070208 Firefox/3.6"


def log(message, exception_instance=None, level=xbmc.LOGDEBUG):
    """
    Log a message to the Kodi debug log, if debug logging is turned on.

    :param message: required, the message to log
    :param exception_instance: optional, an instance of some Exception
    :param level: optional, the Kodi log level to use, default LOGDEBUG
    """

    message = f'### {ADDON_NAME} {ADDON_VERSION} - {message}'
    message_with_exception = message + f' ### Exception: {traceback.format_exc(exception_instance)}'

    if exception_instance is None:
        xbmc.log(message, level)
    else:
        xbmc.log(message_with_exception, level)


def log_notice(message, exception_instance=None):
    """
    Log a message at the LOGNOTICE level, i.e. even if Kodi debugging is not turned on. Use sparingly.

    :param message: required, the message to log
    :param exception_instance: optional, an instance of some Exception
    """

    log(message, exception_instance, level=xbmc.LOGNOTICE)


def footprints(startup=True):
    """
    Log the startup of an addon, and key Kodi details that are helpful for debugging

    :param startup: optional, default True.  If true, log the startup of an addon, otherwise log the exit.
    """
    if startup:
        log_notice(f'Starting...')
        log_notice(f'Kodi Version: {KODI_VERSION}')
        log_notice(f'Addon arguments: {ADDON_ARGUMENTS}')
    else:
        log_notice(f'Exiting...')


def set_property(window, name, value=""):
    """
    Set a property on a window.
    To clear a property, provide an empty string

    :param window: Required.  The Kodi window on which to set the property.
    :param name: Required.  Name of the property.
    :param value: Optional (defaults to "").  Set the property to this value.  An empty string clears the property.
    """
    window.setProperty(name, value)
    # if value and value != False and value != 'na.png':
    #     log(f'Set window property: [{name}] - value: [{value}]')


def send_kodi_json(human_description, json_string):
    """
    Send a JSON command to Kodi, logging the human description, command, and result returned.

    :param human_description: Required. A human sensible description of what the command is aiming to do/retrieve.
    :param json_string: Required. The json command to send.
    """
    log(f'KODI JSON RPC command: {human_description} [{json_string}]')
    result = xbmc.executeJSONRPC(json_string)
    log(f'KODI JSON RPC result: {str(result)}')

