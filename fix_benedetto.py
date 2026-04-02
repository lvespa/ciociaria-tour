import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("da Norcia a Montecassino", "da Cassino a Norcia a ritroso")
text = text.replace("from Norcia to Montecassino", "backwards from Cassino to Norcia")
text = text.replace("Ripercorre le tappe della vita del Santo. Uno dei cammini spirituali", "Ripercorre a ritroso le tappe della vita del Santo, partendo da Cassino verso Norcia. Uno dei cammini spirituali")
text = text.replace("Retraces the stages of the Saint's life. One of the most significant", "Retraces the stages of the Saint's life backwards, starting from Cassino to Norcia. One of the most significant")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)


# Update tour-cammino-san-benedetto.html
with open('tour-cammino-san-benedetto.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Details sidebar
text = text.replace('">Norcia</span', '">Cassino</span')
text = text.replace('">Montecassino</span', '">Norcia</span')

# Descriptions
text = text.replace("Ripercorre le tappe della vita del Santo. Uno dei cammini spirituali più significativi d'Europa, tra boschi e abbazie, da Norcia a Montecassino.", 
                    "Ripercorre a ritroso le tappe della vita del Santo. Uno dei cammini spirituali più significativi d'Europa, tra boschi e abbazie, partendo da Cassino fino a Norcia.")
text = text.replace("Retraces the stages of the Saint's life. One of the most significant spiritual paths in Europe, through woods and abbeys, from Norcia to Montecassino.", 
                    "Retraces the stages of the Saint's life backwards. One of the most significant spiritual paths in Europe, through woods and abbeys, starting from Cassino ending in Norcia.")

# Program IT exactly as found in tour-cammino-san-benedetto.html
prog_it_old = """<ul class="program-list">
        <li>Partenza da Norcia (Umbria)</li>
        <li>Arrivo a Rieti e Valle Santa</li>
        <li>Attraversamento dei borghi ciociari</li>
        <li>Arrivo trionfale all'Abbazia di Montecassino</li>
        <li>Rilascio della credenziale del pellegrino</li>
      </ul>"""

prog_it_new = """<ul class="program-list">
        <li>Partenza dall'Abbazia di Montecassino</li>
        <li>Attraversamento dei borghi ciociari</li>
        <li>Arrivo a Rieti e Valle Santa</li>
        <li>Arrivo trionfale a Norcia (Umbria)</li>
        <li>Rilascio della credenziale del pellegrino</li>
      </ul>"""

# Program EN exactly as found
prog_en_old = """<ul class="program-list" data-lang="en" style="display:none;">
        <li>Departure from Norcia (Umbria)</li>
        <li>Arrival in Rieti and Holy Valley</li>
        <li>Crossing Ciociaria villages</li>
        <li>Triumphant arrival at Montecassino Abbey</li>
        <li>Issuance of pilgrim credential</li>
      </ul>"""

prog_en_new = """<ul class="program-list" data-lang="en" style="display:none;">
        <li>Departure from Montecassino Abbey</li>
        <li>Crossing Ciociaria villages</li>
        <li>Arrival in Rieti and Holy Valley</li>
        <li>Triumphant arrival in Norcia (Umbria)</li>
        <li>Issuance of pilgrim credential</li>
      </ul>"""

text = text.replace(prog_it_old, prog_it_new)
text = text.replace(prog_en_old, prog_en_new)

with open('tour-cammino-san-benedetto.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update tours.md
with open('tours.md', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("| Partenza | Norcia (PG) |", "| Partenza | Cassino |")
text = text.replace("| Arrivo | Abbazia di Montecassino |", "| Arrivo | Norcia (PG) |")
text = text.replace("da Norcia a Montecassino.", "a ritroso da Cassino a Norcia.")
text = text.replace("- Norcia · Cascia · Leonessa (Umbria)\\n- Rieti · Greccio · Poggio Bustone\\n- Sora · Arpino · Atina (Ciociaria)\\n- Cassino · **Abbazia di Montecassino ✦ META FINALE**",
"- Cassino · Abbazia di Montecassino\\n- Sora · Arpino · Atina (Ciociaria)\\n- Rieti · Greccio · Poggio Bustone\\n- **Norcia · Cascia · Leonessa (Umbria) ✦ META FINALE**")

with open('tours.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Benedetto reversed path updated.")
