import os
import urllib.request
import ssl

# Ignore SSL verification for simpler downloading
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def run():
    lines = open('tours.md', 'r', encoding='utf-8').readlines()
    in_images = False
    current_folder = ""

    for line in lines:
        if "## 7. Elenco Immagini da Scaricare" in line:
            in_images = True
            
        if not in_images:
            continue

        if "### Cartella:" in line:
            current_folder = line.split("`")[1]
            os.makedirs(current_folder, exist_ok=True)
            print(f"Created/Using directory: {current_folder}")
        
        if line.startswith("| `"):
            parts = line.split("|")
            if len(parts) >= 3:
                filename = parts[1].strip().strip("`").strip()
                url = parts[2].strip()
                
                # Check if it's actually an HTTP URL (avoids header rows if any slipped through)
                if url.startswith("http"):
                    filepath = os.path.join(current_folder, filename)
                    if not os.path.exists(filepath):
                        print(f"Downloading {filename} from {url}")
                        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
                        try:
                            with urllib.request.urlopen(req, context=ctx) as response, open(filepath, 'wb') as out_file:
                                out_file.write(response.read())
                        except Exception as e:
                            print(f"Failed to download {url}: {e}")
                    else:
                        print(f"Already exists: {filepath}")

if __name__ == '__main__':
    run()
