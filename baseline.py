with open("import_modules.py") as f:
    exec(f.read())

from graph import GraphViz

def baseline_cmap(df, title, min_conf_level=0.75):
    """
        Baseline model for concept maps.
        min_conf_level is the percentile of the confidence score distribution from which we draw
    """
    df_filtered = df[df["confidence"] >= df["confidence"].quantile(min_conf_level)]
    G = GraphViz(df_filtered, title)
    title = title.replace(' ', '_')
    G.graph.write_png(f'example_graph_baseline_{title}_{min_conf_level}.png')


# Test with baseline
with open("../data/eval_extract.pickle", 'rb') as f: 
    data = pickle.load(f)

# Maps generation
for i in data.keys():
    baseline_cmap(data[i], i)