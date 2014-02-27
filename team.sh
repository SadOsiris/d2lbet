cat data-good | awk '{print $4,$5}' | tr " " "\n" | sort | uniq -c | sort -n > team_count
