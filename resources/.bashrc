# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# Load the modules
module purge
module load python
module load pgi/20.9
module load git
module load vim
#source activate astro_base

# Define costom commands
alias cdd='cd /data/OOXX' # Fill in OOXX by your name
alias CDA='conda deactivate'
alias CA='conda activate astro_base'
alias FolderSize='du -h --max-depth=1 | sort -hr'
alias ll='ls -al -h'

export PATH=${HOME}/bin:${PATH}
