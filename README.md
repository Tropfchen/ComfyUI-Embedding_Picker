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

- Delete the `ComfyUi_Embedding_Picker` in your ComfyUI custom_nodes directory

# Use

Simply connect `Embedding Picker` node, that you will find in `utils` menu, in between _CLIP Encoding_ and _Text Multiine_ or other similar nodes.
By default the embedding will be set as first prompt, set `append` to True if you prefer it to be the last one.

## Example Workflow:

![Example](example_workflow.png)
