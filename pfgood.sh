rm goodteamcount team_good_$1
cat data-good | awk 'BEGIN {tot=0}{if($7>"'$1'"){print $4}}{if($8>"'$1'"){print $5}} '> goodteamcount
cat goodteamcount | sort | uniq -c | sort -n > team_good_$1

