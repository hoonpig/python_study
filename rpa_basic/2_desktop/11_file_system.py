import os
import time
import datetime
import shutil # shell utilities
# print(os.getcwd()) # 현재 작업공간 current working directory
# os.chdir("rpa_basic") # 작업공간이동
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("c:/")
# print(os.getcwd())

#파일경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt") # 절대경로 생성
# open(file_path,...)

# 파일경로에서 폴더정보 가져오기
#print(os.path.dirname(r"D:\python_workspace\my_file.txt")) # r은 문자 그래도 read, \ 가 있어도 개행처리를 안한다.

# 파일정보 가져오기

# test_file_path = "rpa_basic/2_desktop/11_file_system.py"

# # 파일의 생성날자
# ctime = os.path.getctime(test_file_path)
# print(ctime)
# # 날자정보를 strftime 을 통해 년월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%y%m%d %H:%M:%S"))

# #파일의 수정날자
# mtime = os.path.getmtime(test_file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%y%m%d %H:%M:%S"))

# #파일의 접근날자
# atime = os.path.getatime(test_file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%y%m%d %H:%M:%S"))

# #파일크기
# fsize = os.path.getsize(test_file_path)
# print(fsize)

# 파일목록 가져오기
#print(os.listdir()) # 모든 정보 파일정보 목록 가져오기
#print(os.listdir("rpa_basic"))

#파일목록 가져오기(하위폴더 포함)
# result = os.walk("rpa_basic") # 주어진 폴더 밑에있는 모든 폴더와 파일목록 가져오기
# for root,dirs,files in result:
#     print(root,dir,files)

# 특정폴더 내애세 특정 파일 찾기
# name = "11_file_system.py"
# result =[]
# for root,dirs,files in os.walk("."):
#     if name in files:
#         result.append(os.path.join(root,name))

# print(result)

# 폴더내 특정 패턴을 가진 파일을 찾기
# import fnmatch
# pattern = "*.py" #.py 로  끝나는 모든 파일
# result = []
# for root,dirs,files in os.walk("."):
#     for names in files:
#         if fnmatch.fnmatch(names, pattern):
#             result.append(os.path.join(root, names))

# print(result)


# 주어진 경로가 파일, 폴더 여부 판단
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic"))
# print(os.path.isdir("run_button.png"))
# print(os.path.isfile("run_button.png"))

# if os.path.exists("rpa_basic"):
#     print("파일또는 폴더가 존재합니다.")
# else : 
#     print("존재하지않음")


# 파일만들기
#open("new_file.txt","a").close()

#파일명 변경하기
#os.rename("new_file.txt","new_file_rename.txt")

#파일삭제
#os.remove("new_file_rename.txt")

#폴더생성
#os.mkdir("new_folder") # 현재경로 기준으로 폴더 생성
# 여러경로 만들때는 os.makedirs 를 사용

#폴더명 변경하기
#os.rename("new_folder", "new_folder_rename")

# 폴더 삭제
#os.rmdir("new_folder_rename")
# shutil.rmtree("")  폴더안에 다른파일이 있어도 다전부삭제


# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사
#shutil.copy("run_button.png","test_folder") # 원본파일경로, 대상폴더 경로
#shutil.copy("run_button.png","test_folder/copied_run_btn.png") # 원본 파일경로를 대상경로+파일명 지정

#shutil.copyfile("run_button.png","test_folder/copied_run_btn_2.png") #원본파일경로, 대상파일경로까지 무조건 지정
# copy, copyfile : 메타정보 복사 x
# copy2 메타정보 복사 ㅇ
# #shutil.copy2("run_button.png","test_folder/copy2.png")


#폴더복사
#shutil.copytree("test_folder","test_folder2")
#shutil.copytree("test_folder","test_folder3")

#폴더 이동
#shutil.move("test_folder3","test_folder2") # 폴더 이동
shutil.move("test_folder2","test_folder") # 폴더이동 및 폴더 가 없을경우 rename 효과가 나타난다.
