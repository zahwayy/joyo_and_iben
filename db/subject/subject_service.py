import os
import const
import utils

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUBJECTS_FILE = os.path.join(BASE_DIR, "subjects.txt")

def ensure_header():
    if not os.path.exists(SUBJECTS_FILE):
        full_path = SUBJECTS_FILE
        utils.create_header(
            full_path,
            const.V_SEPARATOR,
            const.SUBJECT_ID_COL_NAME,
            " " * (const.ID_MAX_CHAR - len(const.SUBJECT_ID_COL_NAME)),
            const.V_SEPARATOR,
            const.NAME_COL_NAME,
            " " * (const.VALUE_MAX_CHAR - len(const.NAME_COL_NAME)),
            const.V_SEPARATOR,
        )

def insert(subject):
    ensure_header()
    try:
        subject_id = str(subject.get_subject_id())
        name       = str(subject.get_name())

        if len(subject_id) > const.ID_MAX_CHAR:
            raise ValueError("Subject ID is too long")
        if len(name) > const.VALUE_MAX_CHAR:
            raise ValueError("Subject Name is too long")

        row = (
            f"{const.V_SEPARATOR}"
            f"{subject_id}"
            f"{' ' * (const.ID_MAX_CHAR - len(subject_id))}"
            f"{const.V_SEPARATOR}"
            f"{name}"
            f"{' ' * (const.VALUE_MAX_CHAR - len(name))}"
            f"{const.V_SEPARATOR}\n"
        )

        hlen = (len(const.V_SEPARATOR) * 3) + const.ID_MAX_CHAR + const.VALUE_MAX_CHAR
        hline = f"{const.H_SEPARATOR * hlen}\n"

        with open(SUBJECTS_FILE, "a") as f:
            f.write(row)
            f.write(hline)

        return True

    except Exception as error:
        raise

def read():
    ensure_header()
    try:
        records = []
        if not os.path.exists(SUBJECTS_FILE):
            return records
        with open(SUBJECTS_FILE, "r") as f:
            for line in f:
                s = line.rstrip("\n")
                if not s:
                    continue
                if set(s) == {const.H_SEPARATOR}:
                    continue
                if not s.startswith(const.V_SEPARATOR) or not s.endswith(const.V_SEPARATOR):
                    continue
                parts = s.split(const.V_SEPARATOR)
                if len(parts) < 4:
                    continue
                sid = parts[1].rstrip()
                name = parts[2].rstrip()
                if sid.strip() == const.SUBJECT_ID_COL_NAME.strip() and name.strip() == const.NAME_COL_NAME.strip():
                    continue
                records.append({"subject_id": sid, "name": name})
        return records
    except Exception as error:
        raise

def delete(subject_id: str):
    ensure_header()
    try:
        target = str(subject_id)
        rows = read()
        kept = [r for r in rows if r["subject_id"] != target]
        if len(kept) == len(rows):
            return False
        tmp_file = SUBJECTS_FILE + ".tmp"
        utils.create_header(
            tmp_file,
            const.V_SEPARATOR,
            const.SUBJECT_ID_COL_NAME,
            " " * (const.ID_MAX_CHAR - len(const.SUBJECT_ID_COL_NAME)),
            const.V_SEPARATOR,
            const.NAME_COL_NAME,
            " " * (const.VALUE_MAX_CHAR - len(const.NAME_COL_NAME)),
            const.V_SEPARATOR,
        )
        with open(tmp_file, "a") as f:
            for r in kept:
                row = (
                    f"{const.V_SEPARATOR}"
                    f"{r['subject_id']}"
                    f"{' ' * (const.ID_MAX_CHAR - len(r['subject_id']))}"
                    f"{const.V_SEPARATOR}"
                    f"{r['name']}"
                    f"{' ' * (const.VALUE_MAX_CHAR - len(r['name']))}"
                    f"{const.V_SEPARATOR}\n"
                )
                hlen = (len(const.V_SEPARATOR) * 3) + const.ID_MAX_CHAR + const.VALUE_MAX_CHAR
                hline = f"{const.H_SEPARATOR * hlen}\n"
                f.write(row)
                f.write(hline)
        os.replace(tmp_file, SUBJECTS_FILE)
        return True
    except Exception as error:
        raise
