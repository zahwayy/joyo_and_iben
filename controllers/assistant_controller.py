from db.assistant import assistant_service
from models.assistant import AssistantModel
from utils import warn, success, error, print_table

def _is_coordinator(role):
    if role is None:
        return False
    if isinstance(role, int):
        return role == 2
    if isinstance(role, str):
        return role.strip().lower().startswith("coord")
    return False

def create_assistant(assistant_id, name, role):
    if not _is_coordinator(role):
        warn("Permission denied: only Coordinator can create assistants.")
        return
    try:
        # TODO: Something is missing here
        assistant_service.insert(assistant)
        success(f"Assistant {name} created with ID: {assistant_id}")
    except Exception as e:
        error(str(e))

def read_assistants():
    try:
        rows = assistant_service.read()
        print_table(rows, [("assistant_id", "ID"), ("name", "Name")])
    except Exception as e:
        error(str(e))

def delete_assistant(assistant_id, role):
    if not _is_coordinator(role):
        warn("Permission denied: only Coordinator can delete assistants.")
        return
    try:
        ok = assistant_service.delete(assistant_id)
        if ok:
            success(f"Assistant with ID {assistant_id} deleted.")
        else:
            error(f"Assistant with ID {assistant_id} not found.")
    except Exception as e:
        error(str(e))
