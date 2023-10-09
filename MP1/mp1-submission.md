<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Shashwat Singh (ss4746)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 4:51:33 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/ss4746" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T05.02.24image.png.webp?alt=media&token=a2ee35aa-c0e3-4e4f-9485-5840867dd2a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of task logic (all checklist items)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.13.09Successfull_Add_Task.png.webp?alt=media&token=29ba1cb3-37d3-492a-acfc-7b79fbf41be4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully Added Task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.13.17Unsuccessful_Add_Task.png.webp?alt=media&token=449c1620-1635-4c23-a82d-33b5f2e2e8e5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error in Adding Task due to Due Date Format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div>Purpose of the Function : The add_task function creates a new task using<br>a template (TASK_TEMPLATE), fills it with data provided as arguments (name, description, and<br>due date), updates the lastActivity timestamp to the current datetime, and then adds<br>this new task to the tasks list.</div><div><br></div><div>Updating lastActivity: The function updates the lastActivity<br>field of the task with the current datetime using datetime.now() to record the<br>time of the most recent activity related to the task.</div><div><br></div><div>Checking for Missing Data:<br>It checks whether the name, description, and due arguments are provided. If any<br>of these are missing (i.e., empty strings), it prints a message indicating that<br>the addition of the task failed due to missing data.</div><div><br></div><div>Validating the Due Date<br>Format: The function attempts to convert the due argument to a datetime format<br>using the str_to_datetime function. If the conversion fails (raises a ValueError), it prints<br>a message indicating that the due date format is not recognized.</div><div><br></div><div>Setting Task Properties:<br>After validating the data, it sets the name, description, and due fields of<br>the task dictionary with the provided arguments.</div><div><br></div><div>Adding the Task to the List: It<br>adds the newly created task to the tasks list.</div><div><br></div><div>Output Messages: Depending on the<br>outcome, the function prints messages confirming whether the task was successfully added or<br>if it was rejected due to missing data.</div><div><br></div><div>Saving Data: The save() function is<br>called to persist any changes made to the tasks list in a JSON<br>file named "tracker.json."</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T05.35.13image.png.webp?alt=media&token=b17ee8e6-8034-490c-9446-3501a5b9f3a5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Process Update Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div>Retrieving Task by Index: The function takes an index as an argument and<br>uses it to access a task from the tasks list. It includes error<br>handling to check for out-of-bounds scenarios, ensuring that the index is valid.</div><div><br></div><div>Displaying Current<br>Task Properties: The function prints out the current values of various task properties,<br>including name, description, and due date. These values are obtained from the task<br>retrieved using the provided index.</div><div><br></div><div>User Input for Updates: After displaying the current task<br>properties, the function prompts the user to enter new values for these properties.<br>It uses input() to collect user input for the name, description, and due<br>date.</div><div><br></div><div>Passing Data to update_task(): The function then calls the update_task() function, passing the<br>index and the user-inputted values (name, description, and due date) as arguments. This<br>initiates the process of updating the task with the new values.</div><div><br></div><div>Handling Invalid Index:<br>In cases where the provided index is out of bounds (less than 0<br>or greater than or equal to the length of the tasks list), the<br>function prints a message asking the user to provide a valid index.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T05.37.17image.png.webp?alt=media&token=362f111a-3d47-495e-a7f0-d404a7d4867e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update Task Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.14.47Update_Task_success.png.webp?alt=media&token=c0afbc80-b0ca-44eb-939f-e310a55d9c40"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated Task Screenshot with Success Message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.19.45NotUpdate_Task_success.png.webp?alt=media&token=77f740bd-7d4e-40ab-950f-827ade2feba3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Not Update the Task Screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div>Finding the Task by Index: The function takes an index as an argument<br>and uses it to access a task from the tasks list. It includes<br>error handling to check for out-of-bounds scenarios, ensuring that the index is valid.</div><div><br></div><div>Updating<br>Task Properties: The function updates the task's properties (name, description, and due date)<br>if new values are provided as arguments (i.e., name, description, or due). If<br>any of these values are provided, they replace the existing task properties.</div><div><br></div><div>Updating lastActivity:<br>The function updates the lastActivity field of the task with the current datetime<br>using datetime.now() to record the time of the most recent activity related to<br>the task.</div><div><br></div><div>Output Messages for Update Status: Depending on whether any of the task<br>properties were changed, the function prints a message indicating whether the task was<br>updated or not. If at least one property is updated, it prints "Task<br>is updated." Otherwise, it prints "Task is not updated."</div><div><br></div><div>Handling Invalid Index: In cases<br>where the provided index is out of bounds (less than 0 or greater<br>than or equal to the length of the tasks list), the function prints<br>a message asking the user to provide a valid index.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T17.51.56image.png.webp?alt=media&token=bf98faca-4d2f-42f2-a3d3-1f509fad0322"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mark Task Done Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T17.53.48image.png.webp?alt=media&token=abc0fe6d-9321-4acd-87c5-7400a8efe823"/></td></tr>
<tr><td> <em>Caption:</em> <p>This pic shows how first second task was marked done by the mark_done()<br>method.<br>Then, if we tried to do again it showed failure as it is<br>already completed.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div>Finding the Task by Index: The function takes an index as an argument<br>and uses it to access a task from the tasks list. It includes<br>error handling to check for out-of-bounds scenarios, ensuring that the index is valid.</div><div><br></div><div>Updating<br>Task Status to "Done": If the task is not currently marked as "done"<br>(i.e., the done property is False), the function records the current datetime as<br>the value of the done property. This ensures that the task's completion timestamp<br>is accurately recorded.</div><div><br></div><div>Handling Already Completed Task: If the task is already marked as<br>"done" (i.e., the done property is True), the function prints a message indicating<br>that the task is already completed. This prevents accidental re-marking of completed tasks.</div><div><br></div><div>Handling<br>Invalid Index: In cases where the provided index is out of bounds (less<br>than 0 or greater than or equal to the length of the tasks<br>list), the function prints a message asking the user to provide a valid<br>index.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T06.17.50image.png.webp?alt=media&token=d8b8d7b3-e649-426c-9990-e32276e48c26"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Task Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.32.15View_Task.png.webp?alt=media&token=426f17ac-3133-4df4-8800-6838461975da"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Task Success<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.34.10image.png.webp?alt=media&token=ed75299e-3872-4475-b60d-e1b524ef2199"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Task Failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.34.52View_Task.png.webp?alt=media&token=1e1b0c61-858d-454d-87d7-d22a342607ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Task With Four Tasks in List<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T06.18.41image.png.webp?alt=media&token=1d829dac-464a-4259-bbe5-70ada6268fec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Task Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T16.54.07image.png.webp?alt=media&token=27224b8c-c018-45e7-b4e9-561fd9708f7a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Task Successfully <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T16.54.57image.png.webp?alt=media&token=38f22568-78a2-4321-9f26-315148bfbf28"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Task unsuccessful due to Invalid index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div>Finding the Task by Index: The function takes an index as an argument<br>and uses it to access a task from the tasks list. It includes<br>error handling to check for out-of-bounds scenarios, ensuring that the index is valid.</div><div><br></div><div>Deleting<br>the Task: The function deletes the task from the tasks list using the<br>pop() method. If the task is successfully deleted, it prints a message indicating<br>that the task was deleted successfully. If there's an issue with the deletion,<br>it prints an error message.</div><div><br></div><div>Handling Invalid Index: In cases where the provided index<br>is out of bounds (less than 0 or greater than or equal to<br>the length of the tasks list), the function prints a message indicating that<br>the provided index is invalid.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T07.16.38image.png.webp?alt=media&token=8a6d9883-4a8e-47bb-95a0-0cc8f033f6a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Incomplete Tasks Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T17.56.42image.png.webp?alt=media&token=789f8bd4-8654-493c-83fb-faaaa096b4cb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing two incomplete tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T17.57.43image.png.webp?alt=media&token=69743748-e063-4528-a940-37d69f90f20d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing when there are no incomplete tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>Generating a List of Incomplete Tasks: The function creates a new list called<br>incomplete_tasks by using a list comprehension. It iterates through the tasks list and<br>filters out tasks that are not marked as "done" (i.e., where the done<br>property is False).</div><div><br></div><div>Printing Incomplete Tasks: If there are incomplete tasks in the incomplete_tasks<br>list, the function passes this list to the list_tasks() function, which prints a<br>summary view of these incomplete tasks. If there are no incomplete tasks, it<br>prints a message stating that there are no incomplete tasks to show.</div><div><br></div><div>Handling Output:<br>The function ensures that the output message is clear and informative, displaying either<br>the incomplete tasks or a message indicating their absence.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T07.52.09image.png.webp?alt=media&token=81e96970-b99d-407a-98a3-43b23078ec37"/></td></tr>
<tr><td> <em>Caption:</em> <p>Get Over Due Tasks <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.49.54Overdue_Task.png.webp?alt=media&token=915e5e01-12bf-403b-81ba-3da55a1d3785"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success OverDue Task<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T17.58.39image.png.webp?alt=media&token=da6606e9-e289-4fa4-bf92-fd0e5c2de15e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failure when no task is overdue<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div>Generating a List of Overdue Tasks: The function creates a new list called<br>overdue_tasks using a list comprehension. It iterates through the tasks list and filters<br>out tasks that are not marked as "done" (i.e., where the done property<br>is False) and have a due date that is older than the current<br>date and time.</div><div><br></div><div>Passing Overdue Tasks to list_tasks(): If there are overdue tasks in<br>the overdue_tasks list, the function passes this list to the list_tasks() function. This<br>function prints a summary view of these overdue tasks.</div><div><br></div><div>Handling Output: The function ensures<br>that the output message is clear and informative, displaying either the overdue tasks<br>or a message indicating their absence.</div><div><br></div><div>Converting Due Dates: The str_to_datetime() function is used<br>to convert the due dates from string format to datetime objects for comparison<br>with the current date and time.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T07.54.11image.png.webp?alt=media&token=23fca631-9e79-4a0b-a1f2-1196660c4538"/></td></tr>
<tr><td> <em>Caption:</em> <p>Get Time Remaining Logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.47.04Remaining_Time.png.webp?alt=media&token=6b721347-3ab0-4b41-8ea1-bbe5af5b84da"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success for get_time_remaining<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T15.49.06image.png.webp?alt=media&token=8e36d97a-e59a-4d3e-a3ad-74ee63fb8447"/></td></tr>
<tr><td> <em>Caption:</em> <p>Overdue message Failure<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div>Getting the Task by Index: The function starts by checking if the provided<br>index is within the valid range for the tasks list. If the index<br>is invalid (either negative or greater than or equal to the length of<br>the tasks list), it prints an appropriate error message and returns, effectively handling<br>index out-of-bounds scenarios.</div><div><br></div><div>Calculating Time Difference: The function calculates the time difference between the<br>due date of the task and the current date and time using the<br>str_to_datetime() function. This calculation is done using datetime objects, making it suitable for<br>accurate time comparisons.</div><div><br></div><div>Displaying Remaining Time: If the calculated time difference is positive (i.e.,<br>the due date is in the future), the function calculates the number of<br>days, hours, minutes, and seconds remaining until the task is due. It then<br>prints this information in a clear format, showing the remaining time components separately.</div><div><br></div><div>Displaying<br>Overdue Time: If the calculated time difference is negative (i.e., the due date<br>has passed), the function calculates the number of days, hours, minutes, and seconds<br>by which the task is overdue. It then prints this information, clearly noting<br>that the task is overdue, and ensuring that the values are positive (no<br>negative values are shown).</div><div><br></div><div>Handling Output: The function ensures that the output messages are<br>informative and easy to understand. It includes the task index in the output<br>to specify which task's time is being displayed.</div><div><br></div><div>Converting Due Dates: The str_to_datetime() function<br>is used to convert the due date from a string format to a<br>datetime object for accurate time calculations.</div><div><br></div><div>No Data Modification: This function is primarily responsible<br>for calculating and displaying time-related information and does not modify any data within<br>the tasks list.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-09T03.48.32Misc.png.webp?alt=media&token=90f92aa3-62ad-4cf3-b5cc-db1cd3aaf69b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of some significant outputs other than above mentioned some<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-09T03.48.45Misc1.png.webp?alt=media&token=d52866ef-801d-41c9-889a-a85a8f270f92"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshots of some significant outputs other than above mentioned some<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-09T20.50.58image.png.webp?alt=media&token=eb8fe572-ce47-4124-a86d-2eb7cb302d2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of some significant otuput<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-08T20.12.01image.png.webp?alt=media&token=91af3cd8-49ea-4570-8a82-e1770ebf970b"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON FILE<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-09T20.50.10After_Delete.png.webp?alt=media&token=b52266cf-a6a2-45b0-9ddd-56b6d2aecd80"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON file after deleting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-09T20.50.11After_Adding_Json.png.webp?alt=media&token=3f0c1663-08c7-4e3c-a84f-0d4ec3879e44"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON file after adding again<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <div><span style="letter-spacing: 0.09996px;">Issues include input validation, error handling, data integrity, date/time handling, and<br>user interface.</span></div><div><span style="letter-spacing: 0.09996px;">Solutions involve improving input validation, adding error handling, ensuring data<br>integrity, enhancing date/time handling, and improving user interface.</span></div><div><span style="letter-spacing: 0.09996px;">Learnings include the importance<br>of testing, code organization, documentation, version control, and user feedback to make a<br>more robust and user-friendly application.</span></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/6">https://github.com/iamshashwat10/ss4746-is601-007/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/ss4746" target="_blank">Grading</a></td></tr></table>