import requests
from fake_useragent import UserAgent

user_agent = UserAgent()

# fake that we're using the Chrome web browser...
header = {'user-agent': user_agent.chrome}

page = requests.get('https://www.google.com', headers=header)

print(page.content)

# Sometimes you need a wait() for a slow server.
page = requests.get('https://www.google.com', timeout=3)



