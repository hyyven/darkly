# Cookie exploit
- In the Application section of the Chrome dev tools, we see a cookie named `I_am_admin` containing the following value: `68934a3e9455fa72420237eb05902327`.
- This is an md5 encrypted value. When decrypted, it is the string `false`.
- So we can encrypt the string `true` and manually replace the cookie's value with the result: `b326b5062b2f0e69046810717534cb09`.
- After this, reloading the page will give an alert with the flag.
