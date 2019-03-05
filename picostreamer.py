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
        q=False
        for st in y.streams.filter(file_extension="mp4",resolution='1080p').all():
            if st.includes_audio_track:
                q=st
                break
        if q:
            print('now')
        q.download()
    except:
        err=True
        r=1080
        while err:
            err=False
            try:
                q=False
                r=r-1
                for st in y.streams.filter(file_extension="mp4",resolution=str(r)+'p').all():
                    if st.includes_audio_track:
                        q=st
                        break
                if q:
                    print('now')
                q.download()
            except:
                err=True
