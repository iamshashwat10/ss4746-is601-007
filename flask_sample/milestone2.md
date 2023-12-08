<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Shashwat Singh (ss4746)</td></tr>
<tr><td> <em>Generated: </em> 12/7/2023 11:39:44 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/ss4746" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <div>API Link: https://rapidapi.com/api-sports/api/api-football</div><div><br></div><div>Free Tier Limits: 100/day hard limit</div><div><br></div><div>What content/entities are you retrieving? The<br>API retrieves a massive of information on football match Livescore (15s), live &amp;<br>pre-match odds, events, line-ups, coachs, players, top scorers, standings, statistics, transfers</div><div><br></div><div>How do you<br>intend to use the data?: I want to enable users to check whether<br>a specific team is in my database and provide information about the teams.<br>Additionally, I plan to allow users to create their own teams by selecting<br>players from the available data.</div><div><br></div><div>Are you using the data as-is or are you<br>doing something interesting with it, if the latter, what are you doing? I<br>intend to use the data as-it-is and let the user personalize/update it as<br>per their needs. The original data most probably will remain the same, but<br>would have custom attributes added on to their respective entities.</div><div><br></div><div>What information gives you<br>the confidence that this API is active and will be active at least<br>for the rest of the semester? It was the popularity of 10/10 and<br>the API was updated just 5 month ago and in the discussions tab,<br>the people’s queries a few hours back were answered quick enough which makes<br>me believe that the API will be active at least, for the coming<br>few months.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">List Teams Endpoint:</span></div><div><span style="font-size: 14px;">Endpoint: /v3/teams</span></div><div><span style="font-size: 14px;">Purpose: Retrieve a list<br>of football teams.</span></div><div><span style="font-size: 14px;">Parameters: You can include parameters like the team name,<br>country, league, etc., to filter the results.</span></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div>'team': { 'id': 529,&nbsp; name': 'Barcelona',&nbsp; &nbsp;'code': 'BAR',&nbsp; 'country': 'Spain',&nbsp; &nbsp;'founded': 1899,&nbsp; 'national':<br>False, 'logo': 'https://media-4.api-sports.io/football/teams/529.png'}</div><div><div><span style="font-size: 14px;">For Football Teams:</span></div><div><span style="font-size: 14px;">id:</span></div><div><span style="font-size: 14px;">Purpose: A unique<br>identifier for the football team.</span></div><div><span style="font-size: 14px;">Usage: Primary key in the database for<br>team records.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">name:</span></div><div><span style="font-size: 14px;">Purpose: The name of the football<br>team.</span></div><div><span style="font-size: 14px;">Usage: Displayed in the application for team identification.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size:<br>14px;">code:</span></div><div><span style="font-size: 14px;">Purpose: A short code representing the team.</span></div><div><span style="font-size: 14px;">Usage: Can be<br>used for additional identification or display purposes.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">country:</span></div><div><span style="font-size: 14px;">Purpose:<br>The country the team belongs to.</span></div><div><span style="font-size: 14px;">Usage: Provides information about the team's<br>origin.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">founded:</span></div><div><span style="font-size: 14px;">Purpose: The year the football team was<br>founded.</span></div><div><span style="font-size: 14px;">Usage: Historical information about the team.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">national:</span></div><div><span style="font-size:<br>14px;">Purpose: Indicates whether the team is a national team (True/False).</span></div><div><span style="font-size: 14px;">Usage: Helps<br>categorize teams based on their nature.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">logo:</span></div><div><span style="font-size: 14px;">Purpose: URL<br>to the team's logo image.</span></div><div><span style="font-size: 14px;">Usage: Display the team logo in the<br>application.</span></div></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">The primary goal of the different entities (Football Teams) is to<br>provide comprehensive information about football teams and their associated venues. This information is<br>crucial for creating a rich user experience in the application, enabling users to:</span></div><div><span<br>style="font-size: 14px;">Explore Teams: Users can search and view detailed information about football teams,<br>including their names, countries, founding years, and logos.</span></div><div><span style="font-size: 14px;">Team Management: Admins can<br>add, edit, and delete football teams, ensuring the application stays updated with the<br>latest information.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Data Usage:</span></div><div><span style="font-size: 14px;">Football Teams:</span></div><div><span style="font-size: 14px;">Search and<br>Display: Teams' data will be displayed in the application, allowing users to search<br>for specific teams and view their details.</span></div><div><span style="font-size: 14px;">User Interaction: Users can interact<br>with team data, such as searching, viewing details, and potentially favoriting teams.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.17.58Create_FilledWithData.png.webp?alt=media&token=b9d90eb5-9943-4278-bb1e-d9435522c0b4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form with valid data filled in, but not yet submitted<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.18.07Create_Errors.png.webp?alt=media&token=0dc1b2a4-6cb1-4f43-838c-2b6cb26baf70"/></td></tr>
<tr><td> <em>Caption:</em> <p>The various data validation messages when attempt to insert invalid data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.18.16Create_Success.png.webp?alt=media&token=cb02d520-21d4-46dc-a99a-9a88a0bffc13"/></td></tr>
<tr><td> <em>Caption:</em> <p>The success message upon valid data insertion<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.18.29Create_Duplicate.png.webp?alt=media&token=47fee7aa-5d16-4f7d-a717-751f0fbd4a32"/></td></tr>
<tr><td> <em>Caption:</em> <p>duplicate records are handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.18.42Create_CodeSnippet.png.webp?alt=media&token=69226acf-c8ea-4d75-99c0-493d0c3beed0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippets may be included and should contain ucid/date comments.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T03.20.34Create_Database.png.webp?alt=media&token=7c2f6110-a15b-4697-9155-384978f22f7e"/></td></tr>
<tr><td> <em>Caption:</em> <p> the previous task having been inserted into the DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/35">https://github.com/iamshashwat10/ss4746-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T05.30.05image.png.webp?alt=media&token=a1cc6fdc-dca5-4e79-aea5-87cb3e8bd047"/></td></tr>
<tr><td> <em>Caption:</em> <p>mix of custom records and API-based records  mentioned in source<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T05.31.00image.png.webp?alt=media&token=cfffe879-3744-4438-a244-ca7db6c5ea55"/></td></tr>
<tr><td> <em>Caption:</em> <p>Applied Sort order filter on ID and Name column <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T05.31.57image.png.webp?alt=media&token=b46c4362-8a3b-40b7-b6c0-72707920ae78"/></td></tr>
<tr><td> <em>Caption:</em> <p>If I select 2 and apply, only top two results pop up<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T05.33.07image.png.webp?alt=media&token=bd47b919-78d4-4b15-843e-b7e0166fd727"/></td></tr>
<tr><td> <em>Caption:</em> <p>Each list item should have a link to single-view, edit, and delete pages/routes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T05.46.25image.png.webp?alt=media&token=3369c61d-4769-446e-88f0-e6857eb2fa3a"/></td></tr>
<tr><td> <em>Caption:</em> <p>A filter with no matching records should clearly show no results available (message<br>format is your choice)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/35">https://github.com/iamshashwat10/ss4746-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-07T15.31.57image.png.webp?alt=media&token=bb3515a9-97e4-4f66-a9d8-96b490e9ab1b"/></td></tr>
<tr><td> <em>Caption:</em> <p>View Edit Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/35">https://github.com/iamshashwat10/ss4746-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.29.29image.png.webp?alt=media&token=a2a745b0-4c25-47f9-9fb2-b05df6f0874f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form should prefill with existing entity data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.30.01image.png.webp?alt=media&token=eb720b6e-70b7-4d6a-a6be-95326ae1c3bf"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message when an edit is successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-08T04.34.38image.png.webp?alt=media&token=657f8342-95d8-43b2-aef9-b25fe9450dae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation errors<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.31.54image.png.webp?alt=media&token=8bbe1ea2-2f6a-40fe-a219-8ae9f29f8acb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before ediit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.32.50image.png.webp?alt=media&token=7c219182-af3c-4e27-a557-3e12a97328b3"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit (change code to real)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/35">https://github.com/iamshashwat10/ss4746-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.48.48image.png.webp?alt=media&token=2005720f-132e-4d1f-91f3-65c4a33b1ec8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete should hold and pass the filter/sort criteria from the search page and<br>re-apply it upon direct like previous lessons have shown<br><br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.47.17image.png.webp?alt=media&token=a2d2887c-1e06-4ca3-b7ba-f766cafed9dc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before Delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-06T06.49.31image.png.webp?alt=media&token=40c15345-7e62-4e6c-8d90-c0b9f51a3aad"/></td></tr>
<tr><td> <em>Caption:</em> <p>After Delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/36">https://github.com/iamshashwat10/ss4746-is601-007/pull/36</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-07T16.47.18image.png.webp?alt=media&token=3aaac689-8fd5-4a7d-a9fb-d7fc30e0831d"/></td></tr>
<tr><td> <em>Caption:</em> <p>User triggering this fetch, Code for API Data Fetch, transforming API data to<br>database and handling duplicates<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <div>User Input: The process starts when a user submits the team search form.<br>This form likely contains an input field where the user enters the name<br>of the football team they want to fetch information about.</div><div><br></div><div>Form Validation: The form.validate_on_submit()<br>condition checks if the form is submitted and validates its contents. If the<br>form is valid, the process continues.</div><div><br></div><div>API Request: The code uses the API.get method,<br>presumably from a custom class API that interacts with a football-related API. It<br>sends a request to the API's /v3/teams endpoint with the team name as<br>a parameter.</div><div><br></div><div>API Response Handling: The result of the API request is then processed.<br>If the API returns results (result.get('results', 0) &gt; 0), it means that information<br>about the requested team is available.</div><div><br></div><div>Data Transformation: The team data is extracted from<br>the API response (team_data = result['response'][0]['team']). This data is then transformed into a<br>format suitable for insertion into the database.</div><div><br></div><div>Database Operation: The transformed team data is<br>inserted into the IS601_Team table in the database using the DB.insertOne method. The<br>ON DUPLICATE KEY UPDATE clause ensures that if a team with the same<br>ID already exists in the database, its information is updated.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/36">https://github.com/iamshashwat10/ss4746-is601-007/pull/36</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Throughout this milestone, one notable issue was encountered during the implementation of data<br>validation and error handling in the Flask application. Specifically, the challenge was ensuring<br>that multiple error messages for different form fields were correctly displayed when there<br>were validation errors. The initial implementation only showed a generic error message, making<br>it difficult to identify specific issues with the form submission.</div><div><br></div><div>To address this issue,<br>I learned that Flask's validate_on_submit() method, while useful, didn't provide a granular approach<br>to handling individual form field errors. To overcome this limitation, I modified the<br>validation process, directly accessing form fields from the request.form object and checking for<br>specific conditions. This allowed for more precise validation and the display of distinct<br>error messages for each relevant form field.</div><div><br></div><div>In terms of resources, the Flask documentation<br>and community forums were valuable references for understanding form validation intricacies and refining<br>the error-handling mechanism. The experience reinforced the importance of closely aligning form validation<br>strategies with specific project requirements, ensuring a user-friendly experience by providing meaningful error<br>feedback.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ss4746-prod-9774fc88225a.herokuapp.com/login">https://is601-ss4746-prod-9774fc88225a.herokuapp.com/login</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-08T04.18.04image.png.webp?alt=media&token=32d06af5-d771-4fa7-8a4a-cdb8ee6f851f"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime SS<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-12-08T04.18.20image.png.webp?alt=media&token=cd8ecce5-57f0-43b9-a7ee-d5c372abf523"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime SS<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/ss4746" target="_blank">Grading</a></td></tr></table>