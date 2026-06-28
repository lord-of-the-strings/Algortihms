import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx
import sys
sys.setrecursionlimit(2000)

class MergeSortTreeVisualizer:
    def __init__(self, array):
        self.array = array
        self.graph = nx.DiGraph()
        self.node_labels = {}
        self.node_colors = {}
        self.counter = 0 
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        self.fig.canvas.manager.set_window_title("Merge Sort")

    def create_layout(self):
        """
        Use in-order traversal to assign X coordinates cleanly.
        """
        position_map = {}
        self.x_counter = 0  # Tracks horizontal placement ordering

        def traverse(node, depth=0):
            if node is None:
                return
            
            children = list(self.graph.successors(node))
            
            if len(children) > 0:
                traverse(children[0], depth + 1)
            
            
            position_map[node] = (self.x_counter, -depth)
            self.x_counter += 1
            
            if len(children) > 1:
                traverse(children[1], depth + 1)

        traverse(0)
        return position_map

    def redraw_tree(self):
        """Clears the axis and updates the visual layout with current states."""
        self.ax.clear()
        if not self.graph.nodes:
            return
            
        pos = self.create_layout()
        
        colors = [self.node_colors.get(node, "lightblue") for node in self.graph.nodes]
        
        nx.draw_networkx_edges(self.graph, pos, ax=self.ax, edge_color="gray", arrows=False)
        nx.draw_networkx_nodes(self.graph, pos, ax=self.ax, node_size=4500, node_color=colors, edgecolors="black")
        nx.draw_networkx_labels(self.graph, pos, labels=self.node_labels, ax=self.ax, font_size=10, font_weight="bold")
        
        self.ax.margins(0.2)
        self.ax.axis("off")
        
        plt.draw()
        plt.pause(0.6)

    def sort_and_visualize(self):
        """Public starter method."""
        root_id = self.counter
        self.graph.add_node(root_id)
        self.node_labels[root_id] = str(self.array)
        self.node_colors[root_id] = "lightcoral" # Light Red: Currently Processing/Splitting
        
        self.redraw_tree()
        self._merge_sort(self.array, root_id)
        
        plt.ioff()
        plt.show(block=True)

    def _merge_sort(self, arr, current_node_id):
        if len(arr) <= 1:
            # Base case reached: turn node green (sorted subarray)
            self.node_colors[current_node_id] = "lightgreen"
            self.redraw_tree()
            return arr

        mid = len(arr) // 2
        
        self.counter += 1
        left_id = self.counter
        self.graph.add_edge(current_node_id, left_id)
        self.node_labels[left_id] = str(arr[:mid])
        self.node_colors[left_id] = "lightcoral"
        self.redraw_tree()
        left_sorted = self._merge_sort(arr[:mid], left_id)

        self.counter += 1
        right_id = self.counter
        self.graph.add_edge(current_node_id, right_id)
        self.node_labels[right_id] = str(arr[mid:])
        self.node_colors[right_id] = "lightcoral"
        self.redraw_tree()
        right_sorted = self._merge_sort(arr[mid:], right_id)

        merged = self._merge(left_sorted, right_sorted)
        
        self.node_labels[current_node_id] = str(merged)
        self.node_colors[current_node_id] = "lightgreen" # Green: Merged and Sorted
        self.redraw_tree()
        
        return merged

    def _merge(self, left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

# --- Execution ---
if __name__ == "__main__":
    # Test array (keep size between 5-10 for clear visual spacing)
    unsorted_data = [14, 3, 9, 7, 1, 11]
    
    visualizer = MergeSortTreeVisualizer(unsorted_data)
    visualizer.sort_and_visualize()
