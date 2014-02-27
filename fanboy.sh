cat data-good-new | awk -v "i=$1" 'BEGIN{br=0;bc=0}
{if ($2==i){br+=1;print $1,br}}'
