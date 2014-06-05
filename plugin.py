import sublime
import sublime_plugin
import subprocess
import os


class Pep8Command(sublime_plugin.TextCommand):
    """pep8 command"""
    def run(self, view):
        if self.view.is_dirty():
            print("Please save the file")
        else:
            filename = self.view.file_name()
            if filename is None:
                print('Wirte some code, save it and then run this command')
                return
            name, ext = os.path.splitext(filename)
            if ext == ".py":
                try:
                    p = subprocess.Popen(['pep8', str(filename)],
                                         stdout=subprocess.PIPE)
                    (output, _) = p.communicate()
                    output = output.decode('utf-8')
                    if output == "" or output is None:
                        print('No pep8 errors found.')
                    else:
                        print(output)
                except subprocess.CalledProcessError as e:
                    print(str(e.output))
            else:
                print("This is not a Python file")
