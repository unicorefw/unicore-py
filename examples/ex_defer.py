# Defers a function until the current call stack has cleared.

def say_hello():
    print("Hello, deferred!")

unicore.defer(say_hello)  # Output: "Hello, deferred!" after stack clears