More about preventing future breakage
=====================================

Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying, isolating, and managing _problem domains_ and _failure domains_.

Problem domains
---------------

Problem domains  describe the complexity of a given problem that one is trying to solve. Let’s look at an example below:

Let’s say you’re counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is an indexing problem. And its problem domain is fairly limited in scope. It’s a single word and a single play. A bit of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.

However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger. Any software solution used to try and solve this indexing problem has to handle various logic that it did not have to handle before, like consolidating word occurrences in various plays. For example, the word 'Brevity' may occur at least once in Hamlet, and multiple times in various other plays. Managing these multiple occurrences of 'Brevity' across Shakespeare's works significantly increases the complexity when describing the problem domain. A bit of BASH could solve this problem, but it might be difficult.

If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word, then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across multiple works of Shakespeare is even MORE complex.

So why is any of this useful? Well, if you can easily describe and reason about a problem in a lot of detail, you understand the problem domain fairly well. Producing a software solution for a given problem becomes easier when you understand the problem domain fairly well. Of course, building a good understanding of the problem domain often requires a lot of experimentation and iteration. This is why it’s good to make a few initial attempts at testing a design before building an entire production system to solve a problem like indexing Shakespeare.

Failure domains
---------------

Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the various problems a system tries to solve, failure domains describe various sub-systems that may fail.

Think of your system architecture like a car. Each critical component or subsystem of the car has its own trouble spot. Take the brakes and engines of a car for example. When the brake system fails, the car can't stop effectively, making it unsafe and essentially useless. Similarly, if the engine fails, the car won't start or move, which is essentially a complete breakdown.

Using the Shakespeare example again, if one of your systems is responsible for managing the full text of the works of Shakespeare (a content server), that might represent a single failure domain. If another system is responsible for actually searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a content server fails, the indexer will probably also fail.

So why do you care about any of this? Well, problem domains drive system complexity. Complex systems often have many failure domains. The key to preventing future breakage is to identify, and manage the scope and severity of a failure domain. This may mean redesigning the system in a way that has many smaller failure domains, instead of few large ones.

As another example It’s better to have a video streaming service slow down instead of failing entirely. This kind of graceful degradation can be attributed to isolated failure domains.

It's essential to understand failure domains when working with complex systems. The concept of failure domains is similar to the concept of problem domains because they define specific subsystems within a larger structure that are capable of malfunctioning without causing a systemic breakdown. By recognizing and managing these domains effectively, you can proactively design systems with self-contained failure compartments, ensuring resilience and graceful deterioration in the event of disturbances. Building reliable systems that navigate modern technological environments requires effective failure domain management.

To learn more about failure domains, read more [here](https://deploy.equinix.com/blog/explaining-failure-domains-sre-lifeblood/).

Programming problem solving
---------------------------

It's essential to approach programming problems methodically. Before coding, it's critical to fully comprehend the issue. Rushing into coding can be counterproductive. To gain a deeper understanding of the problem’s logic and nuances, you’ll want to review the prerequisites and restrictions. You’ll also want to consider solving the problem manually using illustrative data sets. When you have manually solved the problem, it’s important to refine it by adding comments and pseudocode before coding it. This will act as a blueprint to ensure your code adheres to the logical solution as you write it. When you're done coding, you'll want to optimize your code.

To learn more about using a methodical approach when tackling programming problems, read more [here](https://www.freecodecamp.org/news/how-to-solve-coding-problems/#:~:text=review%20them%20here%3A-,Step%201%3A%20understand%20the%20problem.,if%20it%20could%20be%20better.).

Effective troubleshooting
-------------------------

When troubleshooting distributed systems, it's important to look beyond logical behavior. It takes well-established methods and a deep understanding of system behavior to troubleshoot effectively. Making observations, formulating hypotheses, and then systematically testing those hypotheses are all steps in the hypothetico-deductive method. It's crucial to avoid common pitfalls, such as fixating on unrelated symptoms or confusing correlation with causation. As you transition from theoretical concepts to practical implementation, using metrics, logs, and tracing exposes the subtle intricacies of the system's behavior. With defined strategies, well-informed diagnostic tools, and a thorough understanding of system dynamics, troubleshooting becomes a structured process supported by clear strategies.

To learn more about using a systematic approach to troubleshooting effectively in distributed computing environments, read more [here](https://sre.google/sre-book/effective-troubleshooting/).

Mark as completedGo to next item
