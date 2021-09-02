import os
from collections import Counter, OrderedDict

search_path = '.'
file_type = '.txt'
search_str = 'Sweet'

def tag_search(): #Correction поисправлял регистр функций tag_search и tag_search_helper
    deftags = ['%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%', '%%%%%%%%%%']
    tags = input('Enter up to six tags separated by space: ') #Correction Separated by space
    tags = tags.split(' ')
    tags.extend(deftags)
    tags = tags[:6]
    search_path = '.'
    file_type = '.txt'
    flist = []

    if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"

    for fname in os.listdir(path = search_path):
        if fname.endswith(file_type):
            fo = open(search_path + fname)
            line = fo.readline()
            flist = tag_search_helper(tags[0], flist, fname, line)
            flist = tag_search_helper(tags[1], flist, fname, line)
            flist = tag_search_helper(tags[2], flist, fname, line)
            flist = tag_search_helper(tags[3], flist, fname, line)
            flist = tag_search_helper(tags[4], flist, fname, line)
            flist = tag_search_helper(tags[5], flist, fname, line)
            fo.close()

    result = Counter(flist)
    result = OrderedDict(result.most_common()) #Correction Добавил сортировку через OrderedDict
    if not result:
        return 'No match!'
    else:
        print("Matches in Files:")
        for key, value in result.items():
            print(f'{value} : {key}')
    return 'Sorted in descending order'


def show_all_tags():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    taglist = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for filename in files:
        try:
            with open(os.path.join(__location__, filename), encoding='utf-8') as currentFile:
                text = currentFile.readlines()
                # Note we're looking for in the thrid line, lowercase
                temp = (text[0].lower()).split(' ')
                for i in temp:
                    if i.startswith('#'):
                        taglist.append(i.strip())  
        except:
            pass
    result = sorted(list(set(taglist)))
    resstr = " ".join(result) #Correction убрал лишнюю строку
    print('Please see the list of all available tags below:')
    return(resstr) #Correction change from print to return