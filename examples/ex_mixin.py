# Adds properties of obj as functions on unicore itself.

custom_methods = {
    "triple": lambda x: x * 3,
    "quadruple": lambda x: x * 4
}

unicore.mixin(custom_methods)
print(unicore.triple(3))    # Output: 9
print(unicore.quadruple(2)) # Output: 8