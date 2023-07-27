def addLocalization(modID: str, part: str, material: str):
    if part == "block":
        return f"tile.{modID}.{part}_{material}.name={material.capitalize()} {part.capitalize()}\n"
    return f"item.{modID}.{part}_{material}.name={material.capitalize()} {part.capitalize()}\n"
def addLocalizationCategory(part: str):
    return f"#   {part}\n"