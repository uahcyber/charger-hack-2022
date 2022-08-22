# web / Secret Email

This challenge used smtplib to send an email to a user as long as their email ended in `c00lblu3h4x0r.gov`. Because it is fairly difficult to get a `.gov` email, especially in just 2 days, there had to be some web exploitation. 

If someone was able to solve this challenge by registering that domain name, please contact me. 

The intended solution was to use the [SMTP RFC](https://www.rfc-editor.org/rfc/rfc2821) against the challenge. Knowing that a "to" address can include any text + `<email@domain.com>` as the actual email, a player can exploit the web challenge by inputting an email like this: `<myemail@gmail.com>@c00lblu3h4x0r.gov`. 

This challenge was based off of a previous exploit one of our club members conducted against our [Discord bot](https://github.com/uahcyber/cyberbot). The bot was improperly validating university email addresses, using a method identical to the one in this challenge. Wormy's bypass was using the bracket method above. 