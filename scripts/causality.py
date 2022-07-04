from causalnex.structure import StructureModel
from causalnex.structure.notears import from_pandas
from IPython.display import Image
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
import warnings
warnings.filterwarnings("ignore")  # silence warnings
import pandas as pd
import numpy as np
import sys, os
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))


class causality:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.sm = StructureModel()

    def set_empty_structure(self) -> None:
        self.sm = from_pandas(self.df, tabu_edges=[("diagnosis")], w_threshold=0.8)

    def normal_plot(self) -> pd.DataFrame:
    
        viz = plot_structure(
            self.sm,
            graph_attributes={"scale": "0.5"},
            all_node_attributes=NODE_STYLE.WEAK,
            all_edge_attributes=EDGE_STYLE.WEAK,
        )
        Image(viz.draw(format='png'))
    
    def jaccard_similarity(self, percentage, g, h):
        portion = int(self.df.shape[0]* percentage)
        data_por = self.df.head(portion)
        sm2 = from_pandas(data_por, tabu_parent_nodes=['diagnosis'])
        sm2.remove_edges_below_threshold(0.8)
        sm2 = sm2.get_largest_subgraph()
        i = set(g).intersection(h)
        return round(len(i) / (len(g) + len(h) - len(i)), 3)
   