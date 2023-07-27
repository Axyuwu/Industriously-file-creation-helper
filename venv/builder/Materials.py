def getBaseMaterial(type: str, name: str):
    if type == "metal":
        return material(name=name, shouldCreateIngot=True, hasGear=True, shouldCreateBlock=True)

def material(name: str, shouldCreateIngot: bool, hasGear: bool, shouldCreateBlock: bool):
    return {
        "name": name,
        "shouldCreateIngot": shouldCreateIngot,
        "hasGear": hasGear,
        "shouldCreateBlock": shouldCreateBlock
    }

def getAllMaterials():

    aluminium = getBaseMaterial("metal", "aluminium")
    copper = getBaseMaterial("metal", "copper")
    silver = getBaseMaterial("metal", "silver")
    titanium = getBaseMaterial("metal", "titanium")
    tungsten = getBaseMaterial("metal", "tungsten")
    gold = getBaseMaterial("metal", "gold")
    gold["shouldCreateIngot"] = False
    gold["shouldCreateBlock"] = False
    iron = getBaseMaterial("metal", "iron")
    iron["shouldCreateIngot"] = False
    iron["shouldCreateBlock"] = False

    return [
        aluminium,
        copper,
        silver,
        titanium,
        tungsten,
        gold,
        iron
    ]

