import random
import math

# Stores the vnode to node mapping
# Composed within a node so that every node has its own vnode mapping
class VirtualNodeMap:
    def __init__(self, node_names, TOTAL_VIRTUAL_NODES):
        self._vnode_map = {}
        self._node_names = node_names
        self._TOTAL_VIRTUAL_NODES = TOTAL_VIRTUAL_NODES

    @property
    def vnode_map(self):
        return self._vnode_map

    @property
    def node_names(self):
        return self._node_names

    # Populates the Virtual Node Map, given the set of Node names.
    # Creates a mapping of Virtual Node to corresponding assigned physical Node
    def populate_map(self):
        nodesz = len( self.node_names )
        for vnode in range(0,self._TOTAL_VIRTUAL_NODES):
            self._vnode_map[vnode] = self._node_names[vnode % nodesz]

        # Problem statement 1
        # Generate a dict of vnode ids (0 to (TOTAL_VIRTUAL_NODES - 1) mapped randomly 
        # but equally (as far as maths permits) to node names
        #pass

    # Return the vnode name mapped to a particular vnode
    def get_node_for_vnode(self, vnode):
        return self._vnode_map[vnode]

    # Returns the vnode name where a particular key is stored
    # It finds the vnode for the key through modulo mapping, and then looks up the physical node
    def get_assigned_node(self, key):
        vnode = key % self._TOTAL_VIRTUAL_NODES
        return self._vnode_map[vnode]

    # Assign a new node name as mapping for a particular vnode
    # This is useful when vnodes are remapped during node addition or removal
    def set_new_assigned_node(self, vnode, new_node_name):
        self._vnode_map[vnode] = new_node_name

