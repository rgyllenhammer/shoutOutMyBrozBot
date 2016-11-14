from __future__ import print_function
import tweepy
import time


ckey = "zBP1UegoKIMi3Swwr3L859D5h"
csecret = "JzSXepx7VZHygL8RpRG17okUsw8NtDk72wNjPS1b02FEEHB1ar"
asecret = "A8Ij8pmsqQJfcwoXd8HHmuo82oqLEIKSZhsll8qpHmJiE"
atoken = "773297630839316480-yx91y4bX6nXlQINxtmXgiNNlRaLWX5Z"

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)

initialUser = "reesegyll"

friendsToTag = []

try:
	user = api.get_user(initialUser)
except tweepy.TweepError:
	print("An error has occured, (probably rate limiting), sleeping is commenced")
	time.sleep(15*60)
	pass

try:
	initialFriends = user.friends()
except tweepy.TweepError:
	print("An error has occured, (probably rate limiting), sleeping is commenced")
	time.sleep(15*60)
	pass


friendLimit = 0

for friend in initialFriends:
	if friendLimit < 20:
		if friend.screen_name != ("shoutOutMyBroz" or "reesesTrumpBot"):
			friendsToTag.append(friend.screen_name)
			friendLimit += 1
		else:
			continue

print(friendsToTag)

print("""

	********
	********
	********
	********
	********
	********


	""")



for tagger in friendsToTag[0:len(friendsToTag)-1]:
	a = 0
	shoutOutList = []
	try:
		newUser = api.get_user(tagger)
		newUserFriends = newUser.friends()
		for secondFriend in newUserFriends:
			if secondFriend.protected != True:
				if a < 5:
					shoutOutList.append("@"+secondFriend.screen_name)
					a += 1
			else:
				continue

		stringOfUsers = ', '.join(shoutOutList)
		api.update_status(stringOfUsers+"... follow my mans @"+initialUser)
		time.sleep(60 * 5)

	except tweepy.TweepError:
		print("An error has occured, (probably rate limiting), sleeping is commenced")
		time.sleep(15*60)
		pass


	
		





	


