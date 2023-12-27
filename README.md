# Clone this repo...
## Set up git ssh keys
```
ssh-keygen -t rsa -b 4096 -C "sethimcclaine@gmail.com"
```

https://github.com/settings/keys

## Clone the repo
```
mkdir ~/Documents/WorkSpace
cd ~/Documents/WorkSpace
git clone git@github.com:sethimcclaine/RPi.git
```

## Set zshrc to symbolic link so we can track it in git
```
ln -sf ~/Documents/WorkSpace/RPi/RPiConfigs/.zshrc ~/.zshrc
. ~/.zshrc
```

## Run zshrc command to finish setup
```
initialSetup
```

# Install zshrc
```
sudo apt-get install zsh
```
```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

## Do I still need this?
Update Git to use vim on commit
  `git config --global core.editor "vim"`
