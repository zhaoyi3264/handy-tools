import os

TOOL_DIR = os.path.join('.', 'tool')

def is_tool_file(file):
    is_file = os.path.isfile(os.path.join(TOOL_DIR, file))
    return is_file and file.endswith('.py') and (not file.startswith('__'))

TOOLS = []
for file in os.listdir(TOOL_DIR):
    if is_tool_file(file):
        mod = file[:-3]
        TOOLS.append(mod)
