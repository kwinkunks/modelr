from modelr.web.urlargparse import SendHelp, URLArgumentParser


class ModelrScript(object):

    def __init__(self, plot_json, namespace):

        # Parse additional arguments that may be required by the
        # script
        add_arguments = namespace['add_arguments']
        short_description = namespace.get('short_description',
                                          'No description')

        parser = URLArgumentParser(short_description)
        add_arguments(parser)
        try:
            args = parser.parse_params(plot_json)
        except SendHelp:
            raise SendHelp

        self.args = args
        self.script = namespace['run_script']

    def go(self):

        self.plot, metadata = self.script(self.args)

        return self.plot, metadata
