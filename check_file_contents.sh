while true; do
  sleep 1
  curr=$(cat clipboard_register.txt)
  if [[ "$prev" != "$curr" ]]; then
    prev=$curr
    echo "$curr"
  fi
done
