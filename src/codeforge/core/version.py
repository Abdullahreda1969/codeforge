VERSION = (0, 1, 0)

def get_version():
    return '.'.join(map(str, VERSION))

def get_version_tuple():
    return VERSION

def print_version():
    print(f'CodeForge v{get_version()}')
