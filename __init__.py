from .node import EmbeddingPicker

NODE_CLASS_MAPPINGS = {"EmbeddingPicker": EmbeddingPicker}
NODE_DISPLAY_NAME_MAPPINGS = {"EmbeddingPicker": "Embedding Picker"}

# --------------------------- Install web extension ----------------------------
import shutil
from pathlib import Path

# Get base paths
node_dir = Path(__file__).resolve().parent
comfy_dir = node_dir.parent.parent

script_path = node_dir / "js" / "quickNodes.js"
destination_dir = comfy_dir / "web" / "extensions" / "tropfchen"
destination_path = destination_dir / "epQuickNodes.js"

ER = "during installing Embedding Picker web extension"
try:
    destination_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(script_path, destination_path)
except PermissionError as permission_error:
    print(f"Permission error {ER}: {permission_error}")
except Exception as e:
    print(f"An unexpected error occurred {ER}: {e}")
