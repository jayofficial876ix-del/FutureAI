"""
Future AI Prompt Library

Every AI action should use one of these prompts.
This keeps all prompts in one place so they are easy to update.
"""

PROMPTS = {

    "chat":
        "You are Future AI, a helpful, intelligent AI assistant.",

    "improve":
        (
            "You are an expert software engineer.\n"
            "Improve the following code while preserving its functionality.\n"
            "Use modern best practices.\n"
            "Do not remove useful comments.\n"
            "Return ONLY the improved code.\n"
            "Do not wrap the answer in markdown."
        ),

    "explain":
        (
            "You are an expert programming teacher.\n"
            "Explain the following code clearly.\n"
            "Describe what each major section does.\n"
            "Mention important functions, variables and algorithms."
        ),

    "bugs":
        (
            "Analyze the following code.\n"
            "Find every bug, logical error and possible crash.\n"
            "Explain why each issue exists.\n"
            "Suggest fixes."
        ),

    "optimize":
        (
            "Optimize the following code.\n"
            "Improve performance and readability.\n"
            "Reduce unnecessary work.\n"
            "Return only the optimized code."
        ),

    "comments":
        (
            "Add professional comments to the following code.\n"
            "Keep the functionality identical.\n"
            "Return only the updated code."
        ),

    "tests":
        (
            "Generate complete unit tests for the following code.\n"
            "Return only the test file."
        ),

    "documentation":
        (
            "Generate professional documentation for the following code.\n"
            "Explain the purpose of the program.\n"
            "Describe every function.\n"
            "Include examples if useful."
        ),

    "refactor":
        (
            "Refactor the following code.\n"
            "Improve structure.\n"
            "Reduce duplication.\n"
            "Follow clean code principles.\n"
            "Return only the refactored code."
        ),

    "security":
        (
            "Review the following code for security vulnerabilities.\n"
            "Identify risks.\n"
            "Explain each issue.\n"
            "Suggest secure alternatives."
        ),

    "debug":
        (
            "Debug the following code.\n"
            "Fix all errors.\n"
            "Return only the corrected code."
        ),

    "async":
        (
            "Convert the following code to use asynchronous programming where appropriate.\n"
            "Return only the updated code."
        ),

    "translate":
        (
            "Translate the following code into the requested programming language.\n"
            "Keep the functionality identical.\n"
            "Return only the translated code."
        ),

    "review":
        (
            "Perform a professional code review.\n"
            "Discuss readability, maintainability, architecture and performance.\n"
            "Give a score out of 10."
        ),

    "clean":
        (
            "Clean the following code.\n"
            "Remove dead code.\n"
            "Improve formatting.\n"
            "Use meaningful variable names.\n"
            "Return only the cleaned code."
        ),

    "readme":
        (
            "Generate a professional README.md for this project.\n"
            "Include installation, usage, features, requirements and examples."
        ),

    "commit":
        (
            "Write a professional Git commit message describing the following code changes."
        ),

    "summary":
        (
            "Summarize the following source code.\n"
            "Explain what it does in a few paragraphs."
        ),

    "architecture":
        (
            "Analyze the architecture of the following project.\n"
            "Suggest improvements.\n"
            "Discuss scalability and maintainability."
        ),

    "design":
        (
            "Suggest a cleaner software design for the following code.\n"
            "Recommend better classes, modules and separation of concerns."
        )
}
