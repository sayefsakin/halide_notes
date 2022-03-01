Traveler Features
---------------------------


Available Views
- Gantt View
- Utilization View
- Selection Info View
- Code View

- Functional Box Plot
- Line Chart View

- Interval Histogram
- Task Dependency Tree
- Aggregated Gantt



This is an introduction of the Travlere interface. Traveler is hosted at this link https://traveler-integrated.herokuapp.com/. Traveler is an integrated visualization system for asynchronous multitask execution. Here at the bottom right, you can see a Phylan program written in python which executes a basic linear algebra function called dgemm with these parameters. This program uses 16 threads to execute the dgemm function.

Here at the top left is the utilization view, which shows among the 16 CPU threads, how much are being utilized at a time. The x axis here represents time in nanoseconds. At the bottom left is the gantt View. Similarly here at x-axis is time and y-axis represents CPU core and threads. The gantt view shows a task execution as an interval using a rectangle. For example this box represents a task execution at thread location 11 started at this time and ended at this time.

Its possible to zoom in and zoom out by scrolling in the gantt view. If you start scrolling in the y-axis it will zoom vertically over the CPU core locations. You can also click and drag horizontally.

Here, at the utilization view, you can click and drag a brush to highllight a specific time and the gantt view will update accordingly. Its also possible to click and drag this brash in the utilization view.

At the top-right is the Information view. It is showing all the related information of the excution. Clicking on an interval bar in the gantt view will highllight that interval bar in the gannt view and its utilzation in the utilization view. You can also see its relevant information in the selection info view. Here, in the gantt view, the yellow lines represents parent-child dependency. For example the task 'halide_hpx_for' is initiated by this task /phylanx$0/variable$0$alpha/0$12$4. Its possible to follow along the parent and show its other dependencies.

Traveler also has other types of views, if you click on this hamburger menu, it will show you all the available views. Here, you can see that, we have PAPI counters. If I click on PAPI_TOT_CYC, you can see another new view here at the bottom left. It is showing PAPI metric data total CPU cycle as a rate. It is represented as a functional box plots view, where the top line represents the maximum value, the bottom one the minimum, and the middle one the average. The shaed gray area around the average line is the 1 standard deviation. You can also see it has other types of metrics like CPU IDLE %. Here, you can also zoom in/out and drag to pan and it is also linked with the gantt and utilization view.

Lets see the interval histogram view. It is showing how many intervals are there of a specific duration or length. The y axis shows the count and x-axis is the durations. It is possible to click and drag a brush in this view and it will highlight all the inerval bars ranging of these duration in the gantt view and the utilization view. With this , it is possible to find out the longest interval bars, as well as the shortes ones also.

Then, there is the Task Dependency Tree. Clicking on it will bring two interfaces. Here at the bottom-right is task dependecy tree. As a reminder, There could be dependency between these tasks, like a function calls to another function and we could instrument a parent child relationship between these tasks with yellow lines like this. the Task Dependency Tree basically shows this parent-child relationship as a tree and makes it much more easier to navigate through each task. Now, if we aggregate tasks by the subtree rooted at an specific node we could visualized that using an ancillary aggregated gantt view here at the bottom-left. Here, It shows a single aggregated rectangle to represent all such dependent tasks which gets aggregated by the subtree. If you click on differnent node in the task dependecy tree, it will show the aggregated tasks here in the aggregated gantt view, also highlight the related interval bars in the gantt view and update highlighting in the utilization view.

