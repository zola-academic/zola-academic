#!/usr/bin/env python3

class Colorschemes:
    def __init__(self, schemes):
        self.schemes = schemes

    def render(self, out):
        default_scheme = Colorscheme('')

        for property in Colorscheme.properties():
            out.write('{% macro ')
            out.write(property)
            out.write('() %}')
            out.write('{% if config.extra.colorscheme %}')
            for id, scheme in enumerate(self.schemes):
                if id == 0:
                    out.write('{% if config.extra.colorscheme == "' + scheme.name + '" %}')
                else:
                    out.write('{% elif config.extra.colorscheme == "' + scheme.name + '" %}')
                out.write(scheme.__getattribute__(property))
            out.write('{% else %}')
            out.write(default_scheme.__getattribute__(property))
            out.write('{% endif %}')
            out.write('{% else %}')
            out.write(default_scheme.__getattribute__(property))
            out.write('{% endif %}')
            out.write('{% endmacro %}\n')


class Colorscheme:
    def properties():
        return ['background', 'navbar_style', 'style']

    def __init__(self, name):
        self.name = name
        self.background = "white"
        self.navbar_style = "light"
        self.style = "info"

def main():
    default = Colorscheme("default")
    default.navbar_style = "light"
    default.style = "dark"

    ocean = Colorscheme("ocean")
    ocean.navbar_style = "link"
    ocean.style = "link"

    forest = Colorscheme("forest")
    forest.navbar_style = "success"
    forest.style = "success"

    colorschemes = Colorschemes([default, ocean, forest])

    with open('templates/colors.html', 'w') as f:
        colorschemes.render(f)

if __name__ == '__main__':
    main()


