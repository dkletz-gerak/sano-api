from dotenv import load_dotenv
from .setting import *
import sys


load_dotenv()


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
    elif argv[2] == "migrate" and len(argv) == 3:
        module = __import__("core.migration")
        func = getattr(module, argv[2])
        func()
    else:
        print_help()
