try:
    from pytube import YouTube
except ImportError:
    import os,sys
    print(sys.exec_prefix+'\\python -m pip install pytube')
    os.system(sys.exec_prefix+'\\python.exe -m pip install pytube')
    from pytube import YouTube
inp=input('video(s)> ').split('\n')
if len(inp)==1:
    inp=inp[0].split('|')
for i in inp:
    y=YouTube(i)
    print('downloading',i,y.title)
    try:
        q=y.streams.filter(file_extension="mp4",resolution='1080p').all()[0]
        print('now')
        q.download()
    except IndexError:
        err=True
        r=1080
        while err:
            err=False
            try:
                r=r-1
                q=y.streams.filter(file_extension="mp4",resolution=str(r)+'p').all()[0]
                print('now')
                q.download()
            except:
                err=True
