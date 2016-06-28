# scubatools
Python Package containing various tools to aid dive planning.  Including:
* Gas decanting calculator
* NOAA CNS & OTU tables and functions
* MOD, best mix/bailout functions
* Summary functions for printing reports etc

## Installation
Install git & python onto your machine and clone this repo somewhere in pythons path. 
#### E.g. cmdline install for Windows 7 (assuming you followed default installs for python and git)...
Assumes you installed python for only the current user, if you installed python as an administrator, you will need to modify the file/folder permissions in order to sucessfully clone the repo into site-packages.

    cd C:\Users\Admin\AppData\Local\Programs\Python\Python35-32\lib\site-packages
    git clone https://github.com/w3s7y/scubatools.git

Then open idle or just run python off the command line and start using the package!

#### E.g. install on a Linux OS
Python can be installed in many places on UNIX like operating systems, do the following 

    python     # Start python
    import sys
    print(sys.path)
    Ctrl+D     # Quit back to shell prompt

This should print a list of all the directories in pythons path. 

    cd /usr/lib/python3.5    # Or whichever directory you found on the path you want to install to
    git clone https://github.com/w3s7y/scubatools.git
    
## Usage
Please see the Wiki pages on github <https://github.com/w3s7y/scubatools/wiki>
    
