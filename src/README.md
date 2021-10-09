This is a private repository owned by Prajjaval Singh

Program Organization
All the code is in the M01-P02-Source-Code.zip file

 

User.py: This file implements UserInfo and UserData classes. UserInfo has a user id field and UserData data including email and password. These are mainly to create the data to be stored in the data store

 

InfoGenerator.py: InfoGenerator class implements utility methods for generating various random data including:
generate_user_id - Creates monotonically increasing user id using a class method
generate_email and generate_password - Static methods for generating random but structured strings for email and password data
generate_node_name - Static method for generating random node name including timestamp to further avoid any chance of name clashes

 

VirtualNodeMap.py: VirtualNodeMap class implements and stores vnode-to-node name mapping. It値l be composed inside of the Node class. It supports creation of random but balanced vnode-node mapping and provides fetching the node for a given vnode or a given key. Keys are mapped to virtual nodes by a simple modulo based mapping.

Node.py: Node class implements the main logic in the data store. Multiple Node instances work together as an example distributed data store.

get_data and set_data: These methods provide retrieval and insert/update in the data store. Ultimately, they are supposed to handle any key query and internally get the data from the appropriate node. A normal client should be able to interact with any node about any key, without the need to understand or know about key ownership.

add_new_node: This method is called in each existing node when a new node is created. It値l reassign a proportional quantity of virtual nodes from itself to the new node. It値l then prepare for the transfer of the relevant keys and accomplish the actual transfer using transfer_keys method

remove_current_node: This method is called on the node selected for removal in a planned scenario while down-scaling. It値l take all of its virtual nodes and proportionately reassign them to all other remaining nodes. It値l then prepare for the transfer of the keys and accomplish the actual transfer using transfer_keys method

transfer_keys: This function takes keys to be transferred, grouped by the virtual nodes. It goes through all of them, transferring each block and reassigning the virtual node to the new mapped node.
 

data_store.py: This is the main driver program. In order, it:
Creates a node first and creates a random VirtualNodeMap inside it
 

Creates other initial set of nodes, with the same virtual node mapping and connects them with each other
Takes appropriate actions to add a new node
Takes appropriate actions to remove an existing node
Demonstrates the state of all available nodes and also shows data interaction on random user ids, after each major step.

Problem Statement
The program structure is already set and there are specific methods that you are expected to implement. Please also read the comments in the code, especially in the methods to be implemented. Please leave data_store.py as it is. You can copy it to a different file and modify that for your testing and demonstration purposes as you see fit.

 

(Medium) Implement the populate_map method in VirtualNodeMap class.

You are supposed to create a random mapping (dictionary) of virtual node numbers (0 to (TOTAL_VIRTUAL_NODES - 1)) mapped to node names.

Each node should get equal distribution of virtual nodes. However, given the maths, it might not be always exactly possible so slight variations are fine, for example, distributing 200 virtual nodes among 6 nodes would mean that 2 nodes would get an extra virtual node. Please ensure that exactly TOTAL_VIRTUAL_NODES count of virtual nodes are there in the mapping.

(Medium) Implement get_data and set_data in the Node class
2a. get_data: As you can see, it currently just looks up in its local data store and tries to return the value. This would, of course, fail for keys owned by other nodes.
Enhance this method to fetch from local or sibling nodes based on node assignment of the key and return the data to the user. You can assume local ownership if the key exists in the local store.

2b. set_data: Firstly, as specified in the function, data will always be set in the current node if the force flag is True. Aside from that, the method is still setting the data in the local data store.

When the force flag is not True, enhance this method to find the node owner based on node assignment of the key. Then set the data locally or call a sibling set_data method accordingly.

(Hard) Implement gaps specified in add_new_node
3a. At the specified place (see comments in the method), find the list of all virtual nodes mapped to this node, store them in the specified variable and shuffle them

3b. At the specified place (see comments in the method), loop over all local keys and create the appropriate structure that can be ingested by transfer_keys. Please ensure to only consider keys mapped to virtual nodes in the local_vnode_slice as we値l be transferring only a few virtual nodes to a new node.

(Hard) Implement gaps specified in remove_current_node
4a. At the specified place (see comments in method), find the list of all virtual nodes mapped to this node, store them in the specified variable and shuffle them

4b. At the specified place (see comments in the method), loop over all local keys and create the appropriate structure that can be ingested by transfer_keys. Please ensure to correctly mark the appropriate target node based on the new mapping created in transfer_node_mapping


Evaluation Rubric
Total Project Points: 240
Basic compilation without errors (10%) : 24 Points
Correctness:
Problem statement - 1    (30%) : 72 Points
Problem statement - 2.a (15%) : 36 Points
Problem statement - 2.b (15%) : 36 Points
 

Problem statement - 3.a (5%) : 12 Points
Problem statement - 3.b (10%) : 24 Points
Problem statement - 4.a (5%) : 12 Points
Problem statement - 4.b (10%) : 24 Points
 

 

Program Instructions
1. Download the zipped folder named M01-P02-Source-Code.zip, and unzip it on your local machine. Go into the directory named src

2. Make sure that you have Python 3.6, or higher, installed. At your command prompt, run:

$ python --version
Python 3.7.3
If not installed, install the latest available version of Python 3.

3.To run the code in the source code folder, run the following command:

$ python3 data_store.py (On many Linux/Mac platforms)
OR
$ python data_store.py (On Windows/Mac platforms)

In any case, one of these two commands should work.

4. Alternatively, you could install a popular Python IDE, such as PyCharm or Visual Studio Code, and select a command to build the project from there.

Note
Minimum Requirements: The final submission that you upload needs to have a successful compilation, at the least.
Since the program given to you as part of the problem statement is incomplete, it is quite possible that it may not compile or run successfully, as-is. 
The client code is already present in the data_store.py file. That will print the output in an acceptable format. This code in data_store.py is complete, but for it to work, you need to fill up the gaps.
The way to go is to comment out all the code in data_store.py. Then, as you complete the code in other files to fulfil the functionality for parts 1, 2, 3, and 4 of the problem statement - un-comment the code in data_store.py to see if the implemented functionality works. Basically, go step by step. That way, you can  verify if each step of implementation is working.
If you do not attempt any part(s) of the problem statement, make sure that the entire program still gives successful compilation. For this, make sure that the unimplemented parts (in various parts), and the related client code within data_store.py, are commented out as necessary. This is to ensure that the implemented parts compile and run as you desire.
Program Output Format:
Specifically for Step 1, there is a need to verify that the VirtualNodeMap inside the Nodes is correctly populated. Since this verification is not present in the client code, you will need to add it.
Since the virtual node map is essentially a dictionary, you can print out the dictionary to demonstrate its contents.
Since the output is likely to be large, we recommend you print this dictionary out into an output file (by using the standard Python File I/O module API). 
You could achieve this output redirection by a command such as:
python data_store.py > vnode_map.txt
Or (refer to the instructions above)

python3 data_store.py > vnode_map.txt
For Steps 2, 3, and 4, the client code is already present within data_store.py. You can use a suitable strategy, as listed above. 
References
Please refer to the relevant consistent hashing video and notebook content from the course material
Consistent Hashing - https://www.youtube.com/watch?v=SAGxMODAlEg
Random Module - https://www.youtube.com/watch?v=pt3k8pc8f0A
Class and Static methods - https://www.youtube.com/watch?v=rq8cL2XMM5M
Class and Static methods - https://realpython.com/instance-class-and-static-methods-demystified/
There are some python libraries and concepts used which might be new to some of you
list(dict_obj.keys()) - By default, keys function returns a dict_key object. Explicitly converting it to a list is necessary to use it for normal list behaviour.
math.floor(x), math.ceil(x), and round(x) functions respectively provide the integer value just lower than x, the integer value just higher than x, and integer value based on normal rounding rules applied to x.
Multiplying a list with a number, replicates the list internally. for example:
a = [1,2,3]
b = a * 3
print(b)
Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]
random.shuffle(list_obj) on a list will randomly sort the list_obj similar to shuffling a deck of cards. This is extremely handy to generate a randomized list or ordering.
random.choices in combination with the string class allows generation of random strings from a specific character set, for example:
foo = ''.join(random.choices(string.ascii_uppercase, k=10))
print(foo)
Output: PSBYZSHXWN
A ten-digit uppercase-only randomly generated string
zip function combines two different equally sized lists together in different ways. Using dict along with zip can cleanly create a dict from two lists, for example:
a = [1, 2]
b = [3, 4]
dict(zip(a,b))
Output: {1: 3, 2: 4}
Elements from a are taken as keys and from b are taken as values
iter function creates an iterator object on any list. Calling next function on that iterator will give the list elements one-by-one in sequence, for example:
a = [1,2,3,4]
a_iter = iter(a)
next(a_iter)
Output: 1
next(a_iter)   
Output: 2
