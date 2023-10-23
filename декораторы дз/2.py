from functools import lru_cache
from tinydb import TinyDB

class Database:
    def __init__(self, db_name):
        self.db = TinyDB(db_name)

    @lru_cache(maxsize=None)  
    def get_document_by_id(self, doc_id):
        print(f"Getting document with ID {doc_id} from the database.")
        return self.db.get(doc_id=doc_id)

    @lru_cache(maxsize=None)
    def search_documents_by_keyword(self, keyword):
        print(f"Searching documents containing '{keyword}' in the database.")
        return self.db.search(Query().content.search(keyword))

db = Database('my_database.json')

print(db.get_document_by_id(1)) 
print(db.get_document_by_id(1)) 
print(db.search_documents_by_keyword("python")) 
print(db.search_documents_by_keyword("python")) 
