import customtkinter as ctk

from gui.layout.activity_column import ActivityColumn
from gui.sidebar_stack import SidebarStack
from gui.placeholder_page import PlaceholderPage
from gui.project_explorer import ProjectExplorer

from gui.left_sidebar import LeftSidebar
from gui.center_chat import CenterChat
from gui.editor_panel import EditorPanel
from gui.right_sidebar import RightSidebar

from projects.project_manager import load_projects


class AppLayout(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.pack(fill="both", expand=True)

        # --------------------------------
        # Grid Layout
        # --------------------------------

        self.grid_columnconfigure(0, weight=0, minsize=60)
        self.grid_columnconfigure(1, weight=0, minsize=260)
        self.grid_columnconfigure(2, weight=3)
        self.grid_columnconfigure(3, weight=4)
        self.grid_columnconfigure(4, weight=0, minsize=300)

        self.grid_rowconfigure(0, weight=1)

        # --------------------------------
        # Sidebar Stack
        # --------------------------------

        self.left = SidebarStack(self)

        self.left.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        # --------------------------------
        # Activity Bar
        # --------------------------------

        self.activity = ActivityColumn(
            self,
            self.left
        )

        self.activity.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # --------------------------------
        # Chat Sidebar
        # --------------------------------

        self.chat_page = LeftSidebar(
            self.left,
            controller
        )

        # --------------------------------
        # Editor
        # --------------------------------

        self.editor = EditorPanel(
            self,
            controller
        )

        self.editor.grid(
            row=0,
            column=3,
            sticky="nsew"
        )

        controller.editor = self.editor

        # --------------------------------
        # Project Explorer
        # --------------------------------

        self.explorer_page = ProjectExplorer(
            self.left,
            self.editor.open_file
        )

        # --------------------------------
        # Other Pages
        # --------------------------------

        self.search_page = PlaceholderPage(
            self.left,
            "🔍 Search"
        )

        self.agent_page = PlaceholderPage(
            self.left,
            "🤖 AI Agents"
        )

        self.tools_page = PlaceholderPage(
            self.left,
            "🛠 Tools"
        )

        self.settings_page = PlaceholderPage(
            self.left,
            "⚙ Settings"
        )

        # --------------------------------
        # Register Sidebar Pages
        # --------------------------------

        self.left.add("chat", self.chat_page)
        self.left.add("explorer", self.explorer_page)
        self.left.add("search", self.search_page)
        self.left.add("agent", self.agent_page)
        self.left.add("tools", self.tools_page)
        self.left.add("settings", self.settings_page)

        self.left.show("chat")

        # --------------------------------
        # Center Chat
        # --------------------------------

        self.center = CenterChat(
            self,
            controller
        )

        self.center.grid(
            row=0,
            column=2,
            sticky="nsew"
        )

        # --------------------------------
        # Right Sidebar
        # --------------------------------

        self.right = RightSidebar(self)

        self.right.grid(
            row=0,
            column=4,
            sticky="nsew"
        )

        # Give the controller access to the AI Workspace
        controller.right_sidebar = self.right

        # --------------------------------
        # Load Project Into Explorer
        # --------------------------------

        try:
            projects = load_projects()

            if projects:
                project = projects[0]

                if isinstance(project, dict):
                    project_path = project.get("path")
                else:
                    project_path = project

                if project_path:
                    self.explorer_page.load_project(
                        project_path
                    )

        except Exception as e:
            print("Explorer:", e)
