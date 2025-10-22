import const


WIDTH = 60
INNER = WIDTH - 6

def line():
    print(const.H_SEPARATOR * WIDTH)

def space(n=1):
    for _ in range(max(1, n)):
        print()

def center(text):
    t = str(text)[:INNER]
    pad = max(0, INNER - len(t))
    left = pad // 2
    right = pad - left
    print(const.V_SEPARATOR + (" " * left) + t + (" " * right) + const.V_SEPARATOR)

def info(msg):
    print(f"ℹ️  {msg}")
    space()

def success(msg):
    print(f"✅ {msg}")
    space()

def warn(msg):
    print(f"⚠️  {msg}")
    space()

def error(msg):
    print(f"❌ {msg}")
    space()

def write_greeting():
    line()
    center("WELCOME !!!")
    line()
    space()
    center("This application is used to record")
    center("the list of assistants and subjects")
    center("for the Algorithm and Programming course.")
    space()
    line()
    space()

def get_role():
    line()
    print("🔐 Choose role")
    print("1. Assistant")
    print("2. Coordinator")
    line()
    while True:
        o = input("Enter your choice here (1/2): ").strip()
        if o in ("1", "2"):
            space()
            if o == "1":
                info("You're logged in as an assistant.")
            else:
                info("You're logged in as a coordinator.")
            return int(o)
        warn("Invalid input. Please try again.")

def menu(role):
    line()
    print(f"🔐 Role: {'Assistant' if role == 1 else 'Coordinator'}")
    print("1. 👥 View assistants")
    print("2. 📚 View subjects")
    print("3. ➕📚 Add subject")
    print("4. 🗑️📚 Delete subject")
    print("5. ➕👤 Add assistant")
    print("6. 🗑️👤 Delete assistant")
    print("7. 🔄 Switch role")
    print("8. 🚪 Exit")
    choice = input("Choose (1-8): ").strip()
    space()
    return choice

def prompt_subject_create():
    print("➕📚 Create Subject")
    sid = input("Subject ID: ").strip()
    name = input("Subject Name: ").strip()
    space()
    return sid, name

def prompt_subject_delete():
    print("🗑️📚 Delete Subject")
    sid = input("Subject ID to delete: ").strip()
    space()
    return sid

def prompt_assistant_create():
    print("➕👤 Create Assistant")
    aid = input("Assistant ID: ").strip()
    name = input("Assistant Name: ").strip()
    space()
    return aid, name

def prompt_assistant_delete():
    print("🗑️👤 Delete Assistant")
    aid = input("Assistant ID to delete: ").strip()
    space()
    return aid

def print_table(rows, columns):
    if not rows:
        info("No data to display.")
        return
    widths = []
    headers = [h for _, h in columns]
    for i, (key, header) in enumerate(columns):
        w = len(header)
        for r in rows:
            v = str(r.get(key, ""))
            if len(v) > w:
                w = len(v)
        widths.append(w)
    sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
    print(sep)
    cells = []
    for (w, h) in zip(widths, headers):
        cells.append(" " + h.ljust(w) + " ")
    print("|" + "|".join(cells) + "|")
    print(sep)
    for r in rows:
        cells = []
        for (w, (key, _)) in zip(widths, columns):
            cells.append(" " + str(r.get(key, "")).ljust(w) + " ")
        print("|" + "|".join(cells) + "|")
    print(sep)
    space()

def create_header(path, *segments):
    hlen = (len(const.V_SEPARATOR) * 3) + const.ID_MAX_CHAR + const.VALUE_MAX_CHAR
    line = const.H_SEPARATOR * hlen
    header = "".join(str(s) for s in segments)
    with open(path, "w", newline="") as f:
        f.write(line + "\n")
        f.write(header + "\n")
        f.write(line + "\n")
