# Check_MK Plugins

Plugins for Check_MK either based on existing plugins, or newly written.

# webinject
This plugin is an active plugin to be installed on Check_MK Servers based on the webinject plugin of https://github.com/HeinleinSupport/check_mk_extensions.  

## Enhancements
- Re-Usable test files, as you can specify the config file name and the test file name. With this, you can use the same test file, but config files per host
- Environment variable support
 - Configure arbitrary environment variables needed by your tests (e.g. username, password). This is handy if you use common webinject test files for several hosts.

## Usage
- Copy your webinject config files and test files into the site-user directory /etc/webinject of the appliance(s).
Note: You must copy the files to all Check_MK servers in a cluster.

Do not specify a logfile location in the webinject config file!

