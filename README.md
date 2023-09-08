# Embedding Picker

Tired of forgetting and misspelling often weird names of embeddings you use?
Or perhaps you use only one, cause you forgot you have tens of them installed?

Try this.

# Installation

Exactly the same as with other simple custom nodes.

- Click the green **Code** button, select **Download Zip**, and unpack it in your ComfyUI `custom_nodes` directory

or

- Clone this repository by running `git clone https://github.com/Tropfchen/ComfyUI-Embedding_Picker.git` in your ComfyUI `custom_nodes` directory

To uninstall:

- Delete the `ComfyUi_Embedding_Picker` in your ComfyUI custom_nodes directory and `epQuickNodes.js` file in `ComfyUI\web\extensions\tropf` directory

# Use

Simply connect `Embedding Picker` node, that you will find in `utils` menu, in between _CLIP Encoding_ and _Text Multiine_ or other similar nodes.

You can also right click on _CLIP Encoding_ node, and choose `Prepend Embedding Picker` to place and link one automatically.
Similar option exists on `Embedding Picker` node itself, feel free to use both multiple times to chain more nodes.

By default the embedding will be set as the first prompt, set `append` to True if you prefer it to be the last one.

## Example Workflow:

![Example](example_workflow.png)
