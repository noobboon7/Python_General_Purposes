# NOTES

## course intro

### cloud services overview

* Cloud services are hosted on remote servers that can be accessed over the internet.
* Cloud providers offer different service types, including:
* Software as a Service (SaaS): Pre-packaged software applications.
* Platform as a Service (PaaS): Pre-configured platforms for developing and deploying applications.
* Infrastructure as a Service (IaaS): Bare-bones computing resources, such as virtual machines.
* When setting up Cloud resources, consider regions and zones for optimal performance and data storage compliance.
* Qwiklabs uses Infrastructure as a Service (IaaS) to provision virtual machines with operating systems and additional software.

### Scaling in the Cloud

* Cloud providers offer a lot of available capacity that can be used by their customers.
* When we choose to host our infrastructure in the Cloud, we're purchasing and using some of the provider's capacity to supplement or completely replace our on-premise capacity.
* This lets us easily scale our service to satisfy demand.
* There are a couple of different ways that we can scale our service in the Cloud, horizontally and vertically.
* To scale a deployment horizontally, we add more nodes into the pool that's part of a specific service.
* To scale a deployment vertically, it means you're making your nodes bigger.
* When talking about scaling in the Cloud, another aspect we need to take into account is whether the scaling is done automatically or manually.
* When we set our service to use automatic scaling, we're using a service offered by the Cloud provider.
* This service uses metrics to automatically increase or decrease the capacity of the system.
* Using manual scaling means that changes are controlled by humans instead of software.

### Evaluating the cloud

* Cloud computing involves giving up some control to a cloud provider in exchange for benefits such as not having to worry about maintaining hardware and software.
* There are different levels of control depending on the service model chosen: software as a service (SaaS), platform as a service (PaaS), or infrastructure as a service (IaaS).
* When choosing a cloud provider, it's important to consider the level of support available and the security measures in place.
* Cloud users also have a responsibility to follow reasonable security practices.
* Migrating to the cloud can be a big project, but it can also be beneficial.

### Migrating to the cloud

#### Cloud Migration

Migrating to the cloud involves trade-offs between control and maintenance. Infrastructure as a Service (IaaS) provides more control over infrastructure design, while Platform as a Service (PaaS) reduces management responsibilities.

#### Lift and Shift Strategy

In a lift and shift strategy, physical servers are migrated to virtual machines in the cloud, maintaining the same core configurations. This simplifies migration but requires ongoing application management.

#### Containers

Containers package applications with their configurations and dependencies, allowing them to run consistently across different environments. This simplifies migration between platforms.

#### Cloud Types

**Public Cloud**: Cloud services provided by third parties.
**Private Cloud**: Cloud services owned and managed by a single organization.
**Hybrid Cloud**: A combination of public and private clouds.
**Multi-Cloud**: A combination of public and/or private clouds from multiple vendors.

#### Benefits of Multi-Cloud

Multi-cloud deployments provide redundancy and protection against vendor outages.

## Managing instances in the cloud

### Spinning up VMs in the cloud

* Cloud providers offer a console to manage services, including infrastructure-as-a-service.
* When creating a VM in the Cloud, you need to set parameters such as name, region, zone, machine type, CPU, memory, and boot disk.
* The web UI can be used to inspect parameters and compare options, while the command line interface allows for automation.
* Reference images and templating can be used to automate the preparation of VM contents.
* A disk image is a snapshot of a VM's disk at a given point in time.
* Good templating software lets you copy an entire VM and use that copy to generate new ones.

## Automating Cloud Deployments

### Cloud scale deployments

* **Load balancers** ensure that each node in a service receives a balanced number of requests.
* **Autoscaling** allows a service to increase or reduce capacity as needed, while only paying for the cost of the machines that are in use at any given time.
* **Data persistence** is important for services that need to store data, and can be achieved by connecting the service to a database.
* **Caching** can improve the performance of a service by storing frequently requested content in memory.
* **Cloud providers** offer a variety of capabilities to help you manage your services, including automatic scaling, load balancing, and caching.

### What is orchestration

* **Automation** replaces manual steps with automatic ones.
* **Orchestration** automates the configuration and coordination of complex IT systems and services.
* Orchestration tools use APIs to interact with Cloud infrastructure directly from scripts.
* Orchestration can be used to automate complex setups, such as hybrid Cloud setups.
* Orchestration tools can also be used to set up monitoring and alerting systems.

### Cloud Infrastructure as Code

* **Infrastructure as Code** is a way to store and manage infrastructure in a code-like format, using version control to keep track of changes.
* **Cloud Orchestration** is the process of managing and automating the deployment and configuration of cloud resources.
* **Terraform** is a popular tool for cloud orchestration that uses its own domain-specific language to specify the desired cloud infrastructure.
* **Long-lived instances** are typically servers that are not expected to go away and are updated using a configuration management system like Puppet.
* **Short-lived instances** come and go very quickly and are updated by replacing the old instances with new ones.

## Software on the cloud

### Storing Data in the Cloud

* Cloud providers offer a variety of storage options, including block storage, shared file systems, and object storage.
* Block storage is similar to physical hard drives and is used for persistent storage.
* Shared file systems allow multiple instances to access the same file system.
* Object storage is used for storing application data and is accessed through an API.
* Cloud providers also offer databases as a service, including SQL and NoSQL databases.
* When choosing a storage solution, you need to consider factors such as the amount of data, the type of data, the geographical locations, the frequency of access, and the budget.
* Cloud providers offer different storage classes with different performance characteristics and prices.
* Hot data is accessed frequently and stored in hot storage, while cold data is accessed infrequently and stored in cold storage.

### Load balancing

* Load balancing is a technique for distributing requests across multiple servers or containers.
* **Round-robin DNS** is a simple load balancing method that distributes requests in a round-robin fashion.
* **Dedicated load balancers** provide more control over load distribution and can be configured to check the health of backend servers.
* **Sticky sessions** ensure that all requests from the same client go to the same backend server.
* **GeoDNS** and **geoIP** can be used to direct clients to the closest geographical load balancer.
* **Content delivery networks (CDNs)** cache content close to the end user to improve performance.

### Change Management

* **Change management** is a process that helps you make changes to your cloud service in a controlled and safe way.
* **Continuous integration (CI)** is a system that builds and tests your code every time there's a change.
* **Continuous deployment (CD)** is a system that automatically deploys the results of a build or build artifacts.
* **A/B testing** is a technique that lets you test different versions of your service with real users.
* **Post-mortems** are a process that helps you learn from failures and improve your change management systems.

### Understanding Limitations

#### Problems You Might Encounter When Deploying to the Cloud

* Instances might be added or removed from the pool as needed.
* If an individual machine crashes, your service needs to continue running without introducing problems.
* Not every problem results in a crash.
* Sometimes you run into quotas or limits.
* Some API calls used in Cloud services can be expensive to perform.
* There are also utilization limits, which cap the total amount of a certain resource that you can provision.
* If your service performs expensive operations routinely, you should make sure you understand the limitations of the solution that you choose.
* When your service depends on a Platform as a Service offering like a hosted database or CICD system, you're handing the responsibility for maintenance and upgrades of that service off to your Cloud provider.

#### Tips for Avoiding Problems

* Keep in mind how your application will be deployed when writing software to run on the Cloud.
* Make sure your software is fault tolerant and capable of handling unexpected events.
* Monitor your service for problems.
* Set up alerts to notify you when problems occur.
* Understand the limitations of the Cloud services that you're using.
* Work with your Cloud provider to resolve problems.
