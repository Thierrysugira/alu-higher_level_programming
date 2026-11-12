# Python - Inheritance

This directory contains projects on Python inheritance: introspection,
subclassing built-in types, `isinstance`/`issubclass`, and class hierarchies
with `BaseGeometry`, `Rectangle` and `Square`.

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | Returns the attributes and methods of an object. |
| `1-my_list.py` | `MyList`, a list subclass with `print_sorted`. |
| `2-is_same_class.py` | Checks if an object is exactly an instance of a class. |
| `3-is_kind_of_class.py` | Checks if an object is an instance of a class or a subclass. |
| `4-inherits_from.py` | Checks if an object is an instance of a subclass only. |
| `5-base_geometry.py` | An empty class `BaseGeometry`. |
| `6-base_geometry.py` | Adds an `area` method that is not implemented. |
| `7-base_geometry.py` | Adds `integer_validator`. |
| `8-rectangle.py` | `Rectangle` with private, validated width and height. |
| `9-rectangle.py` | Adds `area` and a string description. |
| `10-square.py` | `Square` inheriting from `Rectangle`. |
| `11-square.py` | `Square` with its own string description. |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py`. |
| `tests/7-base_geometry.txt` | Doctests for `7-base_geometry.py`. |

Run the tests from this directory with
`python3 -m doctest -v ./tests/1-my_list.txt`.

Advanced tasks:

| File | Description |
| ---- | ----------- |
| `100-my_int.py` | `MyInt`, an `int` subclass with `==` and `!=` inverted. |
| `101-add_attribute.py` | Adds a new attribute to an object if it is possible. |
