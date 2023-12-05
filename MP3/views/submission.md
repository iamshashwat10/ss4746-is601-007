<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Shashwat Singh (ss4746)</td></tr>
<tr><td> <em>Generated: </em> 11/26/2023 4:25:04 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/ss4746" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-23T04.24.01image.png.webp?alt=media&token=9ead8722-85d4-4134-a117-e43794143c18"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.07.17image.png.webp?alt=media&token=48f74a4c-db76-424a-a87e-b586045dd6d4"/></td></tr>
<tr><td> <em>Caption:</em> <p>instance screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-23T04.23.26image.png.webp?alt=media&token=66322230-4bbf-49be-9099-fd8b08e2a859"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code Screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.07.54image.png.webp?alt=media&token=6f6fbfd8-1c1e-4bf9-b966-fcd13dcc320d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Instance Screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-23T07.02.03image.png.webp?alt=media&token=fa303d43-e6fc-4b50-8042-5fa164d3dec3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Not CSV File Error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.10.35image.png.webp?alt=media&token=ac4ddc34-4530-4f8e-b1b0-dea9669dfc5e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sucessfully added <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.28.51image.png.webp?alt=media&token=11da44db-0e98-4e0a-a867-eaa6b4d0d4c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import csv1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.31.31image.png.webp?alt=media&token=5558eba3-ce36-473c-90bd-7cfcdd318e81"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import CSV 2-3 with ucid code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.33.46image.png.webp?alt=media&token=f09fbf92-fd4c-4575-a681-9307a5f7ca69"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import CSV 4-5 with ucid code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T04.34.12image.png.webp?alt=media&token=2b3861a9-8708-4bbb-8f07-f1fcd90d4a64"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import CSV 6-7-8 with ucid code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.09.51image.png.webp?alt=media&token=5a2ca12c-88ed-45cd-8383-025a1c1fdd09"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create View<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.10.29image.png.webp?alt=media&token=703c7956-dce3-416d-9a94-1f5a63f6cc53"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit View<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.11.52image.png.webp?alt=media&token=41a6f6be-6d34-4df1-81ff-f163febc66bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.12.17image.png.webp?alt=media&token=e311b678-3dd4-453f-95f2-9b436a9278d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.15.36image.png.webp?alt=media&token=b1ebba7d-2973-48ca-933b-61d3d68b47ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show the page loaded with proper list of donations (without any filter applied)<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.16.40image.png.webp?alt=media&token=247e10b3-7c36-4d94-891d-f7dad710933a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donor First Name Filter with Up Order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.18.54image.png.webp?alt=media&token=75dfda73-0f46-49c8-adfa-bcb3a20d56f3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Page with a filter of a specific organization applied (mayer)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.08.41image.png.webp?alt=media&token=cbcd2c44-9fe7-41bd-b2d7-9bbd32a454e9"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Page Screeenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.34.17image.png.webp?alt=media&token=08ee0035-e633-4086-826e-e7b420cfd7ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search 1-6 Python Code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.34.34image.png.webp?alt=media&token=aeaf1fe3-0ac1-4b4c-ba1f-971928700907"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search 7-12 Python Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.39.24image.png.webp?alt=media&token=6f6e3931-2504-4e69-b360-3dab3ea543e0"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.40.42image.png.webp?alt=media&token=29287d63-c9af-4b20-9d3c-215b3be14f88"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations add route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.57.54image.png.webp?alt=media&token=ca3bd607-7161-4a6d-91a2-269168407499"/></td></tr>
<tr><td> <em>Caption:</em> <p>donations edit route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T06.59.11image.png.webp?alt=media&token=13661e78-2b66-4379-88c8-bdccabb06e6a"/></td></tr>
<tr><td> <em>Caption:</em> <p> donations edit route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.02.15image.png.webp?alt=media&token=a7a31ced-11c4-4eb5-86de-fe8db5251a30"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donation delete route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.06.25image.png.webp?alt=media&token=159d1e09-b971-4490-be40-4d88d7a77fc8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully Deleted<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.13.50image.png.webp?alt=media&token=6d6f0be9-f900-4daf-bbe7-64159eb8a376"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create View<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.14.11image.png.webp?alt=media&token=e853a2bf-955e-4d1e-ac2c-ddd5362bf73c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.15.45image.png.webp?alt=media&token=d9380432-fe18-443c-bc73-61b39265bb5c"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.16.08image.png.webp?alt=media&token=55e611d1-2689-4913-99f0-69eb23efb25a"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.16.47image.png.webp?alt=media&token=0b7fd5c3-e7ac-47bf-b23d-493945632937"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.17.57image.png.webp?alt=media&token=ce7e160c-0ec6-473e-9f89-76a105ff39d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name Asc Order Filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.18.46image.png.webp?alt=media&token=9df90273-f3ba-4d06-8eb2-cb19761c2968"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code For Search Organizations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.19.47image.png.webp?alt=media&token=79d660c0-a80c-44c8-8e60-908a389c1214"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization search route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.20.49image.png.webp?alt=media&token=478dcdd6-94d3-4a81-873c-c2928597a54a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add1 to Add 8 Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.21.25image.png.webp?alt=media&token=6049c7ac-aaf2-4f37-8716-d154e62ac225"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add 9-10-11 Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.22.03image.png.webp?alt=media&token=5c81a798-20de-47f1-a250-37385470b59b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit 1 - 7 (A) Code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.22.43image.png.webp?alt=media&token=61bea6a8-271c-44fd-a6f1-de12db8cb978"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit 8 - 13 Code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T21.23.35image.png.webp?alt=media&token=14218cd1-9a22-45cd-91a7-3fa11bd5e27f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete Route Code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T05.35.49image.png.webp?alt=media&token=de5f75ba-3f48-4f9d-ada0-256a8e1f7516"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases Screenshot passing test_donations.py using -rA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T05.36.28image.png.webp?alt=media&token=7e3638b7-01cc-4246-9b1d-6acfd77c02ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases Screenshot passing test_donations.py using -rA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T05.36.50image.png.webp?alt=media&token=c1329d3e-03c2-4b48-987a-57ee3e178fd9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test Cases Screenshot passing test_donations.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T20.32.22image.png.webp?alt=media&token=cdb60d82-c3b5-4178-aa5a-3a2d927414ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_organizations.py using -rA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T20.32.37image.png.webp?alt=media&token=9ade1a35-06ec-40de-a3fb-17bdd92dfc7d"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_organizations.py using -rA<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T20.32.48image.png.webp?alt=media&token=021431dd-3946-40e7-a2c9-0d0c952b9288"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_organizations.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T05.42.56image.png.webp?alt=media&token=f183d032-4e1c-4272-a8a2-ae7e1dc58f81"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of passing test_upload.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T05.43.57image.png.webp?alt=media&token=eae82b26-819e-4f97-8a38-dc868efbf85b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add screenshot of passing test_index.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>All test cases passed.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/33">https://github.com/iamshashwat10/ss4746-is601-007/pull/33</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.13.40image.png.webp?alt=media&token=c32002f2-a05e-46d6-9d8d-558c487f7ef8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commit history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.16.59image.png.webp?alt=media&token=bb32fa43-b629-4568-a70c-5c6b5760c4e1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Waka TIme SS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.17.17image.png.webp?alt=media&token=9f2046b0-f909-4600-b9c0-f58ee59520b7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Waka TIme SS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-26T07.18.09image.png.webp?alt=media&token=bf1d6b9e-42b0-44d3-b1b3-b89f02d0c1ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Waka TIme SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-ss4746-td-3690e1d511f3.herokuapp.com/">https://is601-007-ss4746-td-3690e1d511f3.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/ss4746" target="_blank">Grading</a></td></tr></table>