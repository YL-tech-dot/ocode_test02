# mymodule LYE
# 코랩 청소기 file, folder 모두 가능.
import os
import shutil

file_path = "E:/Data/Combine/History/test.txt"

def del_file(path):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("해당 경로를 확인해주세요")
# del_file(file_path)


# 파일 이동 + 복사 여부 체크 + 없던 폴더 경로까지 만들어주는 친절한 함수
# from google.colab import drive
# drive.mount('/content/gdrive')


src_path = "/content/sample.py"   # 이동할 파일 경로
dest_path ="/content/firstfolder" # 도착할 폴더 경로


def moveNcopyFile(src_dir, dest_dir):
    print(f'현재 경로 안내 >>> {os.getcwd()}')
    if not os.path.exists(src_dir):
        print(f"os : src_dir 경로에 파일 혹은 폴더가 존재하지 않습니다. \n 입력된 경로 : {src_dir}")
        return
    if not os.path.exists(dest_dir):
        print("os : 새로 경로를 생성하겠습니다. ")
        os.makedirs(dest_dir)

        ###############################################
        os.makedirs(dest_dir, exist_ok=True)
        ###############################################


    # 파일 이동시, 복사 여부 확인
    answer = str(input("복사 후 이동하시겠습니까? (y/n) : "))
    if answer == "Y" or 'y':
        shutil.copyfile( src_dir, os.path.join(dest_dir, os.path.basename(src_dir)))
        print(f"{src_dir} 이 \n {dest_dir}로 복사가 되었습니다.")
    elif answer == 'N' or 'n':
        shutil.move(src_dir, os.path.join(dest_dir, os.path.basename(src_dir)))
        print(f"복사 없이\n{src_dir} 이 \n {dest_dir}로 이동되었습니다.")

# 호출명
moveNcopyFile( src_path , dest_path )

# src path : dict path
path_dict = { "/content/sample.py" : " /contetn/firstfolder",
             "/content/sample.py" : " /contetn/firstfolder",
             "/content/sample.py" : " /contetn/firstfolder",
            }

src_lr = []
def moveNcopyFiles( path_dict : dict ) :
    print(f'현재 경로 안내 >>> {os.getcwd()}')
    src_dir = path_dict.keys()
    dest_dir = path_dict.values()
    willDest_directory_file = os.path.join( dest_dir, os.path.basename(src_dir) )
    # willDest_directory_file = 도착 경로 + 복제 파일 이름
        # 복제될 파일의 경로+이름 = os.path.join() 메소드는 그냥 도착할 경로에 파일명을 더해 경로를 이어주는 역할입니다.
        # os.path.basename("/content/testfolder")  # testfolder
    try:
        for d in dest_dir:
            if not os.path.exists(d):
                os.makedirs(d) # os.makedirs() 경로 만들기 메소드
            else : pass

        answer = str(input("copy and move? (y/n) : "))

        if answer == "y" or "Y":
            # copy and move
            shutil.copyfile( dest_dir , willDest_directory_file )
        if answer == "N" or "n":
            # only move
            shutil.move(dest_dir , willDest_directory_file )

    except OSError as oe:
        print( "", oe)

moveNcopyFiles(path_dict)