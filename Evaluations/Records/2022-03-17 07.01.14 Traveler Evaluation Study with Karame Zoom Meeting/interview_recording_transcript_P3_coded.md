interviewer: could you please go to the link I provided you in the chat and load it in your browser	and could you please also share your screen so that we can also see how you are interacting with the interface? 
P3: (P3 share her screen) can you see that?
interviewer: yeah. thank you. so now just take couple of minutes and explore the dataset by your own. so, here um, I think, do you have any other browser other than mozilla firefox? This, um, Traveler runs best in chrome, so if you have chrome then, yeah, **trials: E1**
P3: yes I have but I dont use it. just a second. 
interviewer: or you can use the default, what it is called, if you have microsoft edge you can also use that. I think yeah Traveler also runs smoothly on that also.
P3: I think it should be fine now, let me share, (P3 again shared her screen)
interviewer: ok, **threats: light mode, browser compatibilty**
P3: do I have all the axes like you showed me before (the gantt view didnt' show anything at first, but when she move the vertical slider, the interval bars appeared)
interviewer: so let me give a short introduction about this dataset. so this is a kmeans dataset, so basically this program is actually running the kmeans algorithm and then yeah it also uses 16 CPU threads to run this program. you can then now, you can now explore this dataset on your own and see whats happening with the dataset. 
observer: and you can get all the other windows through the hamburger menu at the purple one. 
P3: (brings the functional box plot view), becuase its um, its not colorful its not very easy to follow, so this is black and white, (brings the interval histogram view, and then the task dependency view, start exploring the tree, brings the line chart view) All of these tabs are working? **comment: hard to follow in light mode**
interviewer: yeah so, the tabs with the tick sign they are being visualized here, yeah.
P3: and all these primitives are (pointing to the nodes in the tree) kind of related to each other right? 
interviewer: yeah,
P3: so is it possible you add anything else to this tool?
interview: uh you mean?
P3: completely something independent to these primittives, just to see all the I mean everything about that specific job or that specific tasks.
interviewer: ok so, if you click on a specific node in here, then you can see that, the related information in the selection info view, ok. the selection info view is at the top right. so if you click on a specific node in here, then you can see the related information here.
P3: my question was just uh, adding something new to this primitives.
observer: I dont understand, what do you mean by adding something new?
P3: you see you are just now you are actually watching everything about all these specific primitives you added right, like the task that you added, imagine we have something that we want to see everything about it the memory, the cache function everything, so is it possible to add something a new task, to that just to see whats going on like we have an HPX like algorithm, we want to see what is happening there?
observer: I think what you are suggesting would have to happen during data collection, so this is you run your program and HPX tells APEX  which is what actually collecting it, the counters, and APEX instruments everything, and records the trace, and then post mortem we are looking at this, nothing is running right now, we just have the data from one something did run, 
P3: so you can add any data to that?
observer: you could add the data by rerunning the program collecing it, but we cant add data throught this interface. 
P3: okay. hmm. (tried to click on the OPEN VIEW then realized just over works, clicking on it would disappear it, she bring back the gantt view, explored a little bit and then closed the dependency tree view and the interval histogram view, clicked on the menu again, tried clicking on PAPI which disappeared the menu, then bring back the interval histogram view, tried to click on the bars)
interviewer: so this bars are not clickable you can click and drag the brush. 
P3: I can see the count. 
interviewer: you need to highlight them like this, yeah. you can see the releated highlighting in the utilization view, 
P3: it is loading ( pointing to the gantt view)
interviewer: yeah, the gantt timeline for the this dataset is little bit slower, 
P3: (keeps brushing over the interval and torchering the gantt timeline)
interviewer: if you feel comfortable with the dataset then I would like to move on to the next section like giving you uh, I am going to give you some task to do here. Its taking longer time. of course you can hit refresh to reload the interface to its basic form. **threats: gantt loading time with duration filter** 
P3: what is that?
interviewer: so you can if you can refresh the browser to reload the interface, just refresh the browser (P3 closed the gantt view and then refresh it). yeah so, my first task for you is, can you locate the longest interval bar here? interval bar with the longest duration. 
P3: this one (pointing to the highest CPU utilization). I cant see interval. 
interviewer: we are calling interval bars, you see the each specific rectangular bar in the gantt view, we are calliing each of them interval bar. 
P3: (seems confused about what is interval bar is, pointing to utilization and gantt bar again)  So this should be the longest one
interviewer: okay so, here, in the utilization view it is showing you the just the utilization, I mean how much CPU are getting utilized among the 16 of them. 
P3: (pointing to the gantt view intervals) so here we can see the intervals.
interviewer: yeah.
P3: so what do you want?
interviewer: interval bar with the longest duration, with the longest length. **trials: E2**
P3: (pointing to the far right in the gantt view) here.
interviewer: ok so yeah, so the thing is that, there is actually, you see that there is darker thing is going on, but these is actually are very smaller interval bars, if you start zooming-in, then you can see that they are very tiny interval bars. actually there are multiple interval bars, since they are tiny and you are in a zoomed-out state, you are seeing them as a single bar, so yeah.
P3: the color is that the darkest and lightest are very not understandable. **comment: the darkest and lightest are very not understandable, threats: light mode**
interviewer: ok you se the border of a specific bar is little bit darker, and the inside of the bar is a lighter gray. since you are in a zoomed-out state so thats why there is like many high number of smaller interval bars there . thats why you are seeing this long streak of darker shade of gray. 
P3: each of these lets say light bars here, so theres 2 colors here right, light and dark.
interviewer: since they are very small so thats why, you can see them as a darker one. if they appear to be like in a consecutive places so that becomes more darker and so on. it will help if you zoom-in, uh zoom-in using the utilization view so you can zoom in faster. then you can see that actually there is very small yeah, like this, you can see that these executions are very small and tiny. so thats why. 
P3: yeah, ok. so what is the task now? 
interviewer: so, which one is the longest one, among these bars, 
P3: these bars? among these bars?
interviewer: among the interval bars in the whole execution. **threats: understanding trails**
P3: umm, I am not sure, 
interviewer: ok so,
P3: wait we have to see the start and the end point right? to see the length?
interviewer: yeah
P3: so for example like this, this is the, this is the start and this is the end (pointing to the beginning and end of mulitple consecutive interval bars)
interviewer: no this is a, there is multiple interval bars here, you see the darkar lines represents start and end position, if you click on it, then you can see, you see, its getting highlighted with a yellow color. 
P3: ok. (clicked on an interval bar), so each of these (pointing to the non selected ones) orange bars is like, it shows the start and end point of execution. **trial E2 unsuccessful**
interviewer: yeah, exactly. ok then I am going to move on to the next task, can you locate where is the CPU utilization is very high? **trials E4**
P3: utilization? uh huh? (pointing to the correct position) here?
inerviewer: ok. yeah. also can you find the responsible primitive for that high utilization. **trials E4**
P3: say that again?
interviewer: can you find the responsible primitive? like you see there is the interval bar in the gantt view, if you click on it, you can see that the primitive which related to that interval bar, ok. so the primitives are actual the functions and code blocks in the code, ok. so I am right now asking you, which primitive causing this high CPU utilization? you see the darker area in the utilization view, that means, the shaded rectangular area, (P3 draw the brus in the utilization view), that means, yeah, right now you are, the gantt view is actually showing you that portion. right now, just find out the primitive name responsible for these executions.
P3: (scrolling a little bit in the code, then updated the brush in utilization view, then closed the selection info view) so this is that related to this change right? the page I closed. 
interviewer: the selection info view, yeah, you can also get more information if you click on the interval bar in the gantt view also. oh yeah, you can bring back the selection info view by going to OPEN VIEW then selection info the top one. ok, now so it is showing you a overall information about the whole dataset. so if you need to know the specific information about specific execution then you have to click on each interval bar in the gantt view. (P3 clicked on an interval bar) you see the information in the selection info view is getting updated. now you can find out the related information about that, 
P3: ok, so it shows all related to this part. **trials E4 unsuccessful**
interviewer: yeah, ok umm, I am going to the next portion. can you please bring, click on the hamburger menu again, and click on it, and then OPEN VIEW, and then PAPI, the bottom one, and then PAPI_L1_DCM, uh seconds yeah this one. again, can you click on the hamburger menu, then open view, and then PAPI, bottom one, and then PAPI_L2_DCM, the bottom one, yeah. you can collapse the left pane, by clicking on the collapse button in the top left. and you can also zoom-out in the maximum zoomed out state by clicking on the utilization view, or by scroll out, scroll down to zoom out yeah like this, so you can zoom out faster, if you click on the utilization view, click and select the whole execution. yeah. (P3 does so). so, now you can see the whole overview of the executions, can you now find out the relationship between the utilization and level 1 and level 2 data cache miss?
P3: can I close it and see (closing the l2 dcm chart)
interviewer: yeah, so it was PAPI_L2_DCM. 
P3: ok this one is level 2 right (pointing to the correct one)
interviewer: yeah, level 2 data cache miss.
P3: so what was your question again?
interviewer: can you find the relationship between the data cache miss and cpu utilization? **trail: E5**
P3: level 1 and level 2?
interviewer: yeah.
P3: (start dragging the brush in the utilization view from the right)  so actually its showing, what is happening to this part (pointing to the utilization view) where it is in level 2 and level 1 cache right? 
interviewer: umhmm.
P3: is that correct?
interviewer: yeah so, you can see that for a specific time, how the utilization is being changed,
P3: so this is for the same time steps, or its showing the function in to different cache misses, for example in level one, in this time step (in l1) its like this in here (in l2), so it shows that its using, its being more used here, **E5 comment**
interviewer: umhmm, yeah thats exactly right, the level 1 cache is getting, the rate is actually getting, you can see the more fluctuations is being is happening here right, its getting more used, so its being more used at that portion of the time. 
P3: so its just, at this function (pointing to far right in l2 misses) at this part, it is being more used in level one, than level 2, **E5 comment**
interviewer: compared to, yeah, exactly yeah thats right, so that was actually what I was looking for. ok so I think thats everything, so then uh, which of the views helped you mostly to perform these tasks? you see there are like couple of interfaces, which of them you think was most helpful?
P3: I think this utilization view was good and then thats graph that show the dependencies. **I1: utilization, task dependency tree**
interviewer: and do you have any preference for any specific feature here? do you like any feature most here? 
P3: uh this is very cool (pointing to the l1 and l2 misses) here, shows the like different level of cache, this is good, and uh, that feature that you can zoom in and go through all intervals you can see, uh, it all details, I think thats helpful. **I2: performance counters, zoom in-out to navigate**
interviewer: so do you have any additional proposal for any feature that we can use here?
P3: at first I was thinking, this is possible that we use because I am doing some kind of uh performance measurement for some algorithm, in HPX, so I was thinking, is that, is this possible, if we can use, because now I have a problem with those measurements, my algorithm is acting very weird in some different parts, and mostly when it gets to level cache 3, this thing is happening, so I was thinking if I can utiliz this like tool with my algorithm, to see what is going on in each level, and then I change the dataset what happens, when I chnage the input size what happens, what happens if I use different number of cores, so I could see that more in detail. so thats why I asked that question, I was thinking that its possible to use that for our algorithms or not. so yeah. **I3: ignored, asked can she used it with her own code**
observer: I was just going to say, so this actually [redacted](interviewer) its your show, so go first.
interviewer: no no I was just saying that, this actually, so the Traveler actually, actually when you run on your program, ok so then you have like collect the traces of that program using, so we are using APEX to collect the traces, so it gets us the trace in a OTF2 format, so we are just loading that OTF2 format here in traveler, so if you are able to somehow collect the traces in OTF2 format, then ofcourse we can use Traveler to visualize that, your program.
observer: so theres a few ways to compile HPX with APEX which will output this data, um specialy, if you are using Rostam, I think that theres very straightforward ways to do this, if you ask around somebody will tell you and then once you do that, there are few environment variables, where you tell it please collect level one, please collect level two, please collect level 3, and I think you can get that through HPX counters as well, but as long as you can write out this data this program can read it and this program is also open source on github, we are super interested in seeing how people use it, so if you need help please just keep contacting us and we will help you get it running, and we are happy to have some one on one sessions to help walk through how you might use it with your own code, so we understand that theres a lot going on in this, so maybe more training will be helpful, but yeah the whole point is so that uh that you and the rest of the HPX team developers have more tools.
P3: so do you have any other documentation for this? I mean actually your presentation was really good but I am interested to go more throuhg that to see.
interviewer: I just give you the github link in the chat and also I prepared a introductory document here, so yeah you can use those. 
observer: I think the introductory document is really good, because it walks you through how you might use particular things, with lots of pictures.
P3: and this I mean, I dont know , uh, if I use any other, environment, that would be different, but this I am using it not understanding at all, I mean, its very difficult to follow, 
interviewer: oh, you mean the colors, **threats: light mode**
P3: yeah, because it is, you know black and white, but the time you were talking about it, that was more made sense to me. 
interviewer: ok, so the main thing is that, the I used dark mode to visualize that thing, but in here it is in light mode, thats why, so if you have like dark mode enabled, then you can, it would be like, you can see that how it was looked in my machine.
P3: so I was thinking maybe you are just using different environment for that to show that. ok.
interviewer: so have you ever used any other performane anlaysis tools like this before? **I3: no**
P3: not really, I mean uh I just started this algorithm, like performane measurement where we got to have like step that I need to go more through that, so [redacted](runtime team leader) suggested me talk to you guys to see I mean maybe I can use that later for my algorithm or not. 
interviewer: so how long have you been working with the HPX team? **I5: few months**
P3: so I started, actually I was working with them, but I was doing something completely not related to HPX but I started uh like few months ago working on HPX.
interviewer: so I think we are almost at a time. so do you have any last comment on this?
P3: no I think, thats cool very cool tool that it can be very helpful, I mean I like that. **I6: thats cool very cool tool that it can be very helpful, I mean I like that**
interviewer: oh thanks. so I think thats all for this evaluation session. so I am concluding this evaluation session. I am going to stop the recording.