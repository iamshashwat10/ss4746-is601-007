<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Shashwat Singh (ss4746)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 6:09:50 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/ss4746" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T00.30.37image.png.webp?alt=media&token=c7cda2c1-1d80-4d8c-933b-38ea0c38fecd"/></td></tr>
<tr><td> <em>Caption:</em> <p>add function, its description and its result output screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T00.32.13image.png.webp?alt=media&token=c092edd9-73eb-457e-8a98-74dc83caec43"/></td></tr>
<tr><td> <em>Caption:</em> <p>subtract function, its description and its result output screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T00.33.35image.png.webp?alt=media&token=d8916922-94cb-4fe4-b817-9b46acc4e100"/></td></tr>
<tr><td> <em>Caption:</em> <p>Multiply function, its description and its result output screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T00.35.08image.png.webp?alt=media&token=2ea0de1e-31af-4655-a041-6d381be9a776"/></td></tr>
<tr><td> <em>Caption:</em> <p>Division function, its description and its result output screen + divide by zero<br>error<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T03.36.02image.png.webp?alt=media&token=cb9ba689-b866-4d49-9df0-3884860658dd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing number-add-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T20.06.53image.png.webp?alt=media&token=533eead8-f55c-45db-89f4-858cbefa0671"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing ans-add-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T03.40.17image.png.webp?alt=media&token=e378b364-fe48-40f4-855f-3b9da76c4674"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing number-sub-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T20.47.39image.png.webp?alt=media&token=1c28a9f1-a5b1-4977-889d-0af42722d5c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing ans-sub-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T03.45.09image.png.webp?alt=media&token=70a45584-ab6f-4227-8f01-e76064211df0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing number-mult-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T20.50.39image.png.webp?alt=media&token=00bec49a-0110-4b1f-af0e-e14fc646e1d8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing ans-multi-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T03.47.19image.png.webp?alt=media&token=2c878b13-4d23-46bf-83ef-db50c1a593dc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing number-div-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fss4746%2F2023-10-16T20.52.47image.png.webp?alt=media&token=50ec851b-d999-4808-8bab-36ac74bb6e4c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passing ans-div-number Test Case and code snippet<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <div>During this module, I learned about creating a basic command-line calculator using Python.<br>I created a class called MyCalc that allows for addition, subtraction, multiplication, and<br>division operations. Some key takeaways from this assignment include:</div><div><br></div><div>Class Structure: I learned how<br>to structure a Python class with methods for performing specific operations. Each method<br>within the class handles a different mathematical operation.</div><div><br></div><div>Handling "ans" and Numbers: I learned<br>how to handle user input where "ans" refers to the previous result, and<br>numbers can be either integers or floating-point values. The calculator class is designed<br>to work with both types of inputs.</div><div><br></div><div>Error Handling: I incorporated error handling to<br>address scenarios like division by zero, ensuring that the calculator behaves gracefully and<br>provides informative messages to the user.</div><div><br></div><div>Recursion: The use of recursion to handle "ans"<br>as one of the operands in calculations. This feature adds flexibility to the<br>calculator.</div><div><br></div><div>Unit Testing with Pytest: I learned how to write unit tests for the<br>calculator methods using the Pytest framework. This allowed me to verify that the<br>calculator functions correctly and handles various input scenarios.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <div>Test cases are an essential part of software development, ensuring that code functions<br>correctly and as intended. In this assignment, I learned more about how test<br>cases work, and I had the opportunity to explore two important testing concepts:<br>fixtures and parameterized tests.</div><div><br></div><div>Test Cases Basics:</div><div>Test cases are functions or methods that verify<br>the behavior of specific parts of your code. They typically include the following<br>elements:</div><div><br></div><div>Setup: Preparing the necessary environment or data for the test.</div><div>Execution: Running the code<br>being tested.</div><div>Assertions: Verifying that the results match the expected outcomes.</div><div><br></div><div>Fixtures: Fixtures in testing<br>are a way to set up and tear down resources or contexts required<br>for one or more test cases. They provide a consistent and clean environment<br>for your tests.</div><div>In this assignment, I used a fixture named calculator to create<br>an instance of the MyCalc class for each test function. This ensures that<br>each test operates on a fresh calculator, preventing interference between tests.</div><div><br></div><div>Parameterized Tests: Parameterized<br>tests allow you to run the same test function with multiple sets of<br>inputs and expected outputs. This is especially useful when you have many similar<br>test cases.</div><div>I used parameterized tests in this assignment to test various scenarios of<br>calculator operations. For example, I tested addition with different sets of input numbers<br>and expected results without having to write separate test functions for each case.</div><div><br></div><div>Pytest<br>Framework: I learned that pytest is a popular testing framework in Python that<br>simplifies the process of writing and running tests.</div><div>Pytest automatically discovers and executes test<br>functions and provides a clean and informative test result output.</div><div><br></div><div>Test Organization: I learned<br>that well-organized test cases can significantly improve the maintainability and effectiveness of your<br>tests. In this assignment, I grouped tests for each calculator operation and ensured<br>they were clear and easy to read.</div><div>In summary, I gained a better understanding<br>of how test cases, fixtures, and parameterized tests work during this assignment. These<br>testing concepts are crucial for ensuring the correctness and reliability of software, and<br>pytest proved to be a powerful tool for test automation and reporting.</div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/iamshashwat10/ss4746-is601-007/pull/10">https://github.com/iamshashwat10/ss4746-is601-007/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/ss4746" target="_blank">Grading</a></td></tr></table>