#🤖 catFactsTest 🐱
Add the Cat Facts Reverse Turing Test to your Twitter Bots.<br/>
- If a user asks your bot some variation of "Are you a bot?" or "Are you a human?" A brief (mostly one sided) Cat Facts conversation will begin at one point prompting the user for verification they are human...
- It tracks state of conversation per username.
- Does not actually deliver hourly/weekly/yearly Cat Facts<br/>

Working example can be seen here: [@pixelswami](https://twitter.com/pixelswami)

Usage Notes:<br/>
  Import the function to your script.<br/>
`from catfacts import catFactsTest`

```
catfact = catFactsTest(mention,username,USERNAME)
        if catfact != "nope":
                s = api.update_status(status="@"+ username + " " + catfact ,in_reply_to_status_id=mentionid)
        else:
                # Do other stuff your bot normally does here
```
  
  The function requires three paramenters:<br/>
1. `mention` - this is the text of the mention to look at.<br/>
2. `username` - `screen_name` from mention.<br/>
3. `USERNAME` - `@screen_name` of the bot.<br/>
    
This is an homage to [a post](https://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was) on reddit via a botALLY slack discussion.  
