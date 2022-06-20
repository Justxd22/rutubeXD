# /bin/bash


if [ -f .env ]; then set -o allexport; source .env; set +o allexport ; echo "using env!" ; fi

python3 /tube/bot.py
