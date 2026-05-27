Starting with this chapter, we're going to focus on how we can store and organize data in a way that allows for even better algorithms.

Data structures are just organizational tools that allow for more advanced algorithms. Some examples:

    Stacks: Last in, first out.
    Queues: First in, first out.
    Linked Lists: A chain of nodes, efficient for inserts and deletes.
    Binary Trees: A tree where each node has up to two children.
    Red Black Trees: A self-balancing binary tree using colors.
    Hashmaps: A data structure that maps keys to values.
    Tries: A tree used for storing and searching words efficiently.
    Graphs: A collection of nodes connected by edges.

A data structure is a data organization, management, and storage format that enables efficient access and modification. More precisely, a data structure is a collection of data values, the relationships among them, and the functions or operations that can be applied to the data.


def count_marketers(job_titles):
    count = 0
    for job in job_titles:
        if job.lower() == "marketer":
            count += 1

    return count
