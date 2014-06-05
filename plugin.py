import sublime
import sublime_plugin
import subprocess
import os


class Pep8Command(sublime_plugin.TextCommand):
    """pep8 command"""
    def run(self, view):
        if self.view.is_dirty():
            sublime.message_dialog("Please save the file")
        else:
            filename = self.view.file_name()
            if filename is None:
                sublime.message_dialog('Wirte some code, save it and then run \
                    this command')
                return
            name, ext = os.path.splitext(filename)
            if ext == ".py":
                try:
                    p = subprocess.Popen(['pep8', str(filename)],
                                         stdout=subprocess.PIPE)
                    (output, _) = p.communicate()
                    output = output.decode('utf-8')
                    if output == "" or output is None:
                        sublime.message_dialog('No pep8 errors found.')
                    else:
                        sublime.message_dialog(output)
                except subprocess.CalledProcessError as e:
                    sublime.message_dialog(str(e.output))
            else:
                sublime.message_dialog("This is not a Python file")
