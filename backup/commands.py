#     Backup is a tool which makes day-to-day backups easier.
#
#     Copyright (C) 2019  kinteriq
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys

import check
import error
from file_handle import DATABASE
import shortcuts

COMMANDS = {
    'create': shortcuts.create,
    'update': shortcuts.update,
    'delete': shortcuts.delete,
    'show': shortcuts.show,
    'showall': shortcuts.showall,
    'clear': None,
}


def read_from_command_line(data) -> list:
    args = sys.argv[1:]  # exclude 'backup.py'
    try:
        check.empty(args)
        check.showall(arguments=args)
        check.shortcut_name(data, arguments=args)
        check.invalid_command(commands=COMMANDS, arguments=args)
    except error.Empty as e:
        sys.exit(e)
    except error.InvalidCommand as e:
        sys.exit(e)
    return args


def execute_command(command, params, data) -> str:
    message = COMMANDS[command](arguments=params, data=data)
    return message


if __name__ == '__main__':
    # add to tests
    print(execute_command('create', ['TEST', 'a', 'b']))
    print(execute_command('show', ['TEST']))
    print(execute_command('showall', []))
    print(execute_command('delete', ['TEST']))
    print(execute_command('showall', []))
