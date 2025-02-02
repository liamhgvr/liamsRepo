#!/bin/zsh
##########
# Aliases
##########
alias ll='ls -l'
alias lla='ll -a'
alias zshconfig="vim ~/.zshrc"
alias envconfig="vim ~/env.sh"
alias path="echo $PATH"
alias ter="terraform"
alias geoip="/usr/local/share/GeoIP/"
alias tellavista='.ssh/keys/tellavista.pem'
alias workoff='deactivate'
alias telladb='ssh -i ~/.ssh/keys/tellavista.pem ubuntu@54.83.139.143'
alias tella='ssh -i ~/.ssh/keys/tellavista.pem ubuntu@54.166.223.138'
alias tellastage='ssh -i ~/.ssh/keys/tellavista.pem ubuntu@50.19.169.238'
alias tellaprod='ssh -i ~/.ssh/keys/tellavista.pem ubuntu@34.198.83.218'
alias test='ssh -i ~/.ssh/keys/test_key.pem  ubuntu@52.17.198.7'
alias ttt='python ~/git/liamsRepo/tick-tack-toe/tick-tack-toe.py'
alias jeff='ssh -i .ssh/keys/test_key.pem ubuntu@52.17.198.7'
alias dircomp='python ~/git/liamsRepo/dir_compare/dir_compare.py'
alias jeff='ssh -i .ssh/keys/keyPair1.pem ubuntu@18.202.76.201'
alias hellojeff='aws ec2 start-instances --instance-ids i-06ec3319a596779f8'
alias byejeff='aws ec2 stop-instances --instance-ids i-06ec3319a596779f8'
alias setme='source git/liamsRepo/env_utilities/liam_conf.sh'
alias setliam='sudo vim git/liamsRepo/env_utilities/liam_conf.sh'
alias py3="python3"

#########
# Export
#########
export PATH="$PATH:/usr/local/bin/python3"
export PATH="$PATH:/Users/liam/git/terraform"
export PATH="$PATH:/usr/local/opt/ncurses/bin"
export PYTHONPATH="/usr/local/bin/python3"
#export EDITOR='subl -w'
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
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

