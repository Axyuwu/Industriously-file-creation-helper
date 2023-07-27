def part(name: str, condition: str):
    return {
        "name": name,
        "condition": condition
    }

def getAllParts():
    return [
        part("ingot", "shouldCreateIngot"),
        part("gear", "hasGear"),
        part("block", "shouldCreateBlock")
    ]