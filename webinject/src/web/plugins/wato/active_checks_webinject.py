#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) 2019 Robert Oschwald <robertoschwald@gmail.com>
# (c) 2013 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

group = "activechecks"

register_rule(group,
    "active_checks:webinject",
    Tuple(
        title = _("Check webservice with Webinject"),
        help = _("Check the result of a Webinject test plan. "),
        elements = [
            TextAscii(
                  title = _("Webinject config file name"),
                  allow_empty = False,
                  help = _('The name of the Webinject configuration XML file in ~sitename/etc/webinject/, e.g. myhost_config.xml')
            ),
            TextAscii(
                  title = _("Webinject test file name"),
                  allow_empty = False,
                  help = _('The name of the Webinject test XML file in ~sitename/etc/webinject/, e.g. myhost_test.xml')
            ),
            Dictionary(
                title = ("Optional parameters"),
                elements = [
                    ( "username",
                      TextAscii(
                          title = _("Username"),
                          help = _("The username you want to login as. Is forwarded as USERNAME param to the test."),
                          size = 30)
                      ),
                    ( "password",
                      Password(
                          title = _("Password"),
                          help = _("The password you want to use for that user. Is forwarded as PASSWORD param to the test."),
                          size = 30)
                      ),
                ]
            )
        ]
    ),
    match = 'all')
