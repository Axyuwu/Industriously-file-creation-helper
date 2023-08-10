preConfigMaterial = {
    "metal": {
        "shouldCreateIngot": True,
        "hasGear": True,
        "shouldCreateBlock": True
    }
}

def material(type_:str, name: str, shouldCreateIngot: bool | None=None, hasGear: bool | None=None, shouldCreateBlock: bool | None=None) -> dict[str,str]:
    return {
        "name": name,
        "shouldCreateIngot": preConfigMaterial[type_]["shouldCreateIngot"] if shouldCreateIngot == None else shouldCreateIngot,
        "hasGear": preConfigMaterial[type_]["hasGear"] if hasGear == None else hasGear,
        "shouldCreateBlock": preConfigMaterial[type_]["shouldCreateBlock"] if shouldCreateBlock == None else shouldCreateBlock
    }

def getAllMaterials():

    aluminium = material("metal", "aluminium")
    copper = material("metal", "copper")
    silver = material("metal", "silver")
    titanium = material("metal", "titanium")
    tungsten = material("metal", "tungsten")
    gold = material("metal", "gold")
    gold["shouldCreateIngot"] = False
    gold["shouldCreateBlock"] = False
    iron = material("metal", "iron")
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

