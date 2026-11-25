
import os
import requests
from html import escape

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["REPOSITORY"]

START = "<!-- STARGAZERS:START -->"
END = "<!-- STARGAZERS:END -->"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
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
    html = [
        START,
        "",
        '<div align="center">',
        "",
        "# ✨ Stargazers",
        "",
        "Thanks to everyone supporting this project!",
        "",
        f"### ⭐ {len(users)} Amazing Supporters",
        "",
        "</div>",
        "",
        '<table align="center" width="100%">'
    ]

    for i in range(0, len(users), 5):
        html.append("<tr>")

        for user in users[i:i + 5]:
            username = escape(user["login"])
            profile = escape(user["html_url"], quote=True)
            avatar = escape(user["avatar_url"], quote=True)

            html.append(f"""
<td align="center" width="20%">
  <a href="{profile}">
    <img src="{avatar}&size=120"
         width="90"
         height="90"
         alt="{username}" />
    <br/>
    <strong>@{username}</strong>
  </a>
</td>
""")

        html.append("</tr>")

    html.extend([
        "</table>",
        "",
        '<div align="center">',
        "",
        "*Made possible by this amazing community!*",
        "",
        "</div>",
        "",
        END
    ])

    return "\n".join(html)


def update_readme(gallery):
    path = "README.md"

    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError("Missing or duplicate Stargazers markers.")

    start = content.index(START)
    end = content.index(END) + len(END)

    if end < start:
        raise ValueError("Incorrect marker order.")

    content = content[:start] + gallery + content[end:]

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    users = fetch_stargazers()
    print(f"Found {len(users)} stargazers")

    gallery = generate_gallery(users)
    update_readme(gallery)

    print("Gallery updated successfully!")
