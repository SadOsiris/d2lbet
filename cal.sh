awk 'NR==FNR {a[$2]=$1;next} {print $2,a[$2],$1}' team_good_$1 poor_$1 > poorteamcal
cat poorteamcal | awk 'BEGIN{val=$3} {val/=$2;printf"%s %d %.3f\n",$1,$2,$3/$2}' > poorteamcal$1
awk 'NR==FNR {a[$2]=$1;next} {print $2,a[$2],$1}' team_bad_$1 good_$1 > goodteamcal
cat goodteamcal | awk 'BEGIN{val=$3} {val/=$2;printf"%s %d %.3f\n",$1,$2,$3/$2}' > goodteamcal$1
awk 'NR==FNR {a[$1]=$0;next} {print "should LOSE: "$1,$2,$3," should WIN: "a[$1]}' poorteamcal$1 goodteamcal$1 > myana
cat myana | sort -k 4 | sort -k 5 > analydata
#lose should win
cat poorteamcal$1 | sort -k 2 | sort -k 3 > huai
#win should lose
cat goodteamcal$1 | sort -k 2 | sort -k 3 > hao
rm myana
rm poorteamcal$1
rm goodteamcal$1

