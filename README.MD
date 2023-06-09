
# [uLauncher](https://github.com/Ulauncher/Ulauncher) remove Apt packages

### Little tool written in python to remove Apt packages using uLauncher.

<p align="center">
   <img src="https://ulauncher-ext-images-prod.nyc3.digitaloceanspaces.com/github|17218425/2023-05-06T05:03:48.200357.png" />
</p>

# Installation
Open uLauncher preferences window -> extensions -> add extension and paste the following url:
`https://github.com/khanghy3004/ulauncher-remove-apt-packages`

## Start up 
Start uLauncher and type `rm`. <br>
To search type `rm -> name of the package or using arrows, enter to delete`.

## Scrolling(kinda)
To "scroll" type `rm -> write number to show packages further down`.

### Currently
* No error handling
* No success prompt
* Sudo prompts for every package, exits uLauncher

## Development
Git clone this repo.

In repo folder do `make link` to create symlink to ulauncher extensions folder.

Close uLauncher and run `make dev` and follow instructions in terminal.

You will get code that looks something like this:
```
VERBOSE=1 ULAUNCHER_WS_API=ws://127.0.0.1:5054/ulauncher-remove-apt-packages PYTHONPATH=/usr/lib/python3/dist-packages /usr/bin/python3 /home/hy/.local/share/ulauncher/extensions/ulauncher-remove-apt-packages/main.py
```
Paste it in new terminal window and run keyword `rm` in uLauncher. 
Happy coding!



# Credits
#### This extension uses uLauncher as main driver https://github.com/Ulauncher/Ulauncher
