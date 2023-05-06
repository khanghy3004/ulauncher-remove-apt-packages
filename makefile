
EXT_NAME:=com.github.khanghy3004.ulauncher-remove-arch-packages
EXT_DIR:=$(shell pwd)

link: 
	ln -s ${EXT_DIR} ~/.local/share/ulauncher/extensions/${EXT_NAME}

dev: 
	ulauncher --no-extensions --dev -v | grep "ulauncher-remove-apt-packages"

.PHONY:link dev 

