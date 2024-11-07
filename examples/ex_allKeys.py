# Retrieves all keys in an object, including inherited ones.

class Parent:
    parent_key = "parent"

class Child(Parent):
    child_key = "child"

result = unicore.allKeys(Child())
print(result)  # Output: ['parent_key', 'child_key']