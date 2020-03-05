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

c.InteractiveShellApp.ignore_old_config=True

c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'linux'
c.TerminalInteractiveShell.highlighting_style = 'monokai'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.editor = 'vim'
c.InteractiveShell.xmode = 'Context'

c.PromptManager.in_template  = 'In [\#]: '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = 'Out[\#]: '
c.PromptManager.justify = True

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
     ('la', 'ls -al'),
     ('lh', 'ls -lht')
     
     ]

