import os
import const
import utils

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSISTANTS_FILE = os.path.join(BASE_DIR, "assistants.txt")

def ensure_header():
    if not os.path.exists(ASSISTANTS_FILE):
        full_path = ASSISTANTS_FILE
        utils.create_header(
            full_path,
            const.V_SEPARATOR,
            const.ASSISTANT_ID_COL_NAME,
            " " * (const.ID_MAX_CHAR - len(const.ASSISTANT_ID_COL_NAME)),
            const.V_SEPARATOR,
            const.NAME_COL_NAME,
            " " * (const.VALUE_MAX_CHAR - len(const.NAME_COL_NAME)),
            const.V_SEPARATOR,
        )

def insert(assistant):
    ensure_header()
    try:
        assistant_id = str(assistant.get_assistant_id())
        name = str(assistant.get_name())

        if len(assistant_id) > const.ID_MAX_CHAR:
            raise ValueError("Assistant ID is too long")
        if len(name) > const.VALUE_MAX_CHAR:
            raise ValueError("Assistant Name is too long")

        row = (
            f"{const.V_SEPARATOR}"
            f"{assistant_id}"
            f"{' ' * (const.ID_MAX_CHAR - len(assistant_id))}"
            f"{const.V_SEPARATOR}"
            f"{name}"
            f"{' ' * (const.VALUE_MAX_CHAR - len(name))}"
            f"{const.V_SEPARATOR}\n"
        )

        hlen = (len(const.V_SEPARATOR) * 3) + const.ID_MAX_CHAR + const.VALUE_MAX_CHAR
        hline = f"{const.H_SEPARATOR * hlen}\n"

        with open(ASSISTANTS_FILE, "a") as f:
            f.write(row)
            f.write(hline)

        return True

    except Exception as error:
        raise

def read():
    ensure_header()
    try:
        records = []
        if not os.path.exists(ASSISTANTS_FILE):
            return records
        with open(ASSISTANTS_FILE, "r") as f:
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
                aid = parts[1].rstrip()
                name = parts[2].rstrip()
                if aid.strip() == const.ASSISTANT_ID_COL_NAME.strip() and name.strip() == const.NAME_COL_NAME.strip():
                    continue
                records.append({"assistant_id": aid, "name": name})
        return records
    except Exception as error:
        raise

def delete(assistant_id: str):
    ensure_header()
    try:
        target = str(assistant_id)
        rows = read()
        kept = [r for r in rows if r["assistant_id"] != target]
        if len(kept) == len(rows):
            return False
        tmp_file = ASSISTANTS_FILE + ".tmp"
        utils.create_header(
            tmp_file,
            const.V_SEPARATOR,
            const.ASSISTANT_ID_COL_NAME,
            " " * (const.ID_MAX_CHAR - len(const.ASSISTANT_ID_COL_NAME)),
            const.V_SEPARATOR,
            const.NAME_COL_NAME,
            " " * (const.VALUE_MAX_CHAR - len(const.NAME_COL_NAME)),
            const.V_SEPARATOR,
        )
        with open(tmp_file, "a") as f:
            for r in kept:
                row = (
                    f"{const.V_SEPARATOR}"
                    f"{r['assistant_id']}"
                    f"{' ' * (const.ID_MAX_CHAR - len(r['assistant_id']))}"
                    f"{const.V_SEPARATOR}"
                    f"{r['name']}"
                    f"{' ' * (const.VALUE_MAX_CHAR - len(r['name']))}"
                    f"{const.V_SEPARATOR}\n"
                )
                hlen = (len(const.V_SEPARATOR) * 3) + const.ID_MAX_CHAR + const.VALUE_MAX_CHAR
                hline = f"{const.H_SEPARATOR * hlen}\n"
                f.write(row)
                f.write(hline)
        os.replace(tmp_file, ASSISTANTS_FILE)
        return True
    except Exception as error:
        raise
