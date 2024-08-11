def getResponses(valid_auth_tokens, requests):
    res = []
    for request in requests:
        url = request
        params = url[url.find("?") + 1 :]
        token = ""
        csr = ""
        for elon in params.split("&"):
            key, value = elon.split("=")
            if key == "token":
                token = value
            elif key == "csrf":
                csr = value
        if token not in valid_auth_tokens:
            res.append("INVALID")
        elif url.startswith("POST") and (
            not csr or not all(c.isdigit() or c.isalpha() for c in csr) or len(csr) < 8
        ):
            res.append("INVALID")
        else:
            rss = "VALID"
            for elon in params.split("&"):
                key, value = elon.split("=")
                if key != "token" and key != "csrf":
                    rss += f", {key}, {value}"
            res.append(rss)
    return res


def main():
    valid_auth_tokens = ["abc123", "xyz456", "123abc"]
    requests = [
        "http://example.com/api/getData?token=abc123&csrf=987654321&param1=value1&param2=value2",
        "POST http://example.com/api/submitData?token=xyz456&csrf=abcdefgh&param3=value3&param4=value4",
        "http://example.com/api/getDetails?token=123abc&param5=value5&param6=value6",
    ]
    responses = getResponses(valid_auth_tokens, requests)
    for response in responses:
        print(response)


if __name__ == "__main__":
    main()
