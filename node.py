from pathlib import Path
import folder_paths
from comfy_api.latest import io, ComfyExtension, ui


class EmbeddingPicker(io.ComfyNode):
    @classmethod
    def define_schema(cls) -> io.Schema:
        embeddings = folder_paths.get_filename_list("embeddings")

        return io.Schema(
            node_id="EmbeddingPicker",
            display_name="Embedding Picker",
            category="utils",
            inputs=[
                io.Combo.Input("embedding", options=embeddings),

                io.Float.Input(
                    "emphasis",
                    default=1.0,
                    min=0.0,
                    max=3.0,
                    step=0.05
                ),

                io.Boolean.Input("append", default=False),

                io.String.Input("text", multiline=True)
            ],
            outputs=[
                io.String.Output("text")
            ]
        )

    @classmethod
    def execute(cls, text, embedding, emphasis, append) -> io.NodeOutput:
        if emphasis < 0.05:
            return io.NodeOutput(text)

        emb = "embedding:" + Path(embedding).stem

        emphasis_str = f"{emphasis:.3f}"
        if emphasis_str != "1.000":
            emb = f"({emb}:{emphasis_str})"

        output = f"{text}, {emb}" if append else f"{emb}, {text}"

        return io.NodeOutput(output)


class EmbeddingPickerExtension(ComfyExtension):
    async def get_node_list(self) -> list[type[io.ComfyNode]]:
        return [EmbeddingPicker]


async def comfy_entrypoint() -> ComfyExtension:
    return EmbeddingPickerExtension()
