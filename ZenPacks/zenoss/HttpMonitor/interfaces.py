###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
from Products.Zuul.interfaces import IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class IHttpMonitorDataSourceInfo(IRRDDataSourceInfo):
    timeout = schema.Int(title=_t(u'Timeout (seconds)'))
    cycletime = schema.Int(title=_t(u'Cycle Time (seconds)'))
    hostname = schema.TextLine(title=_t(u'Host Name'), group=_t('HTTP Monitor'))
    port = schema.Int(title=_t(u'Port'), group=_t('HTTP Monitor'))
    ipAddress = schema.TextLine(title=_t(u'IP Address or Proxy Address'), group=_t('HTTP Monitor'))
    url = schema.TextLine(title=_t(u'URL'), group=_t('HTTP Monitor'))
    useSsl = schema.Bool(title=_t(u'Use SSL?'), group=_t('HTTP Monitor'))
    regex = schema.TextLine(title=_t(u'Regular Expression'), group=_t('HTTP Monitor'))
    caseSensitive = schema.Bool(title=_t(u'Case Sensitive'), group=_t('HTTP Monitor'))
    basicAuthUser = schema.TextLine(title=_t(u'Basic Auth User'), group=_t('HTTP Monitor'))
    invert = schema.Bool(title=_t(u'Invert Expression'), group=_t('HTTP Monitor'))
    basicAuthPass = schema.Password(title=_t(u'Basic Auth Password'), group=_t('HTTP Monitor'))
    onRedirect = schema.Choice(title=_t(u'Redirect Behavior'),
                             vocabulary='httpMonitorRedirectVocabulary', group=_t('HTTP Monitor'))
    proxyAuthUser = schema.TextLine(title=_t(u'Proxy User'), group=_t('Proxy Credentials'))
    proxyAuthPassword = schema.Password(title=_t(u'Proxy Password'), group=_t('Proxy Credentials'))

