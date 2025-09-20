import json

class Encoding:
    def __init__(self):
        self.channels = {}
        self._current = None  # store last channel name if using .field()

    def channel(self, name, field=None):
        """
        Two usage styles:
        1. channel("x", "time")
        2. channel("x").field("time")
        """
        self._current = name
        if field is not None:
            # Style A: both name and field in one call
            self.channels[name] = field
            self._current = None
        return self

    def field(self, value):
        """
        Used only when called after channel("x")
        Example: channel("x").field("time")
        """
        if self._current is None:
            raise ValueError("Call channel(name) before field(value)")
        self.channels[self._current] = value
        self._current = None
        return self

    def build(self):
        if self._current is not None:
            raise ValueError(f"Incomplete encoding: missing field() for channel '{self._current}'")
        return self.channels

class Visualization:
    def __init__(self):
        self.data = {"type": "visualization"}
    def mark(self, mark_type):
        self.data["mark"] = mark_type
        return self
    def add_encoding(self, encoding):
        self.data["encoding"] = encoding.build()
        return self
    def build(self):
        return self.data

class Layout:
    def __init__(self):
        self.data = {"type": "layout", "children": []}
    def direction(self, dir):
        self.data["direction"] = dir
        return self
    def gap(self, g):
        self.data["gap"] = g
        return self
    def add_child(self, child):
        self.data["children"].append(child.build())
        return self
    def build(self):
        return self.data
