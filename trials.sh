# Script to perform random betting simulations for DotA 2 Lounge Betting Analysis.
# CC BY-SA-NC 2013.  
# Ben Sauerwine -- http://sauerwine.blogspot.com

#!/bin/bash
rm trials-common
rm trials-uncommon
rm trials-rare

for (( c=1; c<=600; c++ )) {
echo $c
  cat data-good | awk -v c=$c 'BEGIN {srand(c)} {t += (($6 == 1 + int(rand() * 2)) ? (($6 == 1) ? $9 : $12)/4 : -1)} END {print t}' >> trials-rare
  cat data-good | awk -v c=$c 'BEGIN {srand(c)} {t += (($6 == 1 + int(rand() * 2)) ? (($6 == 1) ? $10 : $13)/4 : -1)} END {print t}' >> trials-uncommon
  cat data-good | awk -v c=$c 'BEGIN {srand(c)} {t += (($6 == 1 + int(rand() * 2)) ? (($6 == 1) ? $11 : $14)/4 : -1)} END {print t}' >> trials-common
}

