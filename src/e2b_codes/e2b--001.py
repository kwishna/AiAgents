from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox

sbx = Sandbox() # By default the sandbox is alive for 5 minutes
execution = sbx.run_code("print('hello world')") # Execute Python inside the sandbox
print(execution.logs)

files = sbx.files.list("/")
print(files)

'''
└─$ python ./src/e2b_codes/e2b--001.py 
Logs(stdout: ['hello world\n'], stderr: [])
[EntryInfo(name='.dockerenv', type=<FileType.FILE: 'file'>, path='/.dockerenv'),
EntryInfo(name='.e2b', type=<FileType.FILE: 'file'>, path='/.e2b'),
EntryInfo(name='bin', type=<FileType.FILE: 'file'>, path='/bin'),
EntryInfo(name='boot', type=<FileType.DIR: 'dir'>, path='/boot'),
EntryInfo(name='code', type=<FileType.DIR: 'dir'>, path='/code'),
EntryInfo(name='dev', type=<FileType.DIR: 'dir'>, path='/dev'),
EntryInfo(name='etc', type=<FileType.DIR: 'dir'>, path='/etc'),
EntryInfo(name='home', type=<FileType.DIR: 'dir'>, path='/home'),
EntryInfo(name='ijava-1.3.0.zip', type=<FileType.FILE: 'file'>, path='/ijava-1.3.0.zip'),
EntryInfo(name='install.py', type=<FileType.FILE: 'file'>, path='/install.py'),
EntryInfo(name='java', type=<FileType.DIR: 'dir'>, path='/java'),
EntryInfo(name='lib', type=<FileType.FILE: 'file'>, path='/lib'),
EntryInfo(name='lib64', type=<FileType.FILE: 'file'>, path='/lib64'),
EntryInfo(name='lost+found', type=<FileType.DIR: 'dir'>, path='/lost+found'),
EntryInfo(name='media', type=<FileType.DIR: 'dir'>, path='/media'),
EntryInfo(name='mnt', type=<FileType.DIR: 'dir'>, path='/mnt'),
EntryInfo(name='opt', type=<FileType.DIR: 'dir'>, path='/opt'),
EntryInfo(name='proc', type=<FileType.DIR: 'dir'>, path='/proc'),
EntryInfo(name='r-4.4.2_1_amd64.deb', type=<FileType.FILE: 'file'>, path='/r-4.4.2_1_amd64.deb'),
EntryInfo(name='requirements.txt', type=<FileType.FILE: 'file'>, path='/requirements.txt'),
EntryInfo(name='root', type=<FileType.DIR: 'dir'>, path='/root'),
EntryInfo(name='run', type=<FileType.DIR: 'dir'>, path='/run'),
EntryInfo(name='sbin', type=<FileType.FILE: 'file'>, path='/sbin'),
EntryInfo(name='srv', type=<FileType.DIR: 'dir'>, path='/srv'),
EntryInfo(name='swap', type=<FileType.DIR: 'dir'>, path='/swap'),
EntryInfo(name='sys', type=<FileType.DIR: 'dir'>, path='/sys'),
EntryInfo(name='tmp', type=<FileType.DIR: 'dir'>, path='/tmp'),
EntryInfo(name='usr', type=<FileType.DIR: 'dir'>, path='/usr'),
EntryInfo(name='var', type=<FileType.DIR: 'dir'>, path='/var')]
'''
