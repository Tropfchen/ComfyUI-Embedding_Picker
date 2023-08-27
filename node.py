from pathlib import Path

import folder_paths


class EmbeddingPicker:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        embeddings = folder_paths.get_filename_list("embeddings")

        return {
            "required": {
                "prompts": ("STRING", {"forceInput": True}),
                "embedding": ((embeddings),),
                "emphasis": (
                    "FLOAT",
                    {
                        "default": 1.0,
                        "min": 0.05,
                        "max": 3.0,
                        "step": 0.05,
                    },
                ),
                "append": (
                    "BOOLEAN",
                    {"default": False, "label_on": "true ", "label_off": "false "},
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompts",)
    FUNCTION = "concat_embedding"
    OUTPUT_NODE = False

    CATEGORY = "utils"

    def concat_embedding(self, prompts, embedding, emphasis, append):
        emb = "embedding:" + Path(embedding).stem

        emphasis = f"{emphasis:.3f}"
        if emphasis != "1.000":
            emb = f"({emb}:{emphasis})"

        output = f"{prompts}, {emb}" if append else f"{emb}, {prompts}"

        return (output,)


NODE_CLASS_MAPPINGS = {"EmbeddingPicker": EmbeddingPicker}
NODE_DISPLAY_NAME_MAPPINGS = {"EmbeddingPicker": "Embedding Picker"}
