
import os
import requests
from html import escape

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["REPOSITORY"]

START = "<!-- STARGAZERS:START -->"
END = "<!-- STARGAZERS:END -->"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def fetch_stargazers():
    users = []
    page = 1

    while True:
        url = (
            f"https://api.github.com/repos/{REPO}/stargazers"
            f"?per_page=100&page={page}"
        )

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )
        response.raise_for_status()

        data = response.json()

        if not data:
            break

        users.extend(data)
        page += 1

    return users


def generate_gallery(users):
    rows = []

    for i in range(0, len(users), 5):
        cells = []

        for user in users[i:i + 5]:
            username = escape(user["login"])
            profile = escape(user["html_url"], quote=True)
            avatar = escape(user["avatar_url"], quote=True)

            cells.append(f"""
            <td align="center" width="20%" valign="top">
              <a href="{profile}">
                <img
                  src="{avatar}&s=120"
                  width="85"
                  height="85"
                  alt="{username}"
                />
                <br />
                <sub><b>@{username}</b></sub>
              </a>
            </td>
            """)

        while len(cells) < 5:
            cells.append('<td width="20%"></td>')

        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")

    table = "\n".join(rows)

    return f"""
{START}

<div align="center">

# ✨ Stargazers

**A huge thank you to everyone supporting this project!**

<br />

<table>
  <tr>
    <td align="center">
      <h2>⭐ {len(users)}</h2>
      <sub>TOTAL STARGAZERS</sub>
    </td>
  </tr>
</table>

<br />

</div>

<table align="center" width="100%">
{table}
</table>

<div align="center">

<br />

*Every star makes a difference. Thank you for being part of this journey!*

</div>

{END}
"""


def update_readme(gallery):
    path = "README.md"

    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    else:
        content = "# Project\n\n"

    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError(
            "README must contain exactly one STARGAZERS:START "
            "and one STARGAZERS:END marker."
        )

    start_pos = content.index(START)
    end_pos = content.index(END)

    if end_pos < start_pos:
        raise ValueError("STARGAZERS markers are in the wrong order.")

    end_pos += len(END)

    updated = (
        content[:start_pos]
        + gallery
        + content[end_pos:]
    )

    with open(path, "w", encoding="utf-8") as file:
        file.write(updated)


def main():
    print("Fetching stargazers...")

    users = fetch_stargazers()

    print(f"Found {len(users)} stargazers.")

    gallery = generate_gallery(users)

    update_readme(gallery)

    print("Stargazers gallery successfully updated!")


if __name__ == "__main__":
    main()
