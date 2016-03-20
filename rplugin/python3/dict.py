import neovim

@neovim.plugin
class Dict(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.command('Dict', range='', nargs='*')
    def command_handler(self, args, range):
        self.vim.current.line = (
            'Command: Called %d times, args: %s, range: %s' % (self.calls,
                                                               args,
                                                               range))

