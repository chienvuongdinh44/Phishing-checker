from urllib.parse import urlparse
import socket
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

    return score




print(check_url("http://example.com"))