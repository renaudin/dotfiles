# sample ipython_config.py
c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
c.TerminalInteractiveShell.editing_mode = 'vi'
#c.InteractiveShellApp.extensions = [
#        'myextension'
#        ]
#c.InteractiveShellApp.exec_lines = [
#        'import numpy',
#            'import scipy'
#        ]
#c.InteractiveShellApp.exec_files = [
#        'mycode.py',
#            'fancy.ipy'
#        ]


c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'linux'
c.TerminalInteractiveShell.highlighting_style = 'monokai'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.editor = 'vim'
c.InteractiveShell.xmode = 'Context'

c.TerminalInteractiveShell.prompts_class.in_template  = 'In [\#]: '
c.TerminalInteractiveShell.prompts_class.in2_template = '   .\D.: '
c.TerminalInteractiveShell.prompts_class.out_template = 'Out[\#]: '
c.TerminalInteractiveShell.prompts_class.justify = True

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
     ('la', 'ls -al'),
     ('lh', 'ls -lht')
     
     ]

