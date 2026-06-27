import os
import webbrowser


def build_website(name):

    # Safe folder name
    folder_name = name.lower().replace(" ", "_")

    project_folder = os.path.join("projects", folder_name)
    os.makedirs(project_folder, exist_ok=True)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

<header>
    <h1>{name}</h1>
    <p>Created with Future AI 🚀</p>
</header>

<section>
    <h2>Welcome</h2>
    <p>This is your brand new website.</p>

    <button onclick="sayHello()">
        Click Me
    </button>
</section>

<script src="script.js"></script>

</body>
</html>
"""

    css = """
body{
    margin:0;
    font-family:Arial, sans-serif;
    background:#111827;
    color:white;
    text-align:center;
}

header{
    background:#2563eb;
    padding:50px;
}

section{
    padding:60px;
}

button{
    background:#2563eb;
    color:white;
    border:none;
    padding:15px 30px;
    border-radius:10px;
    cursor:pointer;
    font-size:16px;
}

button:hover{
    background:#1d4ed8;
}
"""

    javascript = """
function sayHello(){
    alert("Welcome! This website was created by Future AI 🚀");
}
"""

    index_file = os.path.join(project_folder, "index.html")
    css_file = os.path.join(project_folder, "style.css")
    js_file = os.path.join(project_folder, "script.js")

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(html)

    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css)

    with open(js_file, "w", encoding="utf-8") as f:
        f.write(javascript)

    # Automatically open the website
    webbrowser.open(index_file)

    return project_folder
