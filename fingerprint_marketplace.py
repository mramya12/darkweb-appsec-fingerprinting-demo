import hashlib
from bs4 import BeautifulSoup

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def dom_fingerprint(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    tags = [tag.name for tag in soup.find_all()]
    dom_signature = "-".join(tags[:50])
    return hashlib.md5(dom_signature.encode()).hexdigest()

def compare(fp1, fp2):
    return fp1 == fp2

if __name__ == "__main__":
    site_a = "dataset/marketA/index.html"
    site_b = "dataset/marketB/index.html"

    fp_a = dom_fingerprint(site_a)
    fp_b = dom_fingerprint(site_b)

    print("Market A fingerprint:", fp_a)
    print("Market B fingerprint:", fp_b)

    if compare(fp_a, fp_b):
        print("Potential template reuse detected")
    else:
        print("Different templates")
