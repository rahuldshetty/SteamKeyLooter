import praw,re
r=praw.Reddit(user_agent="AGENT_NAME",client_id="YourClientId",client_secret='YourClientSecret')
finder=re.compile(r'[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}')
finder1=re.compile(r'[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}')
def findKey(text):
    keys=[]
    for x in finder.findall(text):
        if len(x) == 17:
            keys.append(x)
    for x in finder1.findall(text):
       if len(x) == 29: 
            keys.append(x)
    return keys
def getPosts(sub,num):
    postText = []
    print("Getting posts from "+str(sub))
    posts = r.subreddit(sub).new(limit=num)
    for x in posts:
        postText.append(x.selftext.encode('ascii', 'ignore').decode())
    return postText
def getKeys(sub,num):
    #find keys in each posts of a subreddit
    posts = getPosts(sub,num)
    keys = []
    for x in posts:
        keysonsub = findKey(x)
        if len(keysonsub) > 0:
            print("\n".join(keysonsub))
            keys.append(keysonsub)
    return [item for sublist in keys for item in sublist]
def subKeys(subs,num):
    foundKeys=[]
    #get keys in each subreddit
    for sub in subs:
        foundKeys.extend(getKeys(sub,num))
    return foundKeys
subs = ["freegamesonsteam","free","freegiveaways","giftofgames","freegamefindings","randomactsofgaming","all","steam_giveaway"]
keylist=subKeys(subs,100)
with open("keys.txt","a") as keys:
    keys.write("\n".join(keylist))

