import requests
import zipfile
import re
def pythonchallenge6(url):
    page = requests.get(url)
    information = page.text
    return information
    #we find the hint <!-- <-- zip -->

result = pythonchallenge6('http://www.pythonchallenge.com/pc/def/channel.html')
#print(result)

#change url end to zip

def pythonchallenge6_1(path):
    with zipfile.ZipFile(path, "r") as zip:
        for file_name in zip.namelist():
            with zip.open(file_name) as file:
                if b'Next nothing is' in file.read():
                    continue
                else:
                    print(zip.open(file_name).read(), file_name)


                # b'Collect the comments.' 46145.txt
                #start from start from 90052

file = pythonchallenge6_1('channel.zip')


def pythonchallenge6_2(path):
    start = '90052'
    comments = []
    with zipfile.ZipFile(path, "r") as zip_ref:
        while True:
            filename = start + ".txt"
            number = zip_ref.read(filename).decode("utf-8")
            comments.append(zip_ref.getinfo(filename).comment.decode('utf-8'))
            next_nums = re.findall(r'[0-9]+', number)
            if len(next_nums) == 0:
                break
            start = next_nums[0]
        print("".join(comments))


pythonchallenge6_2("channel.zip")

def pythonchallenge6_3(url):
#www.pythonchallenge.com/pc/def/hockey.html
    page = requests.get(url)
    information = page.text
    return information
    # we got: it's in the air. look at the letters.
    #right answer is oxygen



result = pythonchallenge6_3('http://www.pythonchallenge.com/pc/def/hockey.html')
print(result) #http://www.pythonchallenge.com/pc/def/oxygen.html
