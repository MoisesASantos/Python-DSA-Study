NP-Complete

Some, but not all problems in NP are also NP-complete.

A problem in NP is also NP-complete if every other problem in NP can be reduced to it in polynomial time.
What Does “reduced” Mean?

We won't dive deep into the subject of reductions in this course, but we'll cover the basic idea.

A reducer is an algorithm that transforms some problem, Problem A, into a different problem which is already solved, Problem B. Then, Problem A can be solved with the algorithm for solving Problem B.

Problem A -> reducer -> Problem B -> solver algorithm Problem B -> solution for Problem A

However, the reducer itself needs to be fast. "Problem A is reducible to Problem B" if the reducer can run in polynomial time.
So Who Cares?

Well, this means that if we can find an algorithm that solves any of the NP-complete problems in polynomial time, then all problems in NP can also be solved in polynomial time.

Super-duper-smart computer scientists have proven it. Trust me. Or optionally read more about it if you're interested.
