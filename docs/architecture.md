# TaskForge architecture

- `main.py`: CLI parsing and command routing
- `taskforge/manager.py`: task creation, completion, deletion, listing
- `taskforge/validator.py`: input validation
- `taskforge/search.py`: searching tasks
- `taskforge/storage.py`: JSON persistence (unfinished)
- `tests/`: initial test suite; intentionally incomplete

Task schema: `{ "id": int, "title": str, "completed": bool, "priority": str }`.
