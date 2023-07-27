import os

import Materials
import Parts
import Texture
import Localization
import Model

def createDir(path: str):
    if not os.path.exists(path):
        os.mkdir(path)

def runBuilder(modID: str):
    createDir(f"./output/models")
    createDir(f"./output/models/item")

    createDir(f"./output/textures")
    createDir(f"./output/textures/item")
    createDir(f"./output/textures/block")
    createDir(f"./output/textures/block/material")

    createDir(f"./output/blockstates")
    createDir(f"./output/blockstates/material")

    materials = Materials.getAllMaterials()
    parts = Parts.getAllParts()

    localizationString = "#Auto Generated\n"

    for part in parts:
        partName = part["name"]
        if not os.path.isfile(f"textures\\bases\\{partName}.png"):
            print(f"Missing {partName} base texture!")
            continue
        localizationString += Localization.addLocalizationCategory(partName)
        if not partName == "block":
            createDir(f"./output/models/item/{partName}")
            createDir(f"./output/textures/item/{partName}")
        for material in materials:
            materialName = material["name"]
            if not material[part["condition"]]:
                continue
            if not os.path.isfile(f"textures\\materials\\{materialName}.png"):
                print(f"Missing {materialName} material texture!")
                continue
            localizationString += Localization.addLocalization(modID = modID, part = partName, material = materialName)
            Model.writeModel(modID = modID, part = partName, material = materialName)
            Texture.createPart(part = partName, material = materialName)

    localizationFile = open("output\localizationFile.lang", "w")
    localizationFile.write(localizationString)
    localizationFile.close()

runBuilder("industriously")