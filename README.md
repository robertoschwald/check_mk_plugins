# Check_MK Plugins

Plugins for Check_MK either based on existing plugins, or newly written.

# Cisco Small Business Switch Fan Check
cisco_sb_fans is an extension to monitor fan status of Cisco Small Business switches like the SG300 series using SNMP.

You must ensure OID .1.3.6.1.4.1.9.6.1.101.83 is visible by your Check_MK server(s) in the switch config (SNMP View)

# Cisco Small Business Switch Temperature Check
Coming soon.

# Webinject Active Check
This plugin is an active plugin to be installed on Check_MK Servers based on the webinject plugin of https://github.com/HeinleinSupport/check_mk_extensions.  

## Enhancements
- Packaged check_webinject Nagios check with the package (Version 1.94)
- Reusable test files, as you can specify the config file name and the test file name. With this, you can use a common test file for many hosts, but webinject config files per host.
- Configure username / password as needed by your webinject tests.

## Installation
1. Upload the mkp package into your Check_MK instance Extension Packages.
2. Install your webinject config- and test files into the site-user directory etc/webinject of the appliance(s).
   Note: You must upload the files to all Check_MK servers in a cluster manually!
3. Create a new webinject active check rule for your host. 
    - Specify the filenames of the config- and test XML files (without path)   
    - Optionally, define username and password (since 1.2)

## Webinject config files
Do not specify a logfile location in the webinject config file!

## check_webinject
This file is based on webinject 1.94 currently.

## Username and Password
If you need username and password in your test, you can configure them in the active check rule.

Use them as ${USERNAME} and ${PASSWORD} in the test.

# Webinject Config file
You must set reporttype=nagios in the Webinject config file. Do not specify an outputdir, as this is set by the plugin.
Example config file:
```xml
<baseurl>https://www.example.whatever</baseurl>
<reporttype>nagios</reporttype>
<globalhttplog>onfail</globalhttplog>
```

# Webinject Test File
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
you might be hit by Check_MK bug CMK-320.

In this case, you must SSH login to the appliance as the site user and change the permission yourself until this gets fixed by the vendor:
```
chmod 755 local/lib/icinga/plugins/check_webinject
```
