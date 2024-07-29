while inotifywait -e modify,create,delete -r .git; do
    clear
    git log --oneline
done