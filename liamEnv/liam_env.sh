#!/bin/zsh
##########
# Aliases
##########
alias lla='ll -a'
alias zshconfig="vim ~/.zshrc"
alias envconfig="vim ~/env.sh"
alias path="echo $PATH"
alias terr="terraform"
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
alias tellalogs='ssh -i ~/.ssh/keys/tellavista.pem ubuntu@34.198.83.218 "bash /home/ubuntu/devops-scripts/logs_bkp_n_del.sh"'
alias space='sudo du -cha --max-depth=1 /var | grep -E "M|G"'
alias dircomp='python ~/git/liamsRepo/dir_compare/dir_compare.py'

#########
# Export
#########
export USER_NAME="LIAM?"
export PATH="/usr/local/share/python:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
export PATH="$/Users/liam/Library/Python/2.7/bin:$PATH"
export PATH="/Users/liam/terraform_ex:$PATH"
export PATH="/usr/local/opt/ncurses/bin:$PATH"
export PYTHONPATH="/usr/local/opt/python@2/bin/python2.7:$PYTHONPATH"
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
