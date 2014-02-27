rm badteamcount team_bad_$1
cat data-good | awk 'BEGIN {tot=0}{if($7>"'$1'"){print $5}}{if($8>"'$1'"){print $4}} '> badteamcount
cat badteamcount | sort | uniq -c | sort -n > team_bad_$1

