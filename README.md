# catFactsTest
##############
Cat Facts Reverse Turing Test for Bots.</br>
*Strictly or entertainment purposes only, not for use in <i>actually</i> identifying humans!

Usage Notes:</br>
  Add library to your script.
    `from catfacts import *`
    
    catfact = catFactsTest(mention,username,USERNAME)
                if catfact != "nope": # It will return nope unless they ask if its a bot or human.
                        s = api.update_status(status="@"+ username + " " + catfact ,in_reply_to_status_id=mentionid)
  
  The function requires three paramenters:</br>
    1. mention - this is the text of the mention to look at.
    2. username - `screen_name` from mention.
    3. USERNAME - `@screen_name` of the bot.
    
This is an homage to <a href="https://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was">a post</a> on reddit via a botALLY slack discussion.
