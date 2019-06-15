import core.load_env
import importlib.util
from setting import *
import sys


def print_help():
    print("Available argument:")
    print("1. start [file] [app]")
    print("2. migrate")
    print("3. help")


argv = sys.argv
if len(argv) == 1:
    print_help()
else:
    if argv[1] == "start" and len(argv) == 4:
        module = __import__(argv[2])
        app = getattr(module, argv[3])
        app.run(
            host=HOST,
            port=PORT,
            threaded=THREADED,
            debug=DEBUG,
        )
    elif argv[1] == "migrate" and len(argv) == 3:
        spec = importlib.util.spec_from_file_location('migrator', 'core/migration.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        getattr(module, argv[2])()
    else:
        print_help()
