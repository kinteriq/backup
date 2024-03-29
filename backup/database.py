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

import functools
import os
import outputs
import sqlite3


def db_creator(datapath):
    if not os.path.exists(os.path.split(datapath)[0]):
        raise SystemExit(outputs.ERROR_MSG['wrong_custom_datapath'])
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS shortcuts
        (name TEXT PRIMARY KEY, source TEXT, destinations TEXT)''')
    connection.commit()
    connection.close()


def db_connect(func):   # TODO @db_connect(datapath)
    """
    Manages the connection with the database, which is in the 'datapath' file.
    """
    @functools.wraps(func)
    def wrapper(datapath, args=tuple()):    # TODO *args
        connection = sqlite3.connect(datapath)
        cursor = connection.cursor()
        result = func(args, datapath=datapath, db_cursor=cursor)
        connection.commit()
        connection.close()
        return result
    return wrapper
