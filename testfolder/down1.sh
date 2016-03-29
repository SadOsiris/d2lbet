# Script to gather data for DotA 2 Lounge betting analysis.
# CC BY-SA-NC 2013.  
# Ben Sauerwine -- http://sauerwine.blogspot.com

#rm data-good-new
#rm data-fail-new

# In the next line, you should set the range of DotA match IDs you want.  
# Currently, this is set up to scan the first 400 matches.  




for i in `seq $1 $1`  ; 

do
  echo $i
  #sleep 1 # Just to throttle a little bit, totally optional.  Remove this line if you want.
  wget http://dota2lounge.com/match?m=$i -O match.htm

  # To get the winning team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print $1}' | grep win | awk -F'_' '{print $1}' > winning-team

  # To get the losing team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print $1}' | head -n 2 | grep -v win | tr -d "_" > losing-team

  # To get the first team on the list
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <(" "_  " | awk '{print $1}' | tr -d "_" | head -n 1 > first-team

  # To get the second team on the list
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <(" "_  " | awk '{print $1}' | head -n 2 | tr -d "_" | tail -n 1 > second-team

  # To get the index of the winning team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print NR, $1}' | grep "(win)" | awk '{print $1}' > winning-team-idx

  # To get the %favor for the left team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr -d " " | tr "<>" "  " | awk '{print $5}' | tr -d "%" | head -n 1 > favor-left

  # To get the %favor for the right team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr -d " " | tr "<>" "  " | awk '{print $5}' | head -n 2 | tr -d "%" | tail -n 1 > favor-right

  # To get the odds (for 4) in Rares, Uncommons and Commons for left team and right team.  e.g.:
  # LeftRares LeftUncommons leftCommons RightRares RightUncommons RightCommons
  cat match.htm | tr "<>" "\n\n" | grep "for 1" | awk '{print $1}' | tr "\n" " " | awk '{print $0}' > odds


  # best of
  cat match.htm | grep "Best" | awk '{print $8}' | head -1 | awk -F '<' '{print $1}' > bo

  echo $i > idx
if [ `ls -l winning-team | awk '{print $5}'` -eq 0 ]
then
 echo ping > winning-team
 echo ping > losing-team
 echo 0 > winning-team-idx
else

#  paste idx winning-team losing-team first-team second-team winning-team-idx favor-left favor-right odds bo| awk '(NF==15) {print}' >> data-good-new
#  paste idx winning-team losing-team first-team second-team winning-team-idx favor-left favor-right odds bo| awk '(NF==17) {print}' >> data-good-new
#  paste idx winning-team losing-team first-team second-team winning-team-idx favor-left favor-right odds bo| awk '(NF!=15 && NF!=17) {print}' >> data-fail-new
  paste winning-team>>updatedteam
  paste losing-team>>updatedteam
fi
done

