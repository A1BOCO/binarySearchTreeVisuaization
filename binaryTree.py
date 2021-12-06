import tkinter
from random import randint



diameter = 100
radius = diameter /2
fontSize = 30


class Node:

    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, canvas):
        self.root = None
        self.canvas = canvas

    def buildBinaryTree(self, arr):
        self.buildBinaryTreeHelper(0, len(arr)-1, arr)

    def buildBinaryTreeHelper(self, start, end, arr):
        if start == end:
            return Node(arr[start],None,None)

        mid = int(len(arr)/2)
        left = None
        if start <= mid-1:
            left = self.buildBinaryTreeHelper(start, mid-1, arr)
        right = None
        if end >= mid+1:
            right = self.buildBinaryTreeHelper(mid+1, end, arr)

        root = BinaryTree(arr[mid], left, right)
        return root

    def addNode(self, num):
        tag = ""
        if self.root is None:
            self.root = Node(num)
            tag = "tag_"+str(self.root.data)
            self.create_circle_center_position(900,100,100,30,self.root.data,tag)
        else:
            iterator = self.root
            node = Node(num)
            tag = "tag_"+str(self.root.data)
            while iterator is not None:
                if iterator.data == node.data:
                    return 'duplicate number'
                    break
                if iterator.data < node.data and iterator.right == None:
                    # insert Node to Binary tree
                    iterator.right = node
                    # get parent node position
                    value = self.canvas.bbox("tag_"+str(iterator.data))
                    # get parent node center position and next chile node center position
                    x_parent_center,y_parent_center,x_center,y_center = self.get_center_position(value[0],value[1],'right')
                    # create line
                    if self.findDepth(node) == 1:
                        x_center = x_center + 200
                    elif self.findDepth(node) == 2:
                        x_center = x_center + 100
                    elif self.findDepth(node) == 3:
                        x_center = x_center + 50

                    self.create_line(x_parent_center, y_parent_center, x_center, y_center, "line_" + str(iterator.right.data))
                    # create circle
                    self.create_circle_center_position(x_center, y_center, diameter, fontSize, iterator.right.data, "tag_" + str(iterator.right.data))
                    break
                elif iterator.data > node.data and iterator.left is None:
                    iterator.left = node
                    value = self.canvas.bbox("tag_"+str(iterator.data))

                    x_parent_center, y_parent_center, x_center, y_center = self.get_center_position(value[0], value[1],
                                                                                               'left')
                    if self.findDepth(node) == 1:
                        x_center = x_center - 200
                    elif self.findDepth(node) == 2:
                        x_center = x_center - 100
                    elif self.findDepth(node) == 3:
                        x_center = x_center - 50
                    self.create_line(x_parent_center, y_parent_center, x_center, y_center, "line_" + str(iterator.left.data))
                    self.create_circle_center_position(x_center, y_center, diameter, fontSize, iterator.left.data,
                                                  "tag_" + str(iterator.left.data))
                    break

                if iterator.data < node.data:
                    iterator = iterator.right

                else:
                    iterator = iterator.left


    def find_node(self, num):
        iterator = self.root
        while iterator is not None:
            if iterator.data == num:
                return iterator

            if iterator.data < num:
                iterator = iterator.right

            elif iterator.data > num:
                iterator = iterator.left

        return None

    def find_parent(self, num):

        node = self.find_node(num)
        iterator = self.root
        parent = None
        while iterator != node:
            parent = iterator
            if iterator.data > node.data:
                iterator = iterator.left
            else:
                iterator = iterator.right
        return parent

    def find_successor(self, num):

        node = self.find_node(num)
        iterator = node.right
        while iterator is not None:
            if iterator.left is not None:
                iterator = iterator.left
            else:
                return iterator

        return


    def delete_node(self,num):

        if self.find_node(num) is None:
            return "No Record Found"
        else:
            delete_node = self.find_node(num)
            parent = self.find_parent(num)

        # delete node whose either side is null
        succesor_list = []
        if delete_node.left is None or delete_node.right is None:
            if parent.left == delete_node:
                succesor_list = self.clear_succesor_node_canvas(delete_node)
                parent.left = None

            elif parent.right == delete_node:
                succesor_list = self.clear_succesor_node_canvas(delete_node)
                parent.right = None

        else:
            succesor = self.find_successor(num)
            succesor_parent = self.find_parent(succesor.data)
            if delete_node.right == succesor:
                succesor.left = delete_node.left
                if parent.right == delete_node:
                    parent.right = None
                else:
                    parent.left = None
                self.clear_succesor_node_canvas(delete_node)
                succesor_list = self.get_list_by_levelorder(succesor)
            else:
                self.clear_succesor_node_canvas(delete_node)
                succesor_parent.left = succesor.right
                succesor.right = delete_node.right
                succesor.left = delete_node.left

                if parent.right == delete_node:
                    parent.right = None
                else:
                    parent.left = None

                succesor_list = self.get_list_by_levelorder(succesor)

        print(succesor_list)
        for num in succesor_list:
            self.addNode(num)

        self.printTree(self.root)

    def clear_succesor_node_canvas(self, node):

        if node is None:
            return None

        queue = []
        traversal = []
        queue.insert(0, node)
        while len(queue) > 0:
            traversal.append(queue[-1].data)
            node = queue.pop()
            # delete images from canvase ###
            self.canvas.delete("tag_"+ str(node.data))
            self.canvas.delete("num_" + str(node.data))
            self.canvas.delete("line_"+str(node.data))
            ###
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # first Node is delete None, it is not needed to returned
        return traversal[1:]


    def get_list_by_levelorder(self,node):

        if node is None:
            return None

        queue = []
        traversal = []
        queue.insert(0, node)
        while len(queue) > 0:
            traversal.append(queue[-1].data)
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return traversal

    def clear(self):
        self.root = None

    def printTree(self, tRoot):
        if tRoot is not None:
            self.printTree(tRoot.left)
            print(str(tRoot.data) + " ")
            self.printTree(tRoot.right)

    def findDepth(self,node):

        iterator = self.root
        depth = 0
        while iterator is not None:
            if iterator == node:
                return depth
            elif iterator.data < node.data:
                iterator = iterator.right
            elif iterator.data > node.data:
                iterator = iterator.left
            depth +=1
        return None

    def create_circle_center_position(self,x, y, diameter, fontsize, num, tag):

        radius = diameter / 2
        x0 = x - radius
        y0 = y + radius
        x1 = x + radius
        y1 = y - radius
        circle = self.canvas.create_oval(x0, y0, x1, y1, fill="lightgreen", tag=tag)
        circle_position = self.canvas.coords(circle)
        circle_radius_x = (circle_position[2] - circle_position[0]) / 2
        circle_radius_y = (circle_position[3] - circle_position[1]) / 2
        circle_ceter_x = (circle_position[0] + circle_radius_x)
        circle_center_y = (circle_position[1] + circle_radius_y)
        textid = self.canvas.create_text(circle_ceter_x, circle_center_y, font=("Purisa", fontsize), text=num,
                                    tag="num_" + str(num))

    def create_line(self,start_x, start_y, end_x, end_y, tag):
        start_x = start_x
        start_y = start_y + radius
        end_x = end_x
        end_y = end_y - radius
        self.canvas.create_line(start_x, start_y, end_x, end_y, width=3, tag=tag)

    def get_center_position(self,parent_x0, parent_y0, direction):

        x_parent_center = parent_x0 + radius
        y_parent_center = parent_y0 + radius
        x_center = parent_x0 + radius + 150
        y_center = parent_y0 + radius + 150
        if direction == 'left':
            x_center = parent_x0 + radius - 150

        return (x_parent_center, y_parent_center, x_center, y_center)