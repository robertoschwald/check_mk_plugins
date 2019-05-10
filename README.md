# Check_MK Plugins

Plugins for Check_MK either based on existing plugins, or newly written.

# webinject
This plugin is an active plugin to be installed on Check_MK Servers based on the webinject plugin of https://github.com/HeinleinSupport/check_mk_extensions.  

## Enhancements
- Re-Usable test files, as you can specify the config file name and the test file name. With this, you can use the same test file, but config files per host
- Environment variables support
 - Configure arbitrary environment variables needed by your webinject tests (e.g. username, password). This is handy if you use common webinject test files for several hosts.

## Installation
1. Installation the mkp package into your Check_MK instance Extension Packages. 
2. Install your webinject config- and test files into the site-user directory /etc/webinject of the appliance(s).
   Note: You must copy the files to all Check_MK servers in a cluster manually!
3. Create a new webinject active check rule for your host. 
    - Specify the filenames of the config- and test XML files (without path)   
    - Define as many environment variables as you need (comming soon)

# Webinject config files
Do not specify a logfile location in the webinject config file!

