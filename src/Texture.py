import png
import itertools
import math

def createPart(part: str, material: str):

    greyScaleArray = list(png.Reader(filename = f"textures\\bases\\{part}.png").asRGBA8()[2])
    textureArray = list(png.Reader(filename = f"textures\\materials\\{material}.png").asRGBA8()[2])

    outputTexture = []

    squareRoot3 = math.sqrt(3)

    max255 = lambda x: min(x,255)

    for pixelLines in itertools.zip_longest(textureArray, greyScaleArray):
        outputTexture.append([])
        textureLine = pixelLines[0]
        greyScaleLine = pixelLines[1]
        for pixelIndex in range(len(textureLine)//4):
            texturePixelR = textureLine[pixelIndex * 4]/255
            texturePixelG = textureLine[pixelIndex * 4 + 1]/255
            texturePixelB = textureLine[pixelIndex * 4 + 2]/255
            greyScalePixelLuminance = math.sqrt(((greyScaleLine[pixelIndex * 4]/255)**2) * 3)/squareRoot3
            outputTexture[-1].extend(
                [
                    max255(),
                    max255(round(texturePixelG * 255 * greyScalePixelLuminance)),
                    max255(round(texturePixelB * 255 * greyScalePixelLuminance)),
                    round(textureLine[pixelIndex * 4 + 3] * greyScaleLine[pixelIndex * 4 + 3]/255)
                ]
            )
    if part == "block":
        png.from_array(outputTexture, "RGBA", {}).save(f"output\\textures\\block\material\\{part}_{material}.png")
    else:
        png.from_array(outputTexture, "RGBA", {}).save(f"output\\textures\item\\{part}\\{part}_{material}.png")