# Reflection

Student Name:  Jiya Sharma
Sudent Email:  jsharma@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

This assignment helped me realize how much deeper my understanding of Python scripting and data extraction needs to go—especially when integrating with external services like Google Sheets and web scraping tools like pandas.read_html. I learned how to load survey data directly from a public Google Sheet using a CSV export link, extract the year from timestamps using a custom function, and scrape cost of living tables for different years from Numbeo. These are valuable skills that blend API usage, web scraping, and data wrangling.

One area where I initially struggled was understanding how Streamlit behaves differently when run as a script versus when executed through its intended interface (streamlit run). I got repeated warnings about missing ScriptRunContext, which I learned happens when trying to use Streamlit interactively without launching the app properly. Knowing that I must run streamlit run from the command line in the correct folder, and not just python filename.py, was an important lesson about how Streamlit’s runtime environment works.

I also encountered confusion around file paths and terminal behavior. Even though I knew the file existed, I saw “file does not exist” errors. This helped me better understand how relative vs absolute paths work in the terminal, and how important it is to cd into the correct directory. I also became more aware of subtle issues like hidden characters or case sensitivity in filenames—things that can go wrong silently if you aren’t paying attention.

While I successfully used pandas and read_html, I still need more practice with exception handling and debugging in scripts that automate web or file tasks. For example, my script could break if the Numbeo table layout changes or if the Google Sheet link is revoked. I want to learn how to make these scripts more robust by using try/except blocks, checking for valid HTML structure, and giving clearer error messages.

Next, I plan to revisit how Streamlit apps are structured so I can move this code from a raw script into an actual app layout using st.title(), st.write(), and other components. I also want to better understand the role of caching and user inputs within Streamlit, which will help me build more interactive data tools in the future.

Overall, this assignment pushed me to debug more independently and understand how tools like Streamlit and pandas work together to process and present data. It was a real-world challenge that forced me to bridge scripting, data science, and web development.