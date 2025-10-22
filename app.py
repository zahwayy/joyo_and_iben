import sys
from utils import write_greeting, get_role, menu, prompt_subject_create, prompt_subject_delete, prompt_assistant_create, prompt_assistant_delete, warn
from controllers.assistant_controller import read_assistants, create_assistant, delete_assistant
from controllers.subject_controller import read_subjects, create_subject, delete_subject

def main():
    write_greeting()
    while True:
        role = get_role()
        while True:
            choice = menu(role)
            if choice == "1":
                read_assistants()
            elif choice == "2":
                read_subjects()
            elif choice == "3":
                sid, name = prompt_subject_create()
                create_subject(sid, name, role)
            elif choice == "4":
                sid = prompt_subject_delete()
                delete_subject(sid, role)
            elif choice == "5":
                aid, name = prompt_assistant_create()
                create_assistant(aid, name, role)
            elif choice == "6":
                aid = prompt_assistant_delete()
                delete_assistant(aid, role)
            elif choice == "7":
                break
            elif choice == "8":
                sys.exit(0)
            else:
                warn("Invalid input, please try again")

if __name__ == "__main__":
    main()