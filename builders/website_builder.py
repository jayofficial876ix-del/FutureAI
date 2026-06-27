import os

def build_website(name):

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{name}</title>
</head>

<body>

<h1>Welcome to {name}</h1>

<p>This website was created by Future AI.</p>

</body>
</html>
"""

    os.makedirs("projects", exist_ok=True)

    filename = f"projects/{name.replace(' ', '_')}.html"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

    return filename