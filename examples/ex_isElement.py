# Checks if an object is an XML element (similar to DOM element).
 
from xml.etree.ElementTree import Element
result = unicore.isElement(Element("tag"))
print(result)  # Output: True

result = unicore.isElement("not an element")
print(result)  # Output: False
