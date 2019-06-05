import pickle, sys

class Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__":
            return super().find_class(module, name)
        raise pickle.UnpicklingError("global '%s.%s' is forbidden" % (module, name))

print("I'm hungry for some pickles")

try:
    p = Unpickler(sys.stdin.buffer).load()
except Exception as e:
    print("Noooo I want pickles", e)
else:
    print("Yum Yum pickle pickle", p)
