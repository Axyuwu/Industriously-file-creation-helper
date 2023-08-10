def part(name: str, condition: str) -> dict[str, str]:
    return {
        "name": name,
        "condition": condition
    }

def getAllParts() -> list[dict[str,str]]:
    return [
        part("ingot", "shouldCreateIngot"),
        part("gear", "hasGear"),
        part("block", "shouldCreateBlock")
    ]