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

        self.controller = controller

        self.pack(
            fill="both",
            expand=True
        )

        self._configure_grid()
        self._create_sidebar_stack()
        self._create_activity_bar()
        self._create_sidebar_pages()
        self._create_center_chat()
        self._create_editor()
        self._create_right_sidebar()

        self._register_pages()

        self._load_project()

    # --------------------------------------------------
    # Grid
    # --------------------------------------------------

    def _configure_grid(self):

        self.grid_columnconfigure(
            0,
            weight=0,
            minsize=60
        )

        self.grid_columnconfigure(
            1,
            weight=0,
            minsize=260
        )

        self.grid_columnconfigure(
            2,
            weight=3
        )

        self.grid_columnconfigure(
            3,
            weight=4
        )

        self.grid_columnconfigure(
            4,
            weight=0,
            minsize=320
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

    # --------------------------------------------------
    # Sidebar Stack
    # --------------------------------------------------

    def _create_sidebar_stack(self):

        self.left = SidebarStack(self)

        self.left.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

    # --------------------------------------------------
    # Activity Bar
    # --------------------------------------------------

    def _create_activity_bar(self):

        self.activity = ActivityColumn(
            self,
            self.left
        )

        self.activity.grid(
            row=0,
            column=0,
            sticky="ns"
        )

    # --------------------------------------------------
    # Sidebar Pages
    # --------------------------------------------------

    def _create_sidebar_pages(self):

        self.chat_page = LeftSidebar(
            self.left,
            self.controller
        )

        self.explorer_page = ProjectExplorer(
            self.left,
            self.open_file
        )

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

    # --------------------------------------------------
    # Center Chat
    # --------------------------------------------------

    def _create_center_chat(self):

        self.center = CenterChat(
            self,
            self.controller
        )

        self.center.grid(
            row=0,
            column=2,
            sticky="nsew"
        )

    # --------------------------------------------------
    # Editor
    # --------------------------------------------------

    def _create_editor(self):

        self.editor = EditorPanel(
            self,
            self.controller
        )

        self.editor.grid(
            row=0,
            column=3,
            sticky="nsew"
        )

        self.controller.editor = self.editor

    # --------------------------------------------------
    # Right Sidebar
    # --------------------------------------------------

    def _create_right_sidebar(self):

        self.right = RightSidebar(self)

        self.right.grid(
            row=0,
            column=4,
            sticky="nsew"
        )

        self.controller.right_sidebar = self.right

    # --------------------------------------------------
    # Register Pages
    # --------------------------------------------------

    def _register_pages(self):

        self.left.add(
            "chat",
            self.chat_page
        )

        self.left.add(
            "explorer",
            self.explorer_page
        )

        self.left.add(
            "search",
            self.search_page
        )

        self.left.add(
            "agent",
            self.agent_page
        )

        self.left.add(
            "tools",
            self.tools_page
        )

        self.left.add(
            "settings",
            self.settings_page
        )

        self.left.show("chat")

    # --------------------------------------------------
    # Open File
    # --------------------------------------------------

    def open_file(self, filename):

        self.editor.open_file(filename)

    # --------------------------------------------------
    # Load Project
    # --------------------------------------------------

    def _load_project(self):

        try:

            projects = load_projects()

            if not projects:
                return

            project = projects[0]

            if isinstance(
                project,
                dict
            ):

                path = project.get(
                    "path"
                )

            else:

                path = project

            if path:

                self.explorer_page.load_project(
                    path
                )

        except Exception as e:

            print(
                "Project Explorer:",
                e
            )
