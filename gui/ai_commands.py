from ai.prompts import PROMPTS


def get_ai_commands(controller):

    return {

        "🤖 Improve Code":
            lambda: controller.run_ai_action("improve"),

        "📝 Explain Code":
            lambda: controller.run_ai_action("explain"),

        "🐞 Find Bugs":
            lambda: controller.run_ai_action("bugs"),

        "⚡ Optimize Code":
            lambda: controller.run_ai_action("optimize"),

        "🧹 Clean Code":
            lambda: controller.run_ai_action("clean"),

        "🧪 Generate Tests":
            lambda: controller.run_ai_action("tests"),

        "📚 Documentation":
            lambda: controller.run_ai_action("documentation"),

        "🔒 Security Review":
            lambda: controller.run_ai_action("security"),

        "🏗 Architecture Review":
            lambda: controller.run_ai_action("architecture"),

        "📄 Generate README":
            lambda: controller.run_ai_action("readme"),

        "📝 Commit Message":
            lambda: controller.run_ai_action("commit")
    }
