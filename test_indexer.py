from app.indexer.application_indexer import ApplicationIndexer
from app.indexer.application_finder import ApplicationFinder

indexer = ApplicationIndexer()
indexer.build_index()

finder = ApplicationFinder()

print(finder.find("discord"))