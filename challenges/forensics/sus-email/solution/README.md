[https://www.trendmicro.com/en_us/research/17/e/rising-trend-attackers-using-lnk-files-download-malware.html](https://www.trendmicro.com/en_us/research/17/e/rising-trend-attackers-using-lnk-files-download-malware.html)

- The target property of lnk files is only 260 characters long. Anything longer will not be visible from the properties panel.
- The maximum length for a command line argument is 4096 characters long, however.
- The attacker can pad several spaces to make it more difficult to determine what they are doing.

- Solution:
	- Use exiftool or Eric Zimmerman's [LECmd](https://github.com/EricZimmerman/LECmd) tool to see the hidden base64 encoded powershell command
	- Decode the Base64 to get the flag
