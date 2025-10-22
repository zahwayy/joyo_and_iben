from db.subject import subject_service
from models.subject_model import SubjectModel
from utils import warn, success, error, print_table

def _is_coordinator(role):
    if role is None:
        return False
    if isinstance(role, int):
        return role == 2
    if isinstance(role, str):
        return role.strip().lower().startswith("coord")
    return False

def create_subject(subject_id, name, role):
    try:
        # TODO: Something is missing here
        subject_service.insert(subject)
        success(f"Subject {name} created with ID: {subject_id}")
    except Exception as e:
        error(str(e))

def read_subjects():
    try:
        rows = subject_service.read()
        print_table(rows, [("subject_id", "ID"), ("name", "Name")])
    except Exception as e:
        error(str(e))

def delete_subject(subject_id, role):
    if not _is_coordinator(role):
        warn("Permission denied: only Coordinator can delete subjects.")
        return
    try:
        ok = subject_service.delete(subject_id)
        if ok:
            success(f"Subject with ID {subject_id} deleted.")
        else:
            error(f"Subject with ID {subject_id} not found.")
    except Exception as e:
        error(str(e))
