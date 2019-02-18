#!/bin/zsh

# Path
export PATH="/usr/local/share/python:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export PATH="$/Users/liam/Library/Python/2.7/bin:$PATH"
export PATH="/Users/liam/terraform_ex:$PATH"
export PATH="/usr/local/opt/ncurses/bin:$PATH"

# Python
export PYTHONPATH="/usr/local/opt/python@2/bin/python2.7:$PYTHONPATH"

# Other Exporets
#export EDITOR='subl -w'
export PYTHONPATH=$PYTHONPATH:/usr/local/bin/python
# export MANPATH="/usr/local/man:$MANPATH"
export JAVA_HOME="`/usr/libexec/java_home -v 1.8`"

# Virtual Environment
#export WORKON_HOME=$HOME/.virtualenvs
#export PROJECT_HOME=$HOME/projects
#source /usr/local/bin/virtualenvwrapper.sh
workon liam

# Git
git config --global user.name "liam156"
git config --global user.email "liamhgvr@gmail.com"
git config --global credential.helper "osxkeychain"

# Owner
export USER_NAME="LIAM?"
#eval "$(rbenv init -)"

# FileSearch
function f() { find . -iname "*$1*" ${@:2} }
function r() { grep "$1" ${@:2} -R . }

#mkdir and cd
#function mkcd() { mkdir -p "$@" && cd "$_"; }

# Set
set LDFLAGS='-L/usr/local/opt/ncurses/lib'
set CPPFLAGS='-I/usr/local/opt/ncurses/include'

