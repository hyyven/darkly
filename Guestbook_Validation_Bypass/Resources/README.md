# Guestbook exploit
- Go to the `/?page=feedback` page.
- In devtools, in the `<input>` tag that is the submit button, replace `onclick="return checkForm();"` by `onclick="return true;"`.
- Enter a name and a message and send it.
- Et voila !