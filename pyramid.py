# Ask the user to enter the number of blocks
blocks = int(input("Enter the number of blocks: "))

# Initialize height and blocks needed for the current layer
height = 0
layer_blocks = 1

# Build the pyramid layer by layer
while blocks >= layer_blocks:
    blocks -= layer_blocks  # Use the blocks for the current layer
    height += 1             # Increase the pyramid height
    layer_blocks += 1       # Next layer needs one more block

# Print the final height of the pyramid
print("The height of the pyramid:", height)
# User Input: The program asks for the number of blocks.
# Initialization:
# height starts at 0 (no layers built yet).
# layer_blocks starts at 1 (first layer needs 1 block).
# Loop Until Blocks Run Out:
# If we have enough blocks for the current layer, we use them.
# Increase height since the layer is completed.
# The next layer requires one more block than the previous.
# Exit When Blocks Are Insufficient:
# The loop stops when we don’t have enough blocks for the next layer.
# Print the Pyramid Height:
# The final height is the maximum fully completed layers.