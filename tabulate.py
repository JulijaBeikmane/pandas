import requests
from tabulate import tabulate

# 1. Iegūstam datus no ZenQuotes API
response = requests.get("https://zenquotes.io/api/quotes")
if response.status_code == 200:
    data = response.json()
else:
    print("Neizdevās iegūt datus no API.")
    exit()

# 2. Apstrādājam datus, lai iegūtu pirmos 10 citātus
quotes = []
for i, item in enumerate(data[:10], start=1):
    author = item.get("a", "Nezināms autors")
    quote = item.get("q", "Nav citāta")
    first_word = quote.split()[0] if quote else ""
    quotes.append([i, first_word, author, quote])

# 3. Izveidojam un izvadām tabulu
headers = ["Nr.", "Pirmais vārds", "Autors", "Citāts"]
print(tabulate(quotes, headers=headers, tablefmt="grid"))
