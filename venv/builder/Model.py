import json


def writeModel(modID: str, part: str, material: str):
    if part == "block":
        jsonModelFile = open(f"output\\blockstates\\block\material\\{part}_{material}.json", "w")
        model = {
            "forge_marker": 1,
            "defaults": {
                "textures": {
                    "all": f"{modID}:block/material/{part}_{material}"
                }
            },
            "variants": {
                "normal": {
                    "model": "cube_all"
                },
                "inventory": {
                    "model": "cube_all"
                }
            }
        }
    else:
        jsonModelFile = open(f"output\models\item\\{part}\\{part}_{material}.json", "w")
        model = {
            "parent": "item/generated",
            "textures": {
                "layer0": f"{modID}:item/{part}/{part}_{material}"
            }
        }
    jsonModelFile.write(json.dumps(model, indent=4))
    jsonModelFile.close()