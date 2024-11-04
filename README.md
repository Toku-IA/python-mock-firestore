# Python Mock Firestore

An in-memory implementation of the [Python client library](https://github.com/googleapis/python-firestore) for Google Cloud Firestore, intended for use in tests to replace the real thing. This project is in early stages and is only a partial implementation of the real client library.

Python 3.10 is required for it to work.

## Usage

```python
db = firestore.Client()
mock_db = MockFirestore()

# Can be used in the same way as a firestore.Client() object would be, e.g.:
db.collection('users').get()
mock_db.collection('users').get()
```

To reset the store to an empty state, use the `reset()` method:

```python
mock_db = MockFirestore()
mock_db.reset()
```

## Running the tests

- Create and activate your virtualenv
- Install dependencies with `pip install -r requirements.txt`
- Run tests with `python -m unittest discover tests -t /`
