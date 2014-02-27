rm goodteamtest
cat data-good | awk 'BEGIN {tot=0}{if(($7>"'$1'")&&($6==2)){print $5}}{if(($8>"'$1'")&&($6==1)){print $4}} '> goodteamtest
cat goodteamtest | sort | uniq -c | sort -n > good_$1

