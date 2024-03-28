def router(path:str, page):
        match path:
            case '/':
                return page[0]()
            case '/page2':
                return page[1]()