from instapy import InstaPy
import pandas as pd


class Instagram():
    def __init__(self):
        self.accounts = []
        self.tags = []

    def getUserPass(self, fileName):
        file = open(fileName, "r")
        content = file.read()
        file.close()
        self.username = content.split('user=', 1)[1].split('pass=', 1)[0].strip()
        self.password = content.split('pass=', 1)[1].strip()

    def extractElements(self, fileName):
        file = open(fileName, "r")
        content = file.read()
        file.close()
        data = []
        while True:
            try:
                element = content.split('\n', 1)[0].strip()
                content = content.split('\n', 1)[1].strip()
                data.append(element)
            except:
                element = content
                data.append(element)
                break
        return pd.DataFrame(data, columns=['name'])


if __name__ == "__main__":
    insta = Instagram()
    insta.getUserPass('pass.txt')
    insta.tags = insta.extractElements('tags.txt')
    session = InstaPy(username=insta.username, password=insta.password)
    session.login()
    # session.like_by_tags(insta.tags['name'], amount=5)
    session.like_by_tags(["پسته"], amount=5)
    session.set_dont_like(["naked", "nsfw"])
