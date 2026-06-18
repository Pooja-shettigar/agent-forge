from pathlib import Path

def load_skill(skill_name):

    path = Path("skills") / skill_name

    with open(path, "r") as f:
        return f.read()