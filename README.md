# System-Monitor
## Dependencies
- python3.10 or higher
- [pyyaml](https://github.com/yaml/pyyaml)
- [psutil](https://github.com/giampaolo/psutil)


## Install
### Arch/Manjaro/etc.:
- download [PKGBUILD](https://github.com/Jonas-Luetolf/System-Monitor/releases/download/beta/PKGBUILD)
- execute makepkg -si
(AUR package coming soon)

## Options
- --outputs the system data repeatedly
- --setconf <file> sets the config file to this file if the configuration is valid

## Config
The config file is written to the directory ~/.config/System-Monitor/config.yaml the first time the program is run.

Not all entries are required by each option, but must still be set.
### The entries are
- update_time (only for --loop)
This entry sets the time until new data is loaded

- loop_objects (only for --loop)
This entry sets witch data is printed out by the loop function

- data_load_time 
This entry says how long it takes to load the systemdata.
Don't edit this it will be removed in comming version.
