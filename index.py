import pandas as pd

# Define the file path
file_path = "E:\Projects\Time Pass\Blood Donation\data.csv"

data = pd.read_csv(file_path)

phone_numbers = data["Mobile Number"].tolist()
names = data["full_name"].tolist()

prefix = f"https://wa.me/"


def generateUrl(i):
    url = f"{prefix}91{int(phone_numbers[i])}?text=Hello *Mr./Ms./Mrs . {names[i].title()}*, I am from Blood Donation Organising Committee. As you have enrolled to donate blood via google form, I am giving you a gentle reminder that tomorrow we have the Blood Donation Camp%0aThe timings are from morning *10 AM to 2 PM*. The venue for the same is Workshop building of *Government Polytechnic Daman*.%0aI request you to bring your Aadhar card for registration process.%0aI request your presence for this social cause and make this event a success.%0aThank you"
    url = url.replace(" ", "+")
    return url


generatedHTML = ""
for i in range(len(phone_numbers)):
    url = generateUrl(i)
    anchorLink = f"<a target='_blank' href='{url}'>Message {int(phone_numbers[i])}: {names[i].title()}</a></br>\n"
    generatedHTML = generatedHTML+anchorLink
file = open("msg.html", "w")

file.write(generatedHTML)
file.close()
