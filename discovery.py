def recursiveFollow(browser, domain, url, listLinks, maxDepth, currentDepth):
    if currentDepth == maxDepth:
        return

    if url.find("logout") == -1 and url.find(".pdf") == -1:
        browser.open(url)

    listLinkHrefs = browser.links()

    externals = browser.links(target="_blank")
    for ext in externals:
        listLinkHrefs.remove(ext)

    for i in listLinkHrefs:
        href = i.get("href")
        if href != "." and href[0] != "." and href[0] != "/" and href.find("http") == -1:
            if href[0] == "?" and url.find("?") == -1:
                if url + href not in listLinks:
                    listLinks.append(url + href)

            elif domain + "/" + href not in listLinks:
                listLinks.append(domain + "/" + href)

    return listLinks


def discoverLinks(browser, url):
    listLinkHrefs = browser.links()
    externals = browser.links(target="_blank")
    listLinks = []
    for ext in externals:
        listLinkHrefs.remove(ext)

    for i in listLinkHrefs:
        if i.get("href") == ".":
            listLinks.append(url)
        else:
            listLinks.append(url + "/" + i.get("href"))

    # if listLinks[0][28] == ".":
    #     listLinks[0] = listLinks[0][:27]

    for each in listLinks:
        recursiveFollow(browser, url, each, listLinks, 10, 0)

    return listLinks
