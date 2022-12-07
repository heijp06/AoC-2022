from file_system import Directory, File


class TreeParser:
    def __init__(self, rows: list[str]) -> Directory:
        self.rows = rows
        self.root = None
        self.current_directory = None

    def parse(self) -> Directory:
        for row in self.rows:
            match row.split():
                case ['$', 'cd', '/']:
                    self.parse_root()
                case ['$', 'cd', '..']:
                    self.parse_up()
                case ['$', 'cd', name]:
                    self.parse_down(name)
                case ['$', 'ls']:
                    continue
                case ['dir', name]:
                    self.add_dir(name)
                case [size, name]:
                    self.add_file(name, int(size))
        return self.root

    def parse_root(self) -> None:
        if not self.root:
            self.root = Directory("")
        self.current_directory = self.root

    def parse_up(self) -> None:
        self.current_directory = self.current_directory.parent

    def parse_down(self, name: str) -> None:
        child = self.current_directory.find_entry(name)
        self.current_directory = child

    def add_dir(self, name: str) -> None:
        self.current_directory.entries.append(Directory(name, self.current_directory))
    
    def add_file(self, name: str, size: int) -> None:
        self.current_directory.entries.append(File(name, size))
