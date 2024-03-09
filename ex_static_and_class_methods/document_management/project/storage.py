from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        try:
            category = next(filter(lambda c: c.name == category.name, self.categories))
        except StopIteration:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        try:
            topic = next(filter(lambda t: t.id == topic.id, self.topics))
        except StopIteration:
            self.topics.append(topic)

    def add_document(self, document: Document):
        try:
            document = next(filter(lambda d: d.id == document.id, self.documents))
        except StopIteration:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document)

    def get_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return document

    def __repr__(self):
        return ', '.join([str(d) for d in self.documents])
