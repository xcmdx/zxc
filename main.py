from blockdiag import parser, builder, drawer
tree = parser.parse_string(sour)
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="foo.png")
draw.draw()
draw.save()