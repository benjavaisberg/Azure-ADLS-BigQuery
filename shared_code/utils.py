import importlib

def import_object(module_name, object_name):
    try:
        module = importlib.import_module(module_name)
        obj = getattr(module, object_name)
        return obj
    except (ImportError, AttributeError) as e:
        print(f"Error importing {object_name} from {module_name}: {e}")
        return None