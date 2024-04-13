Change management in virtualized environments
=============================================

The world we live in is evolving digitally, which makes change management in virtualized environments increasingly important. As an IT professional, you may be responsible for ensuring the stability and reliability of cloud-hosted virtual machines (VMs) within your organization. To make your future life as an IT professional easier, you'll want to familiarize yourself with managing change in virtualized environments, and how to maintain a smooth and controlled transition in cloud-based deployments.

Change management in virtualized environments refers to the structured process of altering, updating, and modifying cloud-based virtual machines. During the change process, your main priority is minimizing disruptions and ensuring system integrity. It’s important to realize that small changes to cloud environments can have significant implications due to their dynamic nature even small changes can have major implications. Therefore, it's your top priority to ensure that changes are managed in a way that protects the VM's infrastructure, overall functionality, and performance.

When working with virtual machines in cloud environments, you have two primary options for change management:

1. Using the disk snapshot feature to roll a VM back to a previous state.

2. Maintaining previous VM images and using them for rollback.

The optimal way to build and deploy virtual machines depends on the specific strategy you employ.

### Implementing change management in Google Cloud Platform (GCP)

When using the Google Cloud Platform, you'll have various tools and processes at your fingertips to facilitate change management.

If you build a custom image and boot from it, using a tool like Packer, then you can just tag your images with a version number and maintain them in the image library (so you’d have images named `MyApp-1.0, MyApp-1.1, MyApp-2.0`, etc). If there’s a problem with the latest release, you can easily roll back in GCP using these steps:

1. In the [GCP console](https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1605212&utm_content=text-ad-none-any-DEV_c-CRE_665735422256-ADGP_Hybrid%20%7C%20BKWS%20-%20MIX%20%7C%20Txt_Cloud%20Console-KWID_43700077225654735-kwd-303045185251&utm_term=KW_google%20cloud%20platform%20console-ST_google%20cloud%20platform%20console&gclid=EAIaIQobChMImNzBxbOqgQMVKyWtBh1sZQN4EAAYASAAEgIU1fD_BwE&gclsrc=aw.ds), navigate to **Compute Engine** > **Virtual machines** > **Instance templates**.

2. Select your template and then click **Create similar**. (GCP doesn’t allow you to edit a template, only create new ones.)

3. Under Boot disk, click **Change** and then select the boot image to roll back to.

4. Save the new template.

5. Navigate to **Instance groups** > **Instance groups**. Edit your MIG and set it to use the new template.

6. Click **Restart/Replace VMs**, select Replace, and then click **Restart VMs**.

GCP will replace every machine in the instance group with a new VM running the old image.

If you use standard OS images with infrastructure as code (IaC) tools like Chef or Puppet to load your applications after the VM is running, then there’s an alternative approach.

Before each deployment, use the GCP console to take a snapshot of the boot disk:

1. In the GCP console, navigate to **Compute Engine** > **Storage** > **Snapshots**.

2. Click **Create snapshot**. Give the snapshot a name and/or tags that relate to your app release (e.g. MyApp-1.0-snapshot or similar).

3. Select the disk belonging to your instance group and set other options.

4. Click **Create**.

If you need to roll back a deployment, you can create a new disk image from the snapshot and then roll back as above:

1. In the GCP console, navigate to **Compute Engine** > **Storage** > **Disks**.

2. Click **Create disk**.

3. Under the Source heading, select Snapshot and choose the snapshot you saved before the deployment.

4. Click **Create**.

5. Now use the steps above to update the instance template and instance group using the disk you just created.

To learn more about change management in Google Cloud Platform (GCP), read more [here](https://cloud.google.com/compute/docs/disks/snapshot-best-practices?authuser=1) and [here](https://cloud.google.com/compute/docs/disks/restore-snapshot).

### Common Challenges and Misconceptions

When you’re first learning how to manage change in virtualized environments, it’s likely that you’ll have to work through challenges and address misconceptions you may have. One of the major challenges you may find yourself grappling with is selecting the right change management approach. To address this and make your future life easier, it’s important to learn more about change management strategies, tools, and processes because selecting appropriate deployment strategies is critical to successful implementations.

Another challenge you may have to overcome is learning how to take snapshots correctly. It’s important to recognize that snapshots are like photographs. They’re taken at a particular instant. That means that if the VM is busy writing to the disk, the snapshot may be in an inconsistent state, which may not work correctly when restored.

To learn more about creating consistent snapshots, read more [here](https://cloud.google.com/compute/docs/disks/snapshot-best-practices).

Key takeaways
-------------

As you continue developing your understanding of change management in virtualized environments, some of the main areas you should focus on are:

* Understanding how to implement change management in virtualized environments in a controlled, structured manner to ensure system stability and reliability is maintained.

* Learning about different types of strategies and their advantages, and how to select methods of deployment strategies within the GCP.

* Learning how to use scheduled snapshots.

To make your future life as an IT professional easier, you’ll want to have a firm grasp of change management in virtualized environments. This will ensure that your strategies for deployment maintain VM stability and reliability.

To learn more about change management in virtualized environments, read more [here](https://cloud.google.com/compute/docs/disks/create-snapshots), [here](https://cloud.google.com/compute/docs/disks/scheduled-snapshots), and [here](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html).
