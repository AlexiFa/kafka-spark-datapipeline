#!/bin/bash

# Lancer Docker Compose en arrière-plan
docker compose down

docker compose up -d

# Attendre que les conteneurs soient prêts (ajustez le délai si nécessaire)
Start-Sleep -Seconds 10

# Lancer le premier script Python (celui qui écoute) en arrière-plan
Start-Process python -ArgumentList "src/consumer.py" -NoNewWindow

Start-Sleep -Seconds 5

# Lancer le second script Python (celui qui envoie les données)
python "src/producer.py"

# Attendre que tous les processus en arrière-plan se terminent
Start-Sleep -Seconds 20