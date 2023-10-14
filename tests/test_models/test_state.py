#!/usr/bin/python3
"""Define unittests for models/state.py

Unittest classes:
    TestState_save
    TestState_to_dict
    TestState_instatiation
"""

import unittest
import models
from datetime import datetime
from time import sleep
from models import storage
from models.state import State
import os

class TestState_save(unittest.TestCase):
    """Test for save method in the state class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save_updates_file(self):
        """Tests for saved Updates within the json file"""
        state = State
        state.save()
        stateid = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(stateid, f.read())

    def test_onetime_save(self):
        state = State()
        sleep(0.5)
        first_updates_at = state.updates_at
        state.save()
        self.assertLess(first_updates_at, state.updates_at)


class TestState_to_dict(unittest.TestCase):
    """Tests for the to_dict method inside the class State."""
    def setUp(self):
        self.state = State()

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstace(state_dict, dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

        self.assertIsInstance(state_dict["id"], str)
        self.assertIsInstance(state_dict["created_at"], str)
        self.assertIsInstance(state_dict["updated_at"], str)

        self.assertEqual(state_dict["id", self.state.id])
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.isoformat())

        self.state.middle_name = "Holberton"
        self.state.my_number = 98
        state_dict = self.state.to_dict()
        self.assertIn("middle_name", state_dict)
        self.assertEqual(state_dict["middle_name"], "Holberton")
        self.assertIn("my_number", state_dict)

        self.assertNotEqual(state_dict, self.state.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.state.to_dict(None)


class TestStateInstatiation(unittest.TestCase):
    """Tests for State Instatiation"""
    def test_instatiation(self):
        state = State()

        self.aessertIsInstance(state, State)
        self.assertIn(state, storage.all().values())

        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(State.name, str)
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

        state2 = State()
        self.assertNotEqual(state.id, state2.id)

        self.asssertNotEqual(state.id, state2.id)

        self.assertLess(state.created_at, state2.created_at)
        self.assertLess(state.updated_at, state2.updated_at)

        dt = datetime.today()
        dt_repr = repr(dt)
        state.id = "456789"
        state.created_at = state.updated_at = dt
        state_str = state.__str__()
        self.assertIn("[State] (456789)", state_str)
        self.assertIn("'id': '456789'", state_str)
        self.assertIn("'created_at': " + dt_repr, state_str)
        self.assertIn("'updated_at': " + dt_repr, state_str)

        state3 = State(id="678", created_at = dt, updated_at = dt)
        self.assertEqual(state3.id, "678")
        self.assertEqual(state3.created_at, dt)
        self.assertEqual(state3.updated_at, dt)

        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

if __name__ == '__main__':
    unittest.main()
