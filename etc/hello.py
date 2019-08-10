# CONFIG = {
#     'mode': 'wsgi',
#     'working_dir': '/home/box/web',
#     'python': '/usr/bin/python',
#     'args': (
#         '--bind=0.0.0.0:8080',
#         '--workers=2',
#         '--timeout=60',
#         '--daemon',
#         'hello:application',
#     ),
# }
CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    'python': '/usr/bin/python3',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        '--log-level=debug',
        'hello',
    ),
}
#bind='0.0.0.0:8080'