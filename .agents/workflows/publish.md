---
description: Salvataggio modifiche e pubblicazione su GitHub Pages
---

Questo comando si occupa di fare automaticamente il push su GitHub, caricando così gli aggiornamenti in remoto e aggiornando il sito GitHub Pages.

// turbo-all

1. Prepara tutti i nuovi file e le modifiche per il commit
```bash
git add .
```

2. Crea un commit (usiamo un messaggio generico sull'aggiornamento automatico)
```bash
git commit -m "Auto-update website"
```

3. Invia i commit a GitHub sul branch corrente
```bash
git push
```
