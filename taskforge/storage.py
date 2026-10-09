import json
from pathlib import Path

DEFAULT_PATH = Path("tasks.json")

def save_tasks(tasks, path=DEFAULT_PATH):
    # Bug B1: currently does not persist anything
    return len(tasks)

def load_tasks(path=DEFAULT_PATH):
    # Bug B1: currently ignores persisted state
    return []
