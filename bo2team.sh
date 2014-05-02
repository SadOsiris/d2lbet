cat bo2-new | awk '{print $4,$5}' | tr " " "\n" | sort | uniq -c | sort -n > bo2list
