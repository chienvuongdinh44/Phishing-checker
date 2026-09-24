### Phishing URL Checker

A small Python tool that checks a URL and tells you if it looks Safe, Suspicious, or Likely Phishing.

I built this after doing a Forage simulation with Mastercard's Security Awareness Team, where I worked on spotting and reporting phishing attempts. Wanted to see if I could turn that into something automated.

## How it works

The tool checks a URL against 5 things and adds up a risk score:

- No HTTPS
- Uses a raw IP address instead of a domain (e.g. 192.168.1.1)
- Too many subdomains (e.g. paypal.com.verify.security-check.com)
- Suspicious keywords like "verify", "login", "urgent", "account" — one point per keyword found
- Known URL shorteners (bit.ly, tinyurl, etc.)

Score 0-1 = Safe, 2-4 = Suspicious, 5+ = Likely Phishing.

No single check decides anything on its own — it's the combination that matters, same way you'd actually spot a phishing link in real life.

## Run it
python phishing_checker.py

Runs the test URLs already in the file and prints a score + verdict for each.

## Example
* https://www.google.com => score: 0 => Safe
* http://secure-login-verify.com/account => score: 5 => Likely Phishing
* http://bit.ly/3xample => score: 2 => Suspicious

## Limitations (found these while testing)
- False positives on country domains — www.bbc.co.uk scores a point on the subdomain check just because co.uk adds an extra dot, even though it's a totally normal, legit domain.
- Keyword scoring stacks up — a URL with 3 suspicious keywords gets 3 points, not 1. That's intentional (more scare-words = more suspicious) but it does mean the max score isn't fixed at 5 like you'd expect.
- Shortener list is hardcoded — only catches the ones I listed, so a new or obscure shortener slips through.
- It's rule-based, not smart — no machine learning here, just fixed checks. Won't catch anything that doesn't match these 5 patterns.

## Possibly later
- Fix the country-domain false positive
- Try a basic ML model on a real phishing URL dataset
- Add a Tkinter GUI
- Check email headers too, not just URLs
## Built with
Python 3, urllib.parse, socket
