Containerized Applications: Docker
==================================

Containerized applications
--------------------------

Containers are software units that allow multiple applications to run on a single host without interfering with one another. Containers provide the flexibility to move applications between different environments and are secure because each application runs in its own isolated environment.

Containerized applications are faster and easier to deploy and run than virtual machines, especially at scale. They have become the standard way to package and deploy many applications. To learn more about containerized applications, read more [here](https://www.docker.com/resources/what-container/) and [here](https://www.datadoghq.com/knowledge-center/containerized-applications/).

An example of using off-the-shelf applications is the popular WordPress blog engine. WordPress requires a database, such as MySQL, and a web server, such as Apache or Nginx. Each one runs in its own container and communicates with the others as necessary. To read more about an example of this, read more [here](https://www.digitalocean.com/community/tutorials/how-to-install-wordpress-with-docker-compose).

Many companies develop in-house applications using a microservice-based architecture. A single application may have anywhere from a handful to dozens or hundreds of microservices, each packaged in its own container and possibly requiring other dependencies.

When you build a container image, you need to include any support files, such as libraries and data files, before uploading it to a registry. Afterward, servers fetch the container images and run them to provide the container with the resources it asks for. These resources may include storage, network access, memory, and direct access to hardware.

Most containers expose one or more network ports to connect to the application. For example, a web application might expose the HTTP or HTTPS port.

Some containers are also designed to work with other containers. For example, a web application might need a database to store data. Containers can be set up to discover and connect with each other, even if they are not publicly accessible. This is called “container networking.”

For example, you can use the time-tracking app Kimai, which runs in a Docker container on your computer and exposes a web interface on port 8080. It also requires a MySQL database, which runs in another container alongside Kimai. The MySQL container exposes port 3306 to Kimai. After you start both containers, you can go to <http://localhost:8080> in your browser and record your time.

When to use (or not use) Docker
-------------------------------

Docker is a containerization platform that bundles applications and their dependencies into portable containers, which simplifies deployment and ensures consistent performance across environments.

You should  use Docker when:

* The application you want to run has already been packaged as containers, or

* You are developing a complex application across multiple teams, such as a microservice-based app, or

* You're running an application at internet scale across hundreds or thousands of servers.

You _may not_ want to use Docker when:

* You’re planning to use Kubernetes, which now prefers new container engines like containerd, or

* You are running a huge, monolithic legacy application written in something like Java.

Note: Traditionally, it was advised not to use Docker or Kubernetes to run performance-sensitive applications, but that no longer holds true in 2023.

### Docker walk-through

To learn how to build and deploy distributed applications to the cloud with Docker, follow these [instructions](https://docker-curriculum.com/) and use the [Docker sandbox environment](https://www.docker.com/101-tutorial/) to practice.

### Docker alternatives

All these alternatives use Linux kernel core technology to provide container management capabilities. You'll also encounter projects such as Kubernetes and Docker Swarm. The tools make large-scale deployments easier for you by adding a layer of management on top of containers.

To learn more about Docker alternatives, read more [here](https://jfrog.com/devops-tools/article/alternatives-to-docker/#runc) and [here](https://kodekloud.com/blog/docker-vs-containerd/).

Key takeaways
-------------

As an IT professional, it is important to become familiar with Docker because it's a tool you'll use to develop, move, and run software across different systems. Learning how to use Docker and perhaps some Docker alternatives will enable you to more efficiently manage software, making your future life easier!
