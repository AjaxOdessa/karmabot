cmd="$HOME/bin/python3/bin/python3.5 main.py"
until $cmd; do
    echo "Slack bot crashed with exit code $?. Respawning.." >&2
    sleep 1
done
