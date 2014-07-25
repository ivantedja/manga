import urllib
import json
import os

# doc reference: https://www.mangaeden.com/api/

# variables

# manga info api url, see documentation
mangainfo_api_url = "https://www.mangaeden.com/api/manga/"
# manga info api url, see documentation
chapterinfo_api_url = "https://www.mangaeden.com/api/chapter/"
# manga id, can be retrieved by checking the web page's source code
manga_id = '4e70e9efc092255ef7004251'
# image prefix
img_prefix = 'https://cdn.mangaeden.com/mangasimg/'
# directory prefix for downloaded images
dir_prefix = 'download/'
# to start download from specific chapter
start_from_chapter = 30

api_mangainfo = urllib.urlopen(mangainfo_api_url + manga_id + "/")
json_mangainfo = api_mangainfo.read()
list_mangainfo = json.loads(json_mangainfo)

# hardcode manga title
manga_title = list_mangainfo['title']

# create manga directory if not exist yet
if not os.path.exists(dir_prefix + manga_title):
    os.makedirs(dir_prefix + manga_title)

# iterate chapters, it is in a reversed order
for mangainfo in reversed(list_mangainfo['chapters']):

    # get chapter #
    chapter_number = mangainfo[0]

    # skip un-needed chapter
    if chapter_number < start_from_chapter:
        continue

    # create chapter directory if not exist yet
    if not os.path.exists(dir_prefix + str(manga_title) + '/' + str(chapter_number)):
        os.makedirs(dir_prefix + str(manga_title) + '/' + str(chapter_number))

    # array index [3] = chapter id. see documentation
    api_chapterinfo = urllib.urlopen(chapterinfo_api_url + mangainfo[3])
    json_chapterinfo = api_chapterinfo.read()
    list_chapterinfo = json.loads(json_chapterinfo)

    # iterate images, it is in a reversed order
    for chapterinfo in reversed(list_chapterinfo['images']):

        # get image #
        image_number = chapterinfo[0]

        # array index [3] = image url. see documentation
        image_url = img_prefix + str(chapterinfo[1])

        # retrieve image extension
        image_extension = os.path.splitext(image_url)[1]

        # image name = chapter number + image number + extension
        image_name = str(chapter_number).zfill(4) + str(image_number).zfill(3) + image_extension

        print image_url + ' : image ' + image_name

        # download image = download/[Manga Title]/[Chapter #]/[Image Name]
        urllib.urlretrieve(image_url, dir_prefix + manga_title + '/' + str(chapter_number) + '/' + image_name)