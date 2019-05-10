import unittest
import json
import sys
sys.path.append('../')
from app import db, app
class test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        self.app = app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(self):
        db.drop_all()

    def Create(self):
        print("Creating New Pokemon")
        send = {
            "pokemon": {
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
            }
        }

        recieve = {
            "pokemon": {
                "cardColours": {
                    "fg": "#111111",
                     "bg": "#222222",
                    "desc": "#333333"
                }
                "id":1,
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
            }
        }

        self.app.post("http://localhost:8006/api/pokemon", data=json.dumps(send),
                                    content_type='application/json')
        original= self.app.get("http://localhost:8006/api/pokemon")
        print(original)
        self.assertEqual(recieve, json.loads(original.data))
        print("Create Pokemon Test Successful")

    def Get(self):
        print("Reading Pokemon Details")
        send = {
            "pokemon": {
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
            }
        }

        recieve = {
            "pokemon": {
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
                "id": 1,
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
            }
        }

        self.app.post("http://localhost:8006/api/pokemon", data=json.dumps(send),
                                    content_type='application/json')
        original = self.app.get("http://localhost:8006/api/pokemon/1")
        print(original)
        self.assertEqual(recieve, json.loads(original.data))
        print("View Pokemon Test Successful")

    def Delete(self):
        print("Deleting Pokemon Details")
        create_send = {
            "pokemon": {
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
            }
        }

        delete_recieve = {
            "pokemon": {
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
                "id": 1,
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
            }
        }

        self.app.post("http://localhost:8006/api/pokemon", data=json.dumps(create_send),content_type='application/json')
        original = self.app.delete("http://localhost:8006/api/pokemon/1")
        print(original)
        self.assertEqual(delete_recieve, json.loads(original.data))
        print("Delete Pokemon Test Successful")

    def test_Update(self):
        print("Updating Pokemon Details")
        create_send = {
            "pokemon": {
                "name": "test-pokemon",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
            }
        }

        update_send ={
            "pokemon": {
                "name": "real-charmender"
            }
        }

        update_recieve = {
            "pokemon": {
                "cardColours": {
                    "fg": "#111111",
                    "bg": "#222222",
                    "desc": "#333333"
                }
                "id": 1,
                "name": "real-charmender",
                "sprite": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/test.png",
            }

        }

        self.app.post("http://localhost:8006/api/pokemon", data=json.dumps(create_send),content_type='application/json')
        original = self.app.patch("http://localhost:8006/api/pokemon/1"')
        print(original)
        self.assertEqual(update_recieve, json.loads(original.data))
        print("Pokemon Details Updated")
        print("Updating Pokemon Test Successful")

if __name__ == '__main__':
    unittest.main()
