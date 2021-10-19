FRACTION = '-'
SUPERSCRIPT_DIFF = 10
SQUARE_ROOT = '\\sqrt'

class TexLet(object):       #TexLet is used for LaTex construction


    def __init__(self, template, insertion_points, extra):


        self.template = template
        import operator
        sorted_insertion_points = sorted(insertion_points.items(), key=operator.itemgetter(1))
        self.names = map(lambda i: i[0], sorted_insertion_points)
        self.poses = map(lambda i: i[1], sorted_insertion_points)
        self.tex_lets = {}
        self.extra = extra
    

    def insert(self, name, new_tex_let):

        if name not in self.names:
            raise RuntimeError('Insertion point name not found')
        else:
            self.tex_lets[name] = new_tex_let



    def __str__(self):

        if len(self.names) > 0:
            first_pos = self.poses[0]
            last_pos = self.poses[len(self.poses) - 1]


            def index_to_tex_let(index):
                return self.tex_lets[self.names[index]]

            







