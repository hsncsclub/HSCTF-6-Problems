import sys
import yaml

print("Welcome to JSON info!")

print("Please enter your JSON:")

try:
    d = yaml.load(sys.stdin)
except Exception as e:
    print("There was an error: %s" % str(e))
else:
    if isinstance(d, list):
        print("You have entered: an array")
        print("The array has %d elements" % len(d))
        print("Thank you for using JSON info!")
    elif isinstance(d, dict):
        print("You have entered: an object")
        print("The object has %d members" % len(d))
        print("Thank you for using JSON info!")
    else:
        print("Type %s is unsupported" % d.__class__.__name__)
        print("Please use a valid JSON array or object")
        print("Thank you for using JSON info!")
