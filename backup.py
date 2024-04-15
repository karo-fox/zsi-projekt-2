import datetime
import re

SEP = r"[\-\:\.]"

if __name__ == "__main__":
    timestamp = re.sub(SEP, "-", str(datetime.datetime.now().isoformat()))
    with open("./report/index.html") as file:
        content = file.read()
    content = content.replace(
        '<p class="title">Raport - Pasjans</p>',
        f'<p class="title">Raport - Pasjans - backup: {timestamp}</p>',
    )
    with open(f"./backup/backup-{timestamp}.html", "x") as file:
        file.write(content)
