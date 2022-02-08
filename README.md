# System-Monitor
## Dependencies
- python3.10 or higher
- [pyyaml](https://github.com/yaml/pyyaml)
- [psutil](https://github.com/giampaolo/psutil)


## Install
The program is officially only available for Linux. If you want you can adapt the code for Windows or Mac.

### self compile
```bash
git clone https://github.com/Jonas-Luetolf/System-Monitor
cd System-Monitor
make compile
```

### Arch-based:
- download [PKGBUILD](https://github.com/Jonas-Luetolf/System-Monitor/releases/download/v1.0/PKGBUILD)
- execute makepkg -si
(AUR package coming soon)

### Debian-based.
- download [Debian-Package](https://github.com/Jonas-Luetolf/System-Monitor/raw/master/releases/system-monitor_1.0-2_amd64.deb)
- install the Package via ``` sudo apt install <path to file ex. ~/downloads/syystem-monitor_1.0-2_amd64.deb>```

## Options
- --loop outputs the system data repeatedly
- --setconf <file> sets the config file to this file if the configuration is valid

## Config
The config file is written to the directory ~/.config/System-Monitor/config.yaml the first time the program is run.

Not all entries are required by each option, but must still be set.
### The entries are
- update_time (only for --loop)
This entry sets the time until new data is loaded. The number must be an Interger.
example: ```update_time: 2```

- loop_objects (only for --loop)
This entry sets witch data is printed out by the loop function. It must be a list out of strings the strings can be:
  - "cpu" for the CPU data
  - "ram" for the RAM data
  - "disks" for the Disks data
  - "general" for general data

If the config file isn't valid the programm takes the default config.
