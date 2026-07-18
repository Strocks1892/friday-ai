from app.indexer.windows_application_indexer import StartMenuIndexer

indexer = StartMenuIndexer()

apps = indexer.scan()

print(f"Found {len(apps)} Start Menu applications.")

for name in list(apps.keys())[:20]:
    print(name)