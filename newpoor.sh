rm poorteamtest
cat data-good | awk 'BEGIN {tot=0}{if(($7>"'$1'")&&($6==2)){print $4}}{if(($8>"'$1'")&&($6==1)){print $5}} '> poorteamtest
cat poorteamtest | sort | uniq -c | sort -n > poor_$1



