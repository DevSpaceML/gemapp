import instaloader

L = instaloader.Instaloader()
username = "shamisobeach"
password = "F@lc0nC0ll3g3!"

#maintain stack of instagram accounts to circumvent rate limits. track time of call and create variable, nextAvailableCall

try:
    L.load_session_from_file(username)
except FileNotFoundError:
    L.login(username, password)
    L.save_session_to_file()

profile = instaloader.Profile.from_username(L.context, "kumbalodge")

for post in profile.get_posts(): 
    print(post)
    print('-----------------------------')



''' 
print("Username:", profile.username)
print("Full Name:", profile.full_name)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Bio:", profile.biography)
print("Website:", profile.external_url)
'''


