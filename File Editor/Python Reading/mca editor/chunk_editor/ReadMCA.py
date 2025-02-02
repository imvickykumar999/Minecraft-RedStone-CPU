
# pip install anvil-parser
import anvil

region = anvil.Region.from_file('r.0.0.mca')
print(region)
# <anvil.region.Region object at 0x0000015FADF447F0>

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global
block = chunk.get_block(0, 0, 0)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
