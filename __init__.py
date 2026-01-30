from pathlib import Path
from .node import comfy_entrypoint

WEB_DIRECTORY = "./js"
__all__ = ["WEB_DIRECTORY", "comfy_entrypoint"]

# ------------------------ Remove copied web extension -------------------------
node_dir = Path(__file__).resolve().parent
comfy_dir = node_dir.parent.parent
destination_dir = comfy_dir / "web" / "extensions" / "tropfchen"
destination_path = destination_dir / "epQuickNodes.js"

if destination_path.exists():
    destination_path.unlink()
# --------------------------- Install web extension ----------------------------
