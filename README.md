# Clone this repo...

`ssh-keygen -t rsa -b 4096 -C "sethimcclaine@gmail.com"`

https://github.com/settings/keys

## Install zshrc
```
sudo apt-get install zsh
```
```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

## Set zshrc to symbolic link so we can track it in git
```
ln -s ~/Documents/WorkSpace/RPi/RPiConfigs/.zshrc ~/.zshrc
```

## Run zshrc command to finish setup
```
initialSetup
```


Update Git to use vim on commit
  `git config --global core.editor "vim"`
