# Check_MK Plugins

Plugins for Check_MK either based on existing plugins, or newly written.

# Webinject Active Check
This plugin is an active plugin to be installed on Check_MK Servers based on the webinject plugin of https://github.com/HeinleinSupport/check_mk_extensions.  

## Enhancements
- Packaged check_webinject Nagios check with the package (Version 1.94)
- Reusable test files, as you can specify the config file name and the test file name. With this, you can use a common test file for many hosts, but webinject config files per host.
- Configure arbitrary environment variables as needed by your webinject tests (e.g. username, password). This is handy if you use a common webinject test file for several hosts (coming soon)

## Installation
1. Upload the mkp package into your Check_MK instance Extension Packages.  (coming soon)
2. Install your webinject config- and test files into the site-user directory /etc/webinject of the appliance(s).
   Note: You must copy the files to all Check_MK servers in a cluster manually!
3. Create a new webinject active check rule for your host. 
    - Specify the filenames of the config- and test XML files (without path)   
    - Optionally, define as many environment variables as you need (coming soon)

## Webinject config files
Do not specify a logfile location in the webinject config file!

## check_webinject
This file is based on webinject 1.94 currently.

## Error: permission denied
If you use the Check_MK virtual appliance and receive error
```
sh: 1: /omd/sites/<your_site>/local/lib/nagios/plugins/check_webinject: Permission denied
```
you might be hit by Check_MK bug CMK-320.

In this case, you must SSH login to the appliance as the site user and change the permission yourself until this gets fixed by the vendor:
```
chmod 755 local/lib/icinga/plugins/check_webinject
```
