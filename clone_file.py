import sublime_plugin

class CloneFileToGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        if self.window.num_groups() == 1:
            self.window.run_command('set_layout',
                            {
                                "cols": [0.0, 0.5, 1.0],
                                "rows": [0.0, 1.0],
                                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
                            })
        self.window.run_command('clone_file')
        self.window.run_command('move_to_group', {"group": 1})
