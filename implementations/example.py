import json
from implementations import CmdUtils
from interfaces.command import ICommand, Argument, CommandArgs

class ExampleCommand(ICommand):
    def __init__(self):
        self.commands = CommandArgs(
            "Example Command",
            ["az", "vm", "list"]
        )

        arguments = [
            # Actual params supply a type
            Argument(["--ids", "-i"], "resource_ids", False, str, "Resource ID's"),
            # Flags don't provide a type
            Argument("--no-wait", "wait", False, None, "Do not wait")
        ]

        self.commands.add_arguments(arguments)

    def execute(self):
        print("Example Command Execute....")
        print(self.commands.parse_result)

