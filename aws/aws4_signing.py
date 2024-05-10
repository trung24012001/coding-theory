# AWS Version 4 signing example
#
# Example:
# Authorization: AWS4-HMAC-SHA256 Credential=AKIDEXAMPLE/20150830/us-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=5d672d79c15b13162d9279b0855cfba6789a8edb4c82c400e06b5924a6f2b5d7

# Formulae:
# CanonicalRequest =
#   HTTPRequestMethod + '\n' +
#   CanonicalURI + '\n' +
#   CanonicalQueryString + '\n' +
#   CanonicalHeaders + '\n' +
#   SignedHeaders + '\n' +
#   HexEncode(Hash(RequestPayload))

# EC2 API (DescribeRegions)

# See: http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
# This version makes a GET request and passes the signature
# in the Authorization header.
import sys, os, base64, datetime, hashlib, hmac, binascii
import openvds

# import requests  # pip install requests

# ************* REQUEST VALUES *************
service = "s3"
host = "node3:9000"
region = "vn-north-1"
access_key = "DojZFN4YxfiVMoAEhD7q"
secret_key = "mIT0PCMR3g2HyL29lweSyfJ2TTsvYdWxfv7AbAa8"
amzdate = "20240420T181455Z"
datestamp = "20240420"
expire = "604800"

method = "GET"
canonical_uri = "/vds-demo/Seismic.vds"
canonical_querystring = f"X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential={access_key}%2F{datestamp}%2F{region}%2F{service}%2Faws4_request&X-Amz-Date={amzdate}&X-Amz-Expires={expire}&X-Amz-SignedHeaders=host&Region=vn-north-1"
canonical_headers = "host:" + host + "\n"
signed_headers = "host"
payload_hash = "UNSIGNED-PAYLOAD"

# service = "s3"
# host = "examplebucket.s3.amazonaws.com"
# region = "us-east-1"
# access_key = "AKIAIOSFODNN7EXAMPLE"
# secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
# amzdate = "20130524T000000Z"
# datestamp = "20130524"
# expire = "86400"

# method = "GET"
# canonical_uri = "/test.txt"
# canonical_querystring = f"X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential={access_key}%2F{datestamp}%2F{region}%2F{service}%2Faws4_request&X-Amz-Date={amzdate}&X-Amz-Expires={expire}&X-Amz-SignedHeaders=host"
# canonical_headers = "host:" + host + "\n"
# signed_headers = "host"
# payload_hash = "UNSIGNED-PAYLOAD"


# Key derivation functions. See:
# http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning


# Step 7: Combine elements to create create canonical request
canonical_request = (
    method
    + "\n"
    + canonical_uri
    + "\n"
    + canonical_querystring
    + "\n"
    + canonical_headers
    + "\n"
    + signed_headers
    + "\n"
    + payload_hash
)


# ************* TASK 2: CREATE THE STRING TO SIGN*************
# Match the algorithm to the hashing algorithm you use, either SHA-1 or
# SHA-256 (recommended)
algorithm = "AWS4-HMAC-SHA256"
credential_scope = datestamp + "/" + region + "/" + service + "/" + "aws4_request"

string_to_sign = (
    algorithm
    + "\n"
    + amzdate
    + "\n"
    + credential_scope
    + "\n"
    + hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
)

# ************* TASK 3: CALCULATE THE SIGNATURE *************
# Create the signing key using the function defined above.
signing_key = getSignatureKey(secret_key, datestamp, region, service)

# Sign the string_to_sign using the signing_key
signature = hmac.new(
    signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256
).hexdigest()

print(string_to_sign)
print(binascii.b2a_hex(signing_key))
print(signature)
