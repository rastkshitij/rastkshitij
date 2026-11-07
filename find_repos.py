import urllib.request, json
req = urllib.request.Request('https://api.github.com/users/rastkshitij/repos?per_page=100', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=8) as r:
    repos = json.load(r)
    print(f'Total public repos: {len(repos)}')
    for repo in repos:
        name = repo['name']
        print(f"  {name} -> {repo['html_url']}")

