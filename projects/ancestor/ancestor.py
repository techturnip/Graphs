from util import Queue


def earliest_ancestor(ancestors, starting_node):

    # queue of current nodes
    q = Queue()

    # add first node to path
    path = [starting_node]

    q.enqueue(path)

    while q.size() > 0:
        current_path = q.dequeue()

        new_path = []
        changed = False

        for node in current_path:
            for ancestor in ancestors:
                if ancestor[1] == node:
                    new_path.append(ancestor[0])
                    changed = True
                    q.enqueue(new_path)

        if changed is False:
            if current_path[0] == starting_node:
                print(f'Node: {starting_node}')
                print("No ancestor\n")
                return -1
            else:
                print(f'Node: {starting_node}')
                print(f'Earliest ancestor: {current_path[0]}\n')
                return current_path[0]
