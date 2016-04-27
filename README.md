# 🤖 catFactsTest 🐱
Cat Facts Reverse Turing Test for Bots.<br/>
- Strictly or entertainment purposes only, not for use in <i>actually</i> identifying humans!
- Does not actually deliver hourly/weekly/yearly Cat Facts<br/>

Working example can be seen here: <a href="https://twitter.com/dad_libs">@dad_libs</a>

Usage Notes:<br/>
  Add library to your script.<br/>
`from catfacts import *`
```
catfact = catFactsTest(mention,username,USERNAME)
        if catfact != "nope":
                s = api.update_status(status="@"+ username + " " + catfact ,in_reply_to_status_id=mentionid)
```
  
  The function requires three paramenters:<br/>
1. `mention` - this is the text of the mention to look at.<br/>
2. `username` - `screen_name` from mention.<br/>
3. `USERNAME` - `@screen_name` of the bot.<br/>
    
This is an homage to <a href="https://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was">a post</a> on reddit via a botALLY slack discussion.  
