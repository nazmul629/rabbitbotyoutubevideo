import praw

reddit = praw.Reddit(
    client_id="Sptks_DFR3nKjgcFXcqR7w",
    client_secret="jQ04FqUULH6t3q17gQodh4Zw6CfWyA",
    password="k/c/Si(rZB74DgZ",
    user_agent="testscript by /u/nazmul629",
    username="nazmul629",
)
# print(reddit.user.me())
print(reddit.read_only) 

subreddits = ["AdvertiseYourVideos","YouTube_startups","SmallYoutuberArmy"]

# subreddits = ["SelfPromotionYoutube", "Youtubeviews", "videos","YouTubePromoter","SubscribeToMe", "YoutubeSelfPromotion",'shamelessplug','YouTubeSubscribeBoost',"industrialized","GetMoreViewsYT","SmallYoutubers","madeinpython","coding","girlsgonewired","codeprojects",'programming']

title = "# 0.2 The Roles Of HTML & CSS In Web Development | |  Modern Web Design"
link = "https://www.youtube.com/watch?v=Jfrp1R_iQn4"



for subreddit in subreddits:
    print(subreddit)
    reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)
   