# Argile 06

Site d'information (statique, sans serveur) sur le retrait-gonflement des argiles, pour Vence et les Alpes-Maritimes.

## Voir en local
    cd ~/argiles-info && python3 -m http.server 8791
puis ouvrir http://127.0.0.1:8791

## Modifier les pages
Les pages HTML sont générées par `tools/gen_pages.py` (contenu, menu, pied de page) :

    python3 tools/gen_pages.py

Avant publication, remplacer `CONTACT` (adresse de contact) dans ce script puis regénérer.

## Données personnelles
Ne jamais committer ni publier d'adresse, de nom ou de numéro de dossier. Le site n'enregistre rien.

## Publier (GitHub Pages)
Voir les commandes données avec la v1.
