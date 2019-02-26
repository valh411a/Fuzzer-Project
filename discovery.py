def discoverLinks(browser, url):
    listLinks = browser.links()
    externals = browser.links(target="_blank")
    for ext in externals:
        listLinks.remove(ext)

    for i in listLinks:
        print(url + "/" + i.get("href"))
