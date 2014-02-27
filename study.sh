# Script to gather data for DotA 2 Lounge betting analysis.
# CC BY-SA-NC 2013.  
# Ben Sauerwine -- http://sauerwine.blogspot.com

rm data-good
rm data-fail

# In the next line, you should set the range of DotA match IDs you want.  
# Currently, this is set up to scan the first 400 matches.  
for (( i=1100; i<=1662; ++i)) ; do
  echo $i
  #sleep 1 # Just to throttle a little bit, totally optional.  Remove this line if you want.
  wget http://www.dota2lounge.com/match?m=$i -O match.htm

  # To get the winning team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print $1}' | grep win | awk '{print substr($0, 0, length($0)-6)}' | tr -d "_" > winning-team

  # To get the losing team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print $1}' | grep -v win | tr -d "_" > losing-team

  # To get the first team on the list
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <(" "_  " | awk '{print $1}' | tr -d "_" | head -n 1 > first-team

  # To get the second team on the list
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <(" "_  " | awk '{print $1}' | tr -d "_" | tail -n 1 > second-team

  # To get the index of the winning team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr " <" "_ " | awk '{print NR, $1}' | grep "(win)" | awk '{print $1}' > winning-team-idx

  # To get the %favor for the left team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr -d " " | tr "<>" "  " | awk '{print $5}' | tr -d "%" | head -n 1 > favor-left

  # To get the %favor for the right team
  cat match.htm | grep team -A 1 | grep span | grep -v steam | awk '{print substr($0, 10)}' | tr -d " " | tr "<>" "  " | awk '{print $5}' | tr -d "%" | tail -n 1 > favor-right

  # To get the odds (for 4) in Rares, Uncommons and Commons for left team and right team.  e.g.:
  # LeftRares LeftUncommons leftCommons RightRares RightUncommons RightCommons
  cat match.htm | tr "<>" "\n\n" | grep "for 4" | awk '{print $1}' | tr "\n" " " | awk '{print $0}' > odds


  # best of
  cat match.htm | grep "Best" | awk '{print $8}' | awk -F '<' '{print $1}' > bo


  echo $i > idx

  paste idx winning-team losing-team first-team second-team winning-team-idx favor-left favor-right odds bo| awk '(NF==15) {print}' >> data-good
  paste idx winning-team losing-team first-team second-team winning-team-idx favor-left favor-right odds bo| awk '(NF!=15) {print}' >> data-fail

  rm match.htm
done
