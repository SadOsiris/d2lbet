# Script to produce data for figures in DotA 2 Lounge Betting Analysis
# CC BY-SA-NC 2013.  
# Ben Sauerwine -- http://sauerwine.blogspot.com

# To generate plot 1 data (favor of winning team)
cat data-good | awk '($6==1) {print $7/100} ($6==2) {print $8/100}' > figure1.dat

# To generate plot 2 data (random betting)
#sh trials.sh

# To generate plot 3 data (bet 1 on crowd favorite)
cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($9 < 4)) {tot += $9/4} (($6 == 1) && ($9 > 4)) {tot -= 1} (($6 == 2) && ($12 < 4)) {tot += $12/4} (($6 == 2) && ($12 > 4)) {tot -= 1} {print NR, tot}' > figure3-rares.dat

cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($10 < 4)) {tot += $10/4} (($6 == 1) && ($10 > 4)) {tot -= 1} (($6 == 2) && ($13 < 4)) {tot += $13/4} (($6 == 2) && ($13 > 4)) {tot -= 1} {print NR, tot}' > figure3-uncommons.dat

cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($11 < 4)) {tot += $11/4} (($6 == 1) && ($11 > 4)) {tot -= 1} (($6 == 2) && ($14 < 4)) {tot += $14/4} (($6 == 2) && ($14 > 4)) {tot -= 1} {print NR, tot}' > figure3-commons.dat

# To generate plot 4 data (bet 1 on underdog)
cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($9 > 4)) {tot += $9/4} (($6 == 1) && ($9 < 4)) {tot -= 1} (($6 == 2) && ($12 > 4)) {tot += $12/4} (($6 == 2) && ($12 < 4)) {tot -= 1} {print NR, tot}' > figure4-rares.dat

cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($10 > 4)) {tot += $10/4} (($6 == 1) && ($10 < 4)) {tot -= 1} (($6 == 2) && ($13 > 4)) {tot += $13/4} (($6 == 2) && ($13 < 4)) {tot -= 1} {print NR, tot}' > figure4-uncommons.dat

cat data-good | awk 'BEGIN {tot=0} (($6==1) && ($11 > 4)) {tot += $11/4} (($6 == 1) && ($11 < 4)) {tot -= 1} (($6 == 2) && ($14 > 4)) {tot += $14/4} (($6 == 2) && ($14 < 4)) {tot -= 1} {print NR, tot}' > figure4-commons.dat

# To generate plot 5 data (bet left column / bet right column)
cat data-good | awk 'BEGIN {tot=0} ($6==1) {tot += $9/4} ($6 == 2) {tot -= 1} {print NR, tot}' > figure5-rares-l.dat

cat data-good | awk 'BEGIN {tot=0} ($6==1) {tot += $10/4} ($6 == 2) {tot -= 1} {print NR, tot}' > figure5-uncommons-l.dat

cat data-good | awk 'BEGIN {tot=0} ($6==1) {tot += $11/4} ($6 == 2) {tot -= 1} {print NR, tot}' > figure5-commons-l.dat

cat data-good | awk 'BEGIN {tot=0} ($6==2) {tot += $12/4} ($6 == 1) {tot -= 1} {print NR, tot}' > figure5-rares-r.dat

cat data-good | awk 'BEGIN {tot=0} ($6==2) {tot += $13/4} ($6 == 1) {tot -= 1} {print NR, tot}' > figure5-uncommons-r.dat

cat data-good | awk 'BEGIN {tot=0} ($6==2) {tot += $14/4} ($6 == 1) {tot -= 1} {print NR, tot}' > figure5-commons-r.dat
