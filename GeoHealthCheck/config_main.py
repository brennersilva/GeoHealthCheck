# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2014 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

DEBUG = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
# Alternative configuration for PostgreSQL database
SQLALCHEMY_DATABASE_URI = 'postgresql://bsilva:bs@localhost:5432/digitearth'

# Replace None with 'your secret key string' in quotes
SECRET_KEY = '2fba43844e7f4766fcf4e656df5a7243ef705995f63758ac'

GHC_RETENTION_DAYS = 30
GHC_PROBE_HTTP_TIMEOUT_SECS = 30
GHC_MINIMAL_RUN_FREQUENCY_MINS = 10
GHC_SELF_REGISTER = False
GHC_NOTIFICATIONS = True
GHC_NOTIFICATIONS_VERBOSITY = True
GHC_WWW_LINK_EXCEPTION_CHECK = False
GHC_ADMIN_EMAIL = 'digitalearth2019@gmail.com'
GHC_NOTIFICATIONS_EMAIL = ['digitalearth2019@gmail.com']
GHC_SITE_TITLE = 'GeoHealthCheck for Digital Earth'
GHC_SITE_URL = 'http://localhost:8000'
GHC_RUNNER_IN_WEBAPP = False
GHC_REQUIRE_WEBAPP_AUTH = True
# 10=DEBUG 20=INFO 30=WARN(ING) 40=ERROR 50=FATAL/CRITICAL
GHC_LOG_LEVEL = 30
GHC_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Some GetCaps docs are huge. This allows
# caching them for N seconds. Set to -1 to
# disable caching.
GHC_METADATA_CACHE_SECS = 900

GHC_SMTP = {
    'server': 'smtp.gmail.com',
    'port': 587,
    'tls': True,
    'ssl': False,
    'username': 'digitalearth2019',
    'password': 'digitalEarth2019*'
}

GHC_RELIABILITY_MATRIX = {
    'red': {
        'min': 0,
        'max': 49
    },
    'orange': {
        'min': 50,
        'max': 79
    },
    'green': {
        'min': 80,
        'max': 100
    }
}

GHC_MAP = {
    'url': 'https://tile.osm.org/{z}/{x}/{y}.png',
    'centre_lat': 55.0,
    'centre_long': 5.0,
    'maxzoom': 18,
    'subdomains': 1234,
}

# GHC Core Plugins
# Each GHC Plugin should derive from GeoHealthCheck.plugin.Plugin,
# and should be findable in sys/PYTHONPATH.
# An entry may be a Python classname or module.
# The latter will include all classes derived from GeoHealthCheck.plugin.Plugin
# in the module file.
GHC_PLUGINS = [
    # Probes
    'GeoHealthCheck.plugins.probe.owsgetcaps',
    'GeoHealthCheck.plugins.probe.wms',
    'GeoHealthCheck.plugins.probe.wfs',
    'GeoHealthCheck.plugins.probe.tms',
    'GeoHealthCheck.plugins.probe.http',
    'GeoHealthCheck.plugins.probe.sta',
    'GeoHealthCheck.plugins.probe.wmsdrilldown',
    'GeoHealthCheck.plugins.probe.wfs3',
    'GeoHealthCheck.plugins.probe.esrifs',
    'GeoHealthCheck.plugins.probe.ghcreport',

    # Checkers
    'GeoHealthCheck.plugins.check.checks',

    # Resource Auth Plugins
    'GeoHealthCheck.plugins.resourceauth.resourceauths',
]

# Entry for User Plugins: will be added to default core GHC_PLUGINS
# This makes it easier for users to just configure their Plugins
# and always get the latest core GHC_PLUGINS without having to upgrade
# their config.
GHC_USER_PLUGINS = []

# Default Probe to assign on "add" per Resource-type
GHC_PROBE_DEFAULTS = {
    'OGC:WMS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.WmsGetCaps'
    },
    'OGC:WMTS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.WmtsGetCaps'
    },
    'OSGeo:TMS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.tms.TmsCaps'
    },
    'OGC:WFS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.WfsGetCaps'
    },
    'OGC:WCS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.WcsGetCaps'
    },
    'OGC:WPS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.WpsGetCaps'
    },
    'OGC:CSW': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.CswGetCaps'
    },
    'OGC:SOS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.owsgetcaps.SosGetCaps'
    },
    'OGC:STA': {
        'probe_class': 'GeoHealthCheck.plugins.probe.sta.StaCaps'
    },
    'OGC:WFS3': {
        'probe_class': 'GeoHealthCheck.plugins.probe.wfs3.WFS3Drilldown'
    },
    'ESRI:FS': {
        'probe_class': 'GeoHealthCheck.plugins.probe.esrifs.ESRIFSDrilldown'
    },
    'urn:geoss:waf': {
        'probe_class': 'GeoHealthCheck.plugins.probe.http.HttpGet'
    },
    'WWW:LINK': {
        'probe_class': 'GeoHealthCheck.plugins.probe.http.HttpGet'
    },
    'FTP': {
        'probe_class': None
    },
    'OSGeo:GeoNode': {
        'probe_class': None
    },
    'GHC:Report': {
        'probe_class':
            'GeoHealthCheck.plugins.probe.ghcreport.GHCEmailReporter'
    }
}
