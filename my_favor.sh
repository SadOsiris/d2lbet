# Script to produce data for figures in DotA 2 Lounge Betting Analysis
# CC BY-SA-NC 2013.  
# Ben Sauerwine -- http://sauerwine.blogspot.com
#1gameid 2.WinT          3.LoseT         4.1stT          5.2ndT  6.IndofW        7.left%         8.Right%        9LK 10LR 11LU 12LC 13RC 14RU 15RR 16RK         BO
#1gameid 2.WinT          3.LoseT         4.1stT          5.2ndT  6.IndofW        7.left%         8.Right%        9LR 10LU 11LC 12RC 13RU 14RR          BO


# To generate plot 1 data (favor of winning team)
cat data-good-new | awk '($6==1) {print $7/100} ($6==2) {print $8/100}' > myfigure1.dat

# To generate plot 2 data (random betting)
#sh trials.sh

# To generate plot 3 data (bet 1 on crowd favorite)


cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7>50)) {tot += $9} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $14} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7>50)) {tot += $10} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $15} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure3-rares.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7>50)) {tot += $10} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $13} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7>50)) {tot += $11} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $14} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure3-uncommons.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7>50)) {tot += $11} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $12} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7>50)) {tot += $12} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $13} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure3-commons.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==17){if(($6==1) && ($7>50)) {tot += $9} else if(($6 == 1) && ($7<50)){tot -= 4} else if(($6 == 2) && ($7 < 50)) {tot += $16} else if(($6 == 2) && ($7 > 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure3-keys.dat

# To generate plot 4 data (bet 1 on underdog)

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7<50)) {tot += $9} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $14} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7<50)) {tot += $10} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $15} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure4-rares.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7<50)) {tot += $10} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $13} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7<50)) {tot += $11} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $14} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure4-uncommons.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if(($6==1) && ($7<50)) {tot += $11} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $12} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{if(NF==17){if(($6==1) && ($7<50)) {tot += $12} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $13} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure4-commons.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==17){if(($6==1) && ($7<50)) {tot += $9} else if(($6 == 1) && ($7>50)){tot -= 4} else if(($6 == 2) && ($7 > 50)) {tot += $16} else if(($6 == 2) && ($7 < 50)) {tot -= 4}}}
{print NR,$1,tot}' > myfigure4-keys.dat

# To generate plot 5 data (bet left column / bet right column)

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==17){if($6==1) {tot += $9} else if($6 == 2) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-keys-l.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==1) {tot += $9} else if($6 == 2) {tot -= 4} }}
{if(NF==17){if($6==1) {tot += $10} else if($6 == 2) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-rares-l.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==1) {tot += $10} else if($6 == 2) {tot -= 4} }}
{if(NF==17){if($6==1) {tot += $11} else if($6 == 2) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-uncommons-l.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==1) {tot += $11} else if($6 == 2) {tot -= 4} }}
{if(NF==17){if($6==1) {tot += $12} else if($6 == 2) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-commons-l.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==2) {tot += $12} else if($6 == 1) {tot -= 4} }}
{if(NF==17){if($6==2) {tot += $13} else if($6 == 1) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-commons-r.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==2) {tot += $13} else if($6 == 1) {tot -= 4} }}
{if(NF==17){if($6==2) {tot += $14} else if($6 == 1) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-uncommons-r.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==15){if($6==2) {tot += $14} else if($6 == 1) {tot -= 4} }}
{if(NF==17){if($6==2) {tot += $15} else if($6 == 1) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-rares-r.dat

cat data-good-new | awk 'BEGIN {tot=0} 
{if(NF==17){if($6==2) {tot += $16} else if($6 == 1) {tot -= 4} }}
{print NR,$1,tot}' > myfigure5-keys-r.dat

