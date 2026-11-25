"""Write the toaster-error entry text to entry.txt in the output directory.

Output directory: $MAKEFUN_OUTPUT_DIR if set and non-empty, else /output.
Standard library only; deterministic, no network, clock, or randomness.
"""

import os

ENTRY = (
    "Error: toast complete. Completed one minute ago. "
    "I chose not to mention it.\n"
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as error:
    raise SystemExit(f"cannot create output directory {output_dir!r}: {error}")

try:
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
except OSError as error:
    raise SystemExit(f"cannot write entry.txt in {output_dir!r}: {error}")
