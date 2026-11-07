import re, urllib.request

with open('README.md', encoding='utf-8') as f:
    text = f.read()

urls = re.findall(r'https?://[^\s"\'<>\)]+', text)
print(f'Checking {len(set(urls))} unique URLs:')
for u in sorted(set(urls)):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            print(f'OK [{r.status}]: {u}')
    except Exception as e:
        print(f'ERR [{e}]: {u}')
