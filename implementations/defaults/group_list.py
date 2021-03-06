from interfaces.command import ICommand, CommandArgs
from implementations.optionalparameters import GenericCommandOptionalParameters
from implementations import CmdUtils
import json

class AzGroupList(ICommand):
    def __init__(self):
        self.commands = CommandArgs(
            "List azure resource groups",
            ["az", "ai","group", "list"]
        )
        self.actual_command = ["az", "group", "list"]

        filtered_args = [x for x in GenericCommandOptionalParameters.PARAMETERS if x.destination not in ["name", "resource_group"]]
        self.commands.add_arguments(filtered_args)


    def execute(self):
        cmd_line = self.get_command_line(self.commands.parse_result)
        output = CmdUtils.get_command_output(cmd_line)
       
        if CmdUtils.LAST_STD_ERR:
            print(CmdUtils.LAST_STD_ERR)
        else:
            print(json.dumps(output, indent=4))
