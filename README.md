# Clone this repo...
## Set up git ssh keys
```
ssh-keygen -t rsa -b 4096 -C "sethimcclaine@gmail.com"
```

https://github.com/settings/keys
## Install git if its not available (OS Lite)
```
sudo apt install git
```

## Clone the repo
```
mkdir ~/Documents/WorkSpace
cd ~/Documents/WorkSpace
git clone git@github.com:sethimcclaine/RPi.git
```

## Install zshrc
```
sudo apt-get install zsh
```
```
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
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

# Minning
## Montero (XMR) - https://www.youtube.com/watch?v=hHtGN_JzoP8
### Get xmrig repo
```
sudo apt update
sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev
git clone git@github.com:xmrig/xmrig.git
cd xmrig
```
### update donations (Optional)
```
vi src/donate.h
```
Change levels to `0`

### Build 
```
mkdir build
cd build
cmake ..
make
```
### Start
* Alias `minePiA` `minePiB`
* Call `./xmring -o {pool} -u {wallet_address} -p{worker_name}`
  * pool: `gulf.moneroocean.stream:10128`
  * wallet_address: `45GWXJrhsJNfRfaAkYVeNCUA8SBo1TkLvjRbDE66Na8kYUnfQA1QavRhQnvFZL7NRdGRXWpWacMxSEQrvNiWP5jZHEQGQNA`
  * worker_name: `rpi5a` (whatever we want to call it)

