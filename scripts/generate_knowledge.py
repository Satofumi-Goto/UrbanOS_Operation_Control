from pathlib import Path

base = Path("GENERATED_KNOWLEDGE")

nodes = [
    ("01_Collapse", "Overall", "Queue_Saturation"),
    ("01_Collapse", "Urban_Operation_Console", "Dispatch_Collapse"),
    ("01_Collapse", "Service_Hub_Console", "Node_Gridlock"),
    ("01_Collapse", "Fleet_Operation_Console", "Fleet_Deadlock"),
    ("01_Collapse", "Seneschal", "ETA_Collapse"),
]

for category, console, topic in nodes:

    folder = base / category / console
    folder.mkdir(parents=True, exist_ok=True)

    content = f"# {topic}\n"

    path = folder / f"{topic}.md"
    path.write_text(content, encoding="utf-8")

print("Knowledge pack generated.")
