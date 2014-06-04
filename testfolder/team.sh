cat data-good-new | awk '{print $4,$5}' | tr " " "\n" | sort | uniq | sort > teamlist
