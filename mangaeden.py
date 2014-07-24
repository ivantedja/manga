import urllib
import json

# doc reference: https://www.mangaeden.com/api/

# manga info api url, see documentation
mangainfo_api_url = "https://www.mangaeden.com/api/manga/"
# manga info api url, see documentation
chapterinfo_api_url = "https://www.mangaeden.com/api/chapter/"
# manga id, can be retrieved by checking the web page's source code
manga_id = '4e70e9efc092255ef7004251'
# hardcode manga title
manga_title = 'Gantz'
# image prefix
img_prefix = 'https://cdn.mangaeden.com/mangasimg/'
# counter for downloaded image
counter = 1

api_mangainfo = urllib.urlopen(mangainfo_api_url + manga_id + "/")
json_mangainfo = api_mangainfo.read()
list_mangainfo = json.loads(json_mangainfo)

# iterate chapters, it is in a reversed order
for mangainfo in reversed(list_mangainfo['chapters']):

    # array index [3] = chapter id. see documentation
    api_chapterinfo = urllib.urlopen(chapterinfo_api_url + mangainfo[3])
    json_chapterinfo = api_chapterinfo.read()
    list_chapterinfo = json.loads(json_chapterinfo)

    # iterate images, it is in a reversed order
    for chapterinfo in reversed(list_chapterinfo['images']):

        # array index [3] = image url. see documentation
        image_url = img_prefix + str(chapterinfo[1])
        image_name = str(counter).zfill(7) + '.jpg'

        print image_url + ' : image ' + image_name

        # download image
        urllib.urlretrieve(image_url, manga_title + '/' + image_name)

        # increment image counter
        counter = counter + 1