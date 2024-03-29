# Check_MK Plugins

Plugins for Check_MK either based on existing plugins, or newly written.

- 2.2.x plugin version are for CheckMK 2.2
- 2.0.x plugin versions are for CheckMK 2.0/2.1
- 1.x plugin versions are for CheckMK 1.x


[TOC levels=1-5]: #

# Table of Contents
- [Check_MK Plugins](#check_mk-plugins)
- [Installation](#installation)
- [Cisco Small Business Switch Fan Check](#cisco-small-business-switch-fan-check)
- [Netgear Smart Manage Pro Series Switch Fan Check](#netgear-smart-manage-pro-series-switch-fan-check)
- [Netgear Smart Manage Pro Series Switch Temperature Sensors Check](#netgear-smart-manage-pro-series-switch-temperature-sensors-check)
- [Webinject Active Check](#webinject-active-check)
  - [Enhancements](#enhancements)
  - [Installation](#installation-1)
  - [Webinject config files](#webinject-config-files)
  - [check_webinject](#check_webinject)
  - [Username and Password](#username-and-password)
  - [Webinject Config file](#webinject-config-file)
  - [Webinject Test File](#webinject-test-file)
  - [Error: permission denied](#error-permission-denied)
- [Building](#building)
- [Contributors](#contributors)

# Installation
If not otherwise stated, you find the extension mkp files on [exchange.checkmk.com](https://exchange.checkmk.com/u/robertoschwald)

To install, download the .mkp file and upload into your CheckMk Extension Packages page.

# Cisco Small Business Switch Fan Check

cisco_sb_fans is an extension to monitor fan status of Cisco Small Business switches like the SG3x0 series 
which support the CISCOSB-HWENVIROMENT MIB.

You must ensure OID .1.3.6.1.4.1.9.6.1.101.83 is visible by your Check_MK server(s) in the switch config (SNMP View)

Note: 2.0.x version is ONLY compatible with CheckMK 2.0.x. Use an older version of the plugin for CheckMK 1.x

# Netgear Smart Manage Pro Series Switch Fan Check
netgear_smpro_fans is an extension to monitor fan status of NetgearSmart Managed Pro NG700 Series switches like the XS716T.
This check is based on netgear_fans, but with changed OIDs, as the NETGEAR-BOXSERVICES-PRIVATE-MIB is different to the FASTPATH-BOXSERVICES-PRIVATE-MIB.

The fans are auto-detected.


# Netgear Smart Manage Pro Series Switch Temperature Sensors Check
netgear_smpro_temp is an extension to monitor fan status of Netgear Smart Managed Pro NG700 Series switches like the XS716T.
This check is based on netgear_temp, but with changed OIDs, as the NETGEAR-BOXSERVICES-PRIVATE-MIB is different to the FASTPATH-BOXSERVICES-PRIVATE-MIB.

The fans are auto-detected.


# Webinject Active Check
This plugin is an active plugin to be installed on Check_MK Servers based on the webinject plugin of https://github.com/HeinleinSupport/check_mk_extensions.  

## Enhancements
- Packaged check_webinject Nagios check with the package (Version 1.94) which also works in the Check_MK Docker images. The check_webinject nagios test provided by newer Check_MK installations currently does not work in the Docker Check_MK images, as Errors.pm library is missing in the Docker image (checked up to 1.6.0p5). Issue is reported to vendor already.
- Reusable test files, as you can specify the config file name and the test file name. With this, you can use a common test file for many hosts, but webinject config files per host.
- Configure username / password as needed by your webinject tests.

## Installation
1. Upload the [check_webinject-1.2.1.mkp](https://github.com/robertoschwald/check_mk_plugins/releases/download/1.2.1/check_webinject-1.2.1.mkp) extension into your Check_MK instance Extension Packages.
2. Install your webinject config- and test files into the site-user directory etc/webinject of the appliance(s).
   Note: You must upload the files to all Check_MK nodes in CheckMK Enterprise cluster / distributed monitoring manually!
3. Create a new webinject active check rule for your host. 
    - Specify the filenames of the config- and test XML files (without path)   
    - Optionally, define username and password (since 1.2)

## Webinject config files
Do not specify a logfile location in the webinject config file!

## check_webinject
This file is based on webinject 1.94 currently. It contains a workaround for the missing Errors.pm library in the CheckMK Docker 1.6.x images.

## Username and Password
If you need username and password in your test, you can configure them in the active check rule.

Use them as ${USERNAME} and ${PASSWORD} in the test.

## Webinject Config file
You must set reporttype=nagios in the Webinject config file. Do not specify an outputdir, as this is set by the plugin.
Example config file:
```xml
<baseurl>https://www.example.whatever</baseurl>
<reporttype>nagios</reporttype>
<globalhttplog>onfail</globalhttplog>
```

## Webinject Test File
Write your test file as usual. Here, the test used the username and password configured in the active check parameters.
```xml
<testcases repeat="1">
  <case
    id="1"
    description1       = "Initial GET request to {BASEURL}/"
    url                = "{BASEURL}?username=${USERNAME}&password=${PASSWORD}"
    method             = "get"
    verifyresponsecode = "200"
    label              = "demo"
  />
</testcases>
```
## Error: permission denied
If you receive error in the check status:
```
sh: 1: /omd/sites/<your_site>/local/lib/nagios/plugins/check_webinject: Permission denied
```
you might be hit by Check_MK bug [CMK-320](https://mathias-kettner.de/bugs.php?bug_id=CMK-320)

In this case, you must SSH login to the appliance as the site user and change the permission yourself until this gets fixed by the vendor:
```
chmod 755 local/lib/icinga/plugins/check_webinject
```

Note: This extension is not available on [CheckMK Exchange](https://exchange.checkmk.com)

# Building
To build an extension package, call
```
./mkp_packer pack <plugin-dir>
```

# Contributors
Contributors in alphabetical order.

- Daniel Paul
- Robert Oschwald (Project Lead)
