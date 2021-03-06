from interfaces.command import ICommand, CommandArgs
from implementations.optionalparameters import GenericCommandOptionalParameters
from implementations import CmdUtils
import json

class AzAiAppList(ICommand):
    def __init__(self):
        self.commands = CommandArgs(
            "First Command Arguments",
            ["az", "ai","app", "list"]
        )
        self.actual_command = ["az", "managedapp", "list"]

        filtered_args = [x for x in GenericCommandOptionalParameters.PARAMETERS if x.destination not in ["name"]]
        self.commands.add_arguments(filtered_args)

    def execute(self):
        cmd_line = self.get_command_line(self.commands.parse_result)
        output = CmdUtils.get_command_output(cmd_line)

        if CmdUtils.LAST_STD_ERR:
            print(CmdUtils.LAST_STD_ERR)
        else:
            print(json.dumps(output, indent=4))
