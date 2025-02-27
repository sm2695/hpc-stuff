alias myq='squeue -u sumalw'
alias slurmkillall="squeue -h -u sumalw -o %A | xargs -n1 scancel"
alias uquota='lfs quota -hp $UID /cfs/klemming'
alias pquota='lfs quota -hp `stat -c "%g" /cfs/klemming/projects/snic/itma-2022` /cfs/klemming'


