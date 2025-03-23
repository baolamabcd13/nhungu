from graphviz import Digraph

dot = Digraph(format='png')
dot.attr(rankdir='LR', nodesep='0.6', ranksep='0.9')
dot.attr('node', shape='box')

dot.node('label_P1', 'P1', shape='plaintext')
dot.node('R1a', 'Reactor P1-1')
dot.node('E1a', 'Extruder P1-1')
dot.node('R1b', 'Reactor P1-2')
dot.node('E1b', 'Extruder P1-2')
dot.node('PK1_1', 'Pkg.Mch.P1-1')
dot.node('PK1_2', 'Pkg.Mch.P1-2')
dot.node('Out1_1', '', shape='point', width='0')
dot.node('Out1_2', '', shape='point', width='0')

dot.edge('label_P1', 'R1a')
dot.edge('label_P1', 'R1b')

dot.edge('R1a', 'E1a')
dot.edge('R1b', 'E1b')

dot.edge('E1a', 'PK1_1')
dot.edge('E1a', 'PK1_2')
dot.edge('E1b', 'PK1_1')
dot.edge('E1b', 'PK1_2')

dot.edge('PK1_1', 'Out1_1')
dot.edge('PK1_2', 'Out1_2')

dot.node('label_P0', 'P0', shape='plaintext')
dot.node('R0', 'Reactor P0-1')
dot.node('E0', 'Extruder P0-1')
dot.node('PK0_1', 'Pkg.Mch.P0-1')
dot.node('PK0_2', 'Pkg.Mch.P0-2')
dot.node('Out0_1', '', shape='point', width='0')
dot.node('Out0_2', '', shape='point', width='0')

dot.edge('label_P0', 'R0')
dot.edge('R0', 'E0')
dot.edge('E0', 'PK0_1')
dot.edge('E0', 'PK0_2')
dot.edge('PK0_1', 'Out0_1')
dot.edge('PK0_2', 'Out0_2')


with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('R0')
    s.node('R1a')
    s.node('R1b')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('E0')
    s.node('E1a')
    s.node('E1b')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('PK0_1')
    s.node('PK0_2')
    s.node('PK1_1')
    s.node('PK1_2')

dot.render('quy_trinh_co_so_san_xuat', view=True)