# Installing WeeWX

## Required Skills

In the world of open-source hobbyist software, WeeWX is pretty easy to install and configure. There are not many package dependencies, the configuration is simple, and this guide includes extensive instructions. There are thousands of people who have successfully done an install. However, there is no "point-and-click" interface, so you will have to do some manual configuring.

You should have the following skills:

* The patience to read and follow this guide.
* Willingness and ability to edit a configuration file.
* Some familiarity with Linux or other Unix derivatives.
* Ability to do simple Unix tasks such as changing file permissions and running commands.

No programming experience is necessary unless you wish to extend WeeWX. In this case, you should be comfortable programming in Python.
If you get stuck, there is a very active [User's Group](https://groups.google.com/forum/#!forum/weewx-user) to help.


## Installation Overview
This is an outline of the process to install, configure, and run WeeWX:

* Read the [hardware notes](https://weewx.com/docs/hardware.htm) for your weather station. This will let you know of any features, limitations, or quirks of your hardware.
* Install WeeWX. Use the step-by-step instructions in one of the [installation methods](index.md) below.
* Configure the hardware. This involves setting things like the onboard archive interval, rain bucket size, etc. You may have to follow directions given by your hardware manufacturer, or you may be able to use the utility [wee_device](https://weewx.com/docs/utilities.htm#wee_device_utility).
* Launch the **weewxd** program. It is run from the command line, either as a [daemon](https://weewx.com/docs/usersguide.htm#Running_as_a_daemon), or [directly](https://weewx.com/docs/usersguide.htm#Running_directly).
* Tune the installation. Typically this is done by changing settings in the WeeWX configuration file. For example, you might want to [register your station](https://weewx.com/docs/usersguide.htm#station_registry), so it shows up on a world-wide map of WeeWX installations.
* [Customize](https://weewx.com/docs/customizing.htm) the installation. This is an advanced topic, which allows you to shape WeeWX exactly to your liking!



## Installation methods

There are two general ways of installing WeeWX: using a package installer, or by using pip.

### Package installers

This is the recommended method for beginners.

- One-step install. When done, WeeWX is up and running.
- Requires root privileges to install.
- Requires root privileges to modify.
- Installs in operating system "standard locations."

Here are quick guides for common operating systems:

[Debian-based systems](../debian.md) : For Debian, Ubuntu, Mint, and Raspbian operating  systems.

[Redhat-based RPM systems](../redhat.md): For Redhat, CentOS, Fedora operating systems.

[SuSE-based RPM systems](../suse.md): For SuSE and OpenSUSE.

### Installing using pip

Best for those who intend to customize their system. 

- Supports most operating systems, including macOS.
- Multi-step install.
- Does not require root privileges to install or modify (except for setting up a daemon).
- Installs in "standard locations" for a Python application.
- All user state is held in one location, making backups easy.


## Where to find things

Here is a summary of the layout for the different install methods, along with the symbolic names used for each role. These names are used throughout the documentation.

=== "Debian"

    | Role                    | Symbolic name     | Nominal value                   |
    |-------------------------|-------------------|---------------------------------|
    | WeeWX root directory    | _`$WEEWX_ROOT`_   | `/`                             |
    | Executables             | _`$BIN_ROOT`_     | `/usr/share/weewx/`             |
    | Configuration directory | _`$CONFIG_ROOT`_  | `/etc/weewx/`                   |
    | Skins and templates     | _`$SKIN_ROOT`_    | `/etc/weewx/skins/`             |
    | SQLite databases        | _`$SQLITE_ROOT`_  | `/var/lib/weewx/`               |
    | Web pages and images    | _`$HTML_ROOT`_    | `/var/www/html/weewx/`          |
    | Documentation           | _`$DOC_ROOT`_     | `/usr/share/doc/weewx/`         |
    | Examples                | _`$EXAMPLE_ROOT`_ | `/usr/share/doc/weewx/examples/`|
    | User directory          | _`$USER_ROOT`_    | `/usr/share/weewx/user`                |
    | PID file                |                   | `/var/run/weewx.pid`            |
    | Log file                |                   | `/var/log/syslog`               |

=== "RedHat/SUSE"

    | Role                    | Symbolic name     | Nominal value                          |
    |-------------------------|-------------------|----------------------------------------|
    | WeeWX root directory    | _`$WEEWX_ROOT`_   | `/`                                    |
    | Executables             | _`$BIN_ROOT`_     | `/usr/share/weewx/`                    |
    | Configuration directory | _`$CONFIG_ROOT`_  | `/etc/weewx/`                          |
    | Skins and templates     | _`$SKIN_ROOT`_    | `/etc/weewx/skins/`                    |
    | SQLite databases        | _`$SQLITE_ROOT`_  | `/var/lib/weewx/`                      |
    | Web pages and images    | _`$HTML_ROOT`_    | `/var/www/html/weewx/`                 |
    | Documentation           | _`$DOC_ROOT`_     | `/usr/share/doc/weewx-x.y.z/`          |
    | Examples                | _`$EXAMPLE_ROOT`_ | `/usr/share/doc/weewx-x.y.z/examples/` |
    | User directory          | _`$USER_ROOT`_    | `/usr/share/weewx/user`                |
    | PID file                |                   | `/var/run/weewx.pid`                   |
    | Log file                |                   | `/var/log/syslog`                      |

=== "Pip (including macOS)"
    !!! Note
        Pip install locations are *relative to _`$WEEWX_ROOT`_*

    | Role                    | Symbolic name     | Nominal value                                            |
    |-------------------------|-------------------|----------------------------------------------------------|
    | WeeWX root directory    | _`$WEEWX_ROOT`_   | `~/weewx-data`                                           |
    | Executables             | _`$BIN_ROOT`_     | `~/.local/pipx/venvs/weewx/lib/python3.x/site-packages/` |
    | Configuration directory | _`$CONFIG_ROOT`_  | `./`                                                     |
    | Skins and templates     | _`$SKIN_ROOT`_    | `./skins/`                                               |
    | SQLite databases        | _`$SQLITE_ROOT`_  | `./archive/`                                             |
    | Web pages and images    | _`$HTML_ROOT`_    | `./public_html/`                                         |
    | Documentation           | _`$DOC_ROOT`_     | `./docs`                                                 |
    | Examples                | _`$EXAMPLE_ROOT`_ | `./examples/`                                            |
    | User directory          | _`$USER_ROOT`_    | `./bin/user`                                             |
    | PID file                |                   | `/var/run/weewx.pid`                                     |
    | Log file                |                   | `/var/log/syslog`                                        |