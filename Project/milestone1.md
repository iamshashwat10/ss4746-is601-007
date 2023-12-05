<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Shashwat Singh (ss4746)</td></tr>
<tr><td> <em>Generated: </em> 11/13/2023 10:35:03 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/ss4746" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-13T21.42.03image.png.webp?alt=media&token=a2778904-7755-4d7c-afa3-8e99b713898b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.32.38image.png.webp?alt=media&token=e71eda74-d99b-48f2-b278-f8568c1003df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.20.24image.png.webp?alt=media&token=6c88f294-667a-4ac2-ac30-c2da62d196fe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Match Error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.21.11image.png.webp?alt=media&token=2d733136-ebb5-4a3d-bc34-878d1b07654b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Not Available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.23.11image.png.webp?alt=media&token=7f2f3fed-fc26-4e55-b93d-23309e012170"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Not Available <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.25.18image.png.webp?alt=media&token=d55b99b2-35aa-40fa-80e3-dff5c6b6c967"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.27.46image.png.webp?alt=media&token=89e4502b-9506-4df0-8465-7f27ff363575"/></td></tr>
<tr><td> <em>Caption:</em> <p>The valid user data from Task 1 should be present in this screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/26">https://github.com/iamshashwat10/ss4746-is601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 14px;">The registration form utilizes a secure POST method for submitting user<br>data with fields for username, email, password, and confirmation.&nbsp;</span><div><span style="font-size: 14px;">B</span>ackend SQL operations<br>handle validation, ensuring unique usernames and emails, valid email formats, and password criteria<br>adherence.</div><div>Passwords undergo hashing before SQL insertion to enhance security.&nbsp;</div><div>The database interactions involve secure<br>insertions using parameterized queries or other SQL injection prevention methods.&nbsp;</div><div>While frontend validation isn&#39;t<br>explicitly detailed, backend SQL processes prioritize data security and integrity.&nbsp;</div><div>The registration process underscores<br>SQL best practices for secure user information storage and validation, contributing to a<br>seamless and protected user registration experience.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.31.47image.png.webp?alt=media&token=3cf48d1e-fb6e-49b2-a41d-e1c676c48830"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.33.41image.png.webp?alt=media&token=c2b33aa7-d074-47b2-b4ff-49a9bb1ab3b1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.34.12image.png.webp?alt=media&token=163c25e3-4083-4e36-8183-4e113c6e4ea6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login Success<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/26">https://github.com/iamshashwat10/ss4746-is601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>The registration form utilizes a secure POST method for submitting user data with<br>fields for username, email, password, and confirmation.&nbsp;<div>Backend SQL operations handle validation, ensuring unique<br>usernames and emails, valid email formats, and password criteria adherence.</div><div>Passwords undergo hashing before<br>SQL insertion to enhance security.&nbsp;</div><div>The database interactions involve secure insertions using parameterized queries<br>or other SQL injection prevention methods.&nbsp;</div><div>While frontend validation isn&#39;t explicitly detailed, backend SQL<br>processes prioritize data security and integrity.&nbsp;</div><div>The registration process underscores SQL best practices for<br>secure user information storage and validation, contributing to a seamless and protected user<br>registration experience.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.35.18image.png.webp?alt=media&token=ed86a92a-ce34-412d-af4f-ca9a07a4e155"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logout<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.36.14image.png.webp?alt=media&token=3c246b62-fb5a-4d3d-9446-dad26cc53e46"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login Protected<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/26">https://github.com/iamshashwat10/ss4746-is601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">Session logic in a login system involves several steps to ensure<br>secure user authentication and controlled access to protected pages. When a user logs<br>in, their credentials are verified, and upon success, a unique session identifier is<br>generated. This identifier is stored, either as a cookie in the user's browser<br>or on the server-side, marking the user as authenticated. Protected pages, like a<br>dashboard, are configured to be accessible only to users with valid sessions.</span></div><div><span style="font-size:<br>14px;"><br></span></div><div><span style="font-size: 14px;">When a user attempts to access a login-protected page, the server<br>checks for a valid session. If the session is absent or has expired,<br>the user is redirected to the login page, preventing unauthorized access. The session<br>is typically managed with a timeout to enhance security. When a user logs<br>out, the session identifier is invalidated, ensuring the user loses access to protected<br>content.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">The logic involves verifying credentials, creating and managing sessions,<br>and checking for session validity when accessing protected pages. This session-based approach enhances<br>user security, offering a seamless experience where only authenticated users can access designated<br>content, effectively demonstrating that a logged-out user cannot reach login-protected pages.</span></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.37.33image.png.webp?alt=media&token=7fdccbf6-0e5b-4855-8511-66deffeb9e54"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login Protected<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.39.20image.png.webp?alt=media&token=28c30edf-e43c-4d22-844f-668d09cdb2d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied to Non Admins<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.40.06image.png.webp?alt=media&token=7b7f89aa-4be0-4c87-9fde-73cf2ed7b39b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles Table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.40.48image.png.webp?alt=media&token=344455d5-cb37-4728-b7ad-3b29e52e4bc3"/></td></tr>
<tr><td> <em>Caption:</em> <p>User 1 is my Admin  (Given admin role to only one)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/27 ">https://github.com/iamshashwat10/ss4746-is601-007/pull/27 </a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div><span style="font-size: 14px;">In the context of login-protected pages, the process typically involves a<br>server-side framework,and utilizes session management for user authentication. When a user logs in,<br>their credentials are authenticated, and a unique session identifier is generated, associating the<br>user with a valid session. This session identifier is stored, either as a<br>cookie on the user's browser or on the server-side.</span></div><div><span style="font-size: 14px;"><br></span></div><div><span style="font-size: 14px;">Login-protected<br>pages are configured to check for the presence of a valid session when<br>a user attempts to access them. The server-side logic verifies if the user<br>has an active session; if not, the user is redirected to the login<br>page. This mechanism ensures that only authenticated users with valid sessions can access<br>protected content.</span></div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 14px;">Role-protected pages in web applications establish controlled access based on user<br>roles or authorization levels.&nbsp;</span><div><span style="font-size: 14px;">This process involves assigning roles during user creation<br>or updates, designating specific privileges to roles like &quot;admin&quot; or &quot;user.&quot;&nbsp;</span></div><div><span style="font-size: 14px;">When<br>users attempt to access role-protected pages, the server-side logic verifies their assigned role,<br>ensuring appropriate authorization.</span><div><span style="font-size: 14px;">We use SQL tables in our database to assign<br>roles to these users and once successful&nbsp;done, we can confirm roles of each<br>user and give them permission likewise.&nbsp;</span></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.42.25image.png.webp?alt=media&token=e8c8bda4-9e79-4f97-8d6f-8d80e835e53b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Styles Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.42.38image.png.webp?alt=media&token=7b1c04f7-e910-4050-b650-8eee028103df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Styles Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.42.59image.png.webp?alt=media&token=7748a3fa-559c-4314-99b1-fb791d6baba5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Styles Applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.43.17image.png.webp?alt=media&token=406cf9f7-69c0-443d-b4d4-8bd9f70e193e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Styles Applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/28">https://github.com/iamshashwat10/ss4746-is601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>We used following concepts of CSS&nbsp; to make look our website stylish and<br>cool<div><div><span style="font-size: 14px;">Selectors: Define which HTML elements the styles should apply to.</span></div><div><span style="font-size:<br>14px;">Properties: Specify the visual attributes of selected elements (e.g., color, font-size, margin).</span></div><div><span style="font-size:<br>14px;">Values: Assign specific values to properties, determining the appearance of the selected elements.</span></div><div>&lt;span<br>style=&quot;font-size: 14px;&quot;&gt;Selectors Hierarchy: Establish a hierarchy for styling, enabling the cascading nature of<br>CSS, where styles can be inherited and overridden.</span></div><div><span style="font-size: 14px;">CSS allows for the<br>creation of responsive designs, ensuring that web content adapts to different screen sizes<br>and devices. It plays a crucial role in enhancing the user experience by<br>creating visually appealing and well-organized web interfaces. CSS rules can be written directly<br>in HTML files or kept in separate stylesheet files for better maintainability and<br>reusability.</span></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.46.39image.png.webp?alt=media&token=392c0557-0875-473f-91ee-ab97f8a6aeb0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error SS<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/29">https://github.com/iamshashwat10/ss4746-is601-007/pull/29</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>User-friendly messages are crafted for clarity and conciseness, ensuring easy comprehension.&nbsp;</div><div>Consistent use of<br>positive language, maintaining context awareness, and effective error handling contribute to a positive<br>user experience.&nbsp;</div><div>Messages also offer user assistance, such as relevant links or support details,<br>for additional information or help when needed.&nbsp;</div><div>Prioritizing these elements enhances the overall usability<br>and user-friendliness of the interface or application.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.47.38image.png.webp?alt=media&token=4c848dc8-f4c2-48ba-b1db-304c4cbc1604"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/28">https://github.com/iamshashwat10/ss4746-is601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 14px;">User data retrieval and display involve direct fetching from an SQL<br>table.</span><div><span style="font-size: 14px;">&nbsp;The backend initiates an SQL query, such as SELECT username, email<br>FROM users WHERE user_id = ?, retrieving the user&#39;s username and email.&nbsp;</span></div><div><span style="font-size:<br>14px;">The obtained data is then passed to the template as variables, like return<br>render_template(&#39;profile.html&#39;, username=user_data[&#39;username&#39;], email=user_data[&#39;email&#39;]).&nbsp;</span></div><div><span style="font-size: 14px;">Within the template, {{ render_field(form.username) }} and {{ render_field(form.email)<br>}} statements dynamically fill the form fields with the user&#39;s current username and<br>email.&nbsp;</span></div><div><span style="font-size: 14px;">This seamless integration allows users to view their existing information when<br>accessing the profile page, creating a user-friendly experience for modifying and updating their<br>profile details.&nbsp;</span></div><div><span style="font-size: 14px;">The backend process ensures efficient data retrieval, fostering a personalized<br>and responsive interface for users interacting with their profile information.</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.49.28image.png.webp?alt=media&token=26c5b279-9ba1-4e94-b47d-abac4c1aa2cf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username Updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.50.04image.png.webp?alt=media&token=aeaf99b9-88b7-4911-b3d8-7179f0b9f2e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.51.35image.png.webp?alt=media&token=5c8690ba-a4a9-404a-9496-86529bdb964d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.52.13image.png.webp?alt=media&token=4c12a23c-7d97-4df4-802d-5ca29cb1adf9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Missmatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.53.07image.png.webp?alt=media&token=7faac2d3-760c-4ecd-a381-4761e88ea5a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-11-14T02.57.26image.png.webp?alt=media&token=0072aac6-c252-4aa9-8f77-5abf6e7b28b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated Table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/28">https://github.com/iamshashwat10/ss4746-is601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p><span style="font-size: 14px;">When a user successfully edits their profile, the backend logic manages<br>the update of email, username, and password, incorporating validation measures.&nbsp;</span><div><span style="font-size: 14px;">Upon form<br>submission, the backend validates the data, checking email format, ensuring username and email<br>uniqueness, and verifying password security.&nbsp;</span></div><div><span style="font-size: 14px;">If validation passes, the backend updates the<br>corresponding records in the database, employing security measures like password hashing.&nbsp;</span></div><div><span style="font-size: 14px;">The<br>user receives a success message upon a successful update, while validation failures prompt<br>appropriate error messages.</span></div><div><span style="font-size: 14px;">In cases where sensitive information like passwords is updated,<br>the session may be revalidated.&nbsp;</span></div><div><span style="font-size: 14px;">This comprehensive approach ensures a secure and<br>validated process for users, maintaining the integrity and security of their profile information.</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I learned how to make different HTML and CSS files. How to make<br>register and login pages.<div>How to make different SQL tables and give roles to<br>different users according to SQL table entries.</div><div>i also learned how to utilize different&nbsp;<br>packages of flask and everything.</div><div>I faced difficulties in following ways:</div><div>1. I was not<br>able to give roles and apply correctly.</div><div>2. I was not able to use<br>CSS styling efficiently.</div><div>3. I was not able to user Heroku app .yml files<br>updates.</div><div>With the help of class files and professor i was able to correct<br>all my errors and succeed in completion of this Assignment.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ss4746-prod-9774fc88225a.herokuapp.com/login">https://is601-ss4746-prod-9774fc88225a.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/ss4746" target="_blank">Grading</a></td></tr></table>