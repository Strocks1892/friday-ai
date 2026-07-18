from app.indexer.uwp_indexer import UWPIndexer

apps = UWPIndexer().scan()
print(apps["netflix"])

print("Discord:", "discord" in apps)
print("Google Chrome:", "google chrome" in apps)
print("OBS Studio:", "obs studio" in apps)
print("Netflix:", "netflix" in apps)
print("Google Play Games:", "google play games" in apps)
print("Visual Studio Code:", "visual studio code" in apps)