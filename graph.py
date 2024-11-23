with open("import_modules.py") as f:
    exec(f.read())

class GraphViz:
    def __init__(self, data, title, words_per_line = 5):
        self.words_per_line = words_per_line
        self.title = title
        self.subj = data['arg1'].to_list()
        self.obj = data['arg2'].to_list()
        self.rel = data['rel'].to_list()
        
        self.first_level_nodes = set(data['arg1']).difference(set(data['arg2']))
        
        self.nodes = []
        self.edges = []
        self.seen = set()
        self.graph = pydot.Dot(graph_type='digraph', ordering = 'out', rankdir = 'LR') #layout = 'sfdp',
        self.fill_graph()
    
    def __str__(self):
        return 'Nodes:' + str(self.nodes) + '\n' + 'Edges:' + str(self.edges)
    
    def get_node(self, text):
        if text.lower() in self.seen:
            for node in self.nodes:
                if node.get_attributes()['label'].lower() == text.lower() or self.title == text.lower():
                    return node
        
        text_split = text.split(' ')
        text_len = len(text_split)
        if text_len > self.words_per_line:
            new_text = text_split[:self.words_per_line]
            for i in range(self.words_per_line, text_len, self.words_per_line):
                new_text += ['\n'] + text_split[i:i+self.words_per_line] 
                node = pydot.Node(text, label = ' '.join(new_text))
        else:
                node = pydot.Node(text, label = text)
                
        self.nodes.append(node)
        self.graph.add_node(node)
        self.seen.add(text.lower())
        return node
    
    def add_edge(self, node1, node2, r = ''):
        edge = pydot.Edge(node1, node2, label = ' ' + r, color='orange')
        self.edges.append(edge)
        self.graph.add_edge(edge)
        
            
    def fill_graph(self):
        central_node = pydot.Node(unidecode(self.title), label=f'<<font face="bold"> {self.title} </font>>', color='orange')
        self.nodes.append(central_node)
        self.graph.add_node(central_node)
        self.seen.add(self.title.lower())
        
        seen_c1 = set()
        for c1, c2, r in zip(self.subj, self.obj, self.rel):
            #print(c1, c2, r)
            if c1 != self.title:
                node1 = self.get_node(c1)
                if c1 in self.first_level_nodes and c1 not in seen_c1:
                    seen_c1.add(c1)
                    self.add_edge(central_node, node1)
            else:
                node1 = central_node
            node2 = self.get_node(c2)  
            self.add_edge(node1, node2, r)