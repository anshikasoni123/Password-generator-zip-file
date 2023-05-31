import zipfile
import time

file_path = input('Write your file path : ')
zip_file = zipfile.ZipFile(file_path)
c = 0
result = 0

if not zip_file:
    print('The zipped file/folder is not password protected! You can successfully open it!')
else:
    starttime = time.time()
    wordList = open('wordlist.txt','r',errors = "ignore")
    body = wordList.read().lower()
    words = body.split('\n')
    for i in range(len(words)):
        word = words[i]
        password = word.encode('utf8').strip()
        c = c + 1
        print('Trying to decode password by : {}'.format(word))
        try:
            with zipfile.ZipFile(file_path,'r') as zf:
               zf.extractall(pwd=password)
               print('Success ! the password is : '+word)
               endtime = time.time()
               result = 1
            break
        except:
            pass
        
    if result == 0:
        duration = endtime-starttime
        print('Sorry ! password not found .A total of '+str(c)+' possible combinations tried in ' + str(duration)+ ' seconds. Password is not of 4 characters.')
    else:
        duration = endtime-starttime
        print('Congratulations !!! password found after trying ' + str(c) + ' combinations in ' + str(duration) + ' seconds.')

        
