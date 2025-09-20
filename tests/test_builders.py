import json
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from builders.builder import Layout, Visualization, Encoding

def test_example1():
    spec = Visualization().mark("bar").add_encoding(
        Encoding().channel("x", "category").channel("y", "value").channel("color", "region")
    ).build()

    with open("examples/example1.json") as f:
        expected = json.load(f)

    assert spec == expected

def test_example2():
    spec = Layout().direction("vertical").gap("10px") \
        .add_child(Visualization().mark("line").add_encoding(
            Encoding().channel("x", "time").channel("y", "sales"))) \
        .add_child(Visualization().mark("area").add_encoding(
            Encoding().channel("x", "month").channel("y", "revenue"))).build()

    with open("examples/example2.json") as f:
        expected = json.load(f)

    assert spec == expected

def test_style_b_channel_field():
    spec = Visualization().mark("point").add_encoding(
        Encoding().channel("x").field("foo").channel("y").field("bar")
    ).build()

    expected = {
        "type": "visualization",
        "mark": "point",
        "encoding": {"x": "foo", "y": "bar"}
    }

    assert spec == expected
