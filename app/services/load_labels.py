import pickle

def load_label_encoder():
    class CustomUnpickler(pickle.Unpickler):
        def find_class(self, module, name):
            if module == "sklearn.preprocessing.label":
                module = "sklearn.preprocessing"
            return super().find_class(module, name)
    
    filename = 'labels/labels'
    with open(filename, 'rb') as infile:
        lb = CustomUnpickler(infile).load()
    return lb