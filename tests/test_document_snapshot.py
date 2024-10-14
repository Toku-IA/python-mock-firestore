from unittest import TestCase

from mockfirestore import MockFirestore


class TestDocumentSnapshot(TestCase):
    def test_documentSnapshot_toDict(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertEqual({"id": 1}, doc.to_dict())

    def test_documentSnapshot_toDict_isolation(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc_dict = fs.collection("foo").document("first").get().to_dict()
        fs._data["foo"]["first"]["id"] = 2
        self.assertEqual({"id": 1}, doc_dict)

    def test_documentSnapshot_exists(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertTrue(doc.exists)

    def test_documentSnapshot_exists_documentDoesNotExist(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("second").get()
        self.assertFalse(doc.exists)

    def test_documentSnapshot_reference(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc_ref = fs.collection("foo").document("second")
        doc_snapshot = doc_ref.get()
        self.assertIs(doc_ref, doc_snapshot.reference)

    def test_documentSnapshot_id(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertIsInstance(doc.id, str)

    def test_documentSnapshot_create_time(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertIsNotNone(doc.create_time)

    def test_documentSnapshot_update_time(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertIsNotNone(doc.update_time)

    def test_documentSnapshot_read_time(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1}}}
        doc = fs.collection("foo").document("first").get()
        self.assertIsNotNone(doc.read_time)

    def test_documentSnapshot_get_by_existing_field_path(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1, "contact": {"email": "email@test.com"}}}}
        doc = fs.collection("foo").document("first").get()
        self.assertEqual(doc.get("contact.email"), "email@test.com")

    def test_documentSnapshot_get_by_non_existing_field_path(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1, "contact": {"email": "email@test.com"}}}}
        doc = fs.collection("foo").document("first").get()
        with self.assertRaises(KeyError):
            doc.get("contact.phone")

    def test_documentSnapshot_get_in_an_non_existing_document(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1, "contact": {"email": "email@test.com"}}}}
        doc = fs.collection("foo").document("second").get()
        self.assertIsNone(doc.get("contact.email"))

    def test_documentSnapshot_get_returns_a_copy_of_the_data_stored(self):
        fs = MockFirestore()
        fs._data = {"foo": {"first": {"id": 1, "contact": {"email": "email@test.com"}}}}
        doc = fs.collection("foo").document("first").get()
        self.assertIsNot(doc.get("contact"), fs._data["foo"]["first"]["contact"])

    def test_documentSnapshot_to_dict_returns_none_when_exists_false(self):
        fs = MockFirestore()
        fs._data = {"foo": {}}
        doc = fs.collection("foo").document("first").get()
        self.assertIs(doc.to_dict(), None)

    def test_documentSnapshot_get_raises_error_for_single_digits(self):
        fs = MockFirestore()
        fs._data = {"foo": {"bar": {"3": "value"}}}
        doc = fs.collection("foo").document("bar").get()

        with self.assertRaises(ValueError):
            doc.get("3")
