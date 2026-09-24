from urllib.parse import urlparse
import socket
url_shorteners = ["bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "rebrand.ly",
    "cutt.ly",
    "shorturl.at"]
sus_keywords = ["verify", "login", "secure", "account", "urgent"]
# This takes a string and return a risk score
def check_url(url):
    score = 0
    result = urlparse(url)

    # Check the scheme
    if result.scheme != "https":
        score +=1

    # Check if the netloc is an IP or has an actual name
    try:
        host = result.netloc.split(":")[0]
        socket.inet_aton(host) # This return the Ip packed into bytes if the Ip is valid, if not it raises an exception
        score += 1
    except:
        pass

    # Checking for an excessive number of subdomains - count how many dots appear in the netloc
    # >=3 is suspicious
    if host.count(".") >= 3:
        score += 1

    # Check if they use url shortener
    if host in url_shorteners:
        score += 1

    # Check for the suspicious keywords in the url
    for keyword in sus_keywords:
        if keyword in url.lower():
            score += 1  

    return score

def get_verdict(score):
    if score < 2:
        return "Safe"
    elif  2 <= score <= 3:
        return "Suspicious"
    else: 
        return "Likely Phishing"

def main():
    test_urls = [
        # Safe / legitimate
    "https://www.google.com",
    "https://www.github.com",
    "https://www.bbc.co.uk/news",

    # Suspicious — no HTTPS + keyword
    "http://secure-login-verify.com/account",

    # Suspicious — IP address instead of domain
    "http://192.168.1.1/login",

    # Suspicious — excessive subdomains (mimicking a real brand)
    "http://paypal.com.account.verify.security-check.com/login",

    # Suspicious — URL shortener
    "http://bit.ly/3xample",

    # Suspicious — stacks multiple red flags at once
    "http://192.168.0.5.verify-account.urgent-login.com/secure"
                ]
    for url in test_urls:
        score = check_url(url)
        verdict = get_verdict(score)
        print(f"{url} => score: {score} => verdict: {verdict}")


if __name__ == "__main__":
    main()