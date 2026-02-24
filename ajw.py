import os
import json
import tempfile
from typing import Union
from pathlib import Path

DATA_BASE_PATH = Path("/home/jvk/depromo/data_set.json")

if not DATA_BASE_PATH.exists():
    DATA_BASE_PATH.write_text("{}")

def dump(data:dict, file:Union[str,Path]):
    file = Path(file)
    with tempfile.NamedTemporaryFile("w", delete = False,dir = file.parent) as tmp:
        json.dump(data, tmp, indent = 4)
        tmp.flush()
        os.fsync(tmp.fileno())
        tmp_name = tmp.name
    
    os.replace(tmp_name, file)

def append(key:int, value:str):
    file = open(str(DATA_BASE_PATH),"r")
    data = json.load(file)
    file.close()
    new_data = {
        **data,
        str(key):value
        }
    dump(new_data,DATA_BASE_PATH)

