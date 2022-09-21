import importlib.util
import inspect
import json
import sys

from beam import App


def build(path: str) -> str:
    beamapp = None
    spec = importlib.util.spec_from_file_location("app_module", path)
    app_module = importlib.util.module_from_spec(spec)
    sys.modules["app_module"] = app_module
    spec.loader.exec_module(app_module)

    for member in inspect.getmembers(app_module):
        member_value = member[1]
        if isinstance(member_value, App):
            beamapp = member_value
            break

    if beamapp is not None:
        return json.dumps(beamapp.dumps())
    
    raise Exception("Beam app not found")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)

    path = sys.argv[1]
    save_stdout = sys.stdout
    sys.stdout = None
    app_config = build(path)
    sys.stdout = save_stdout
    print(app_config)
