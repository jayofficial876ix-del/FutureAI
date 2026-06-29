from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from services.indexer.workspace_indexer import WorkspaceIndexer


class WorkspaceWatcher(FileSystemEventHandler):

    def __init__(self, project):

        self.project = project
        self.indexer = WorkspaceIndexer()

        self.observer = Observer()

    # --------------------------------

    def start(self):

        self.observer.schedule(
            self,
            self.project,
            recursive=True
        )

        self.observer.start()

    # --------------------------------

    def stop(self):

        self.observer.stop()

        self.observer.join()

    # --------------------------------

    def on_modified(self, event):

        if event.is_directory:
            return

        if event.src_path.endswith(".py"):

            print(
                "Index updated:",
                event.src_path
            )

            self.indexer.index_file(
                event.src_path
            )

    # --------------------------------

    def on_created(self, event):

        self.on_modified(event)
