import json
from view_model_create_category import ViewModelCreateCategory
from repository import Repository

def list_categories():
    repository = Repository("listCategories")
    result = repository.connect_with_db()
