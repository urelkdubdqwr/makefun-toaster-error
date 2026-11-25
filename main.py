import os

ENTRY = (
    "Error: toast complete. Completed one minute ago. "
    "I chose not to mention it.\n"
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY)
