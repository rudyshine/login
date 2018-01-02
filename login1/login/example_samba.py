from smb.SMBConnection import SMBConnection
from smb import smb_constants

conn = SMBConnection('deploy', 'deploy', '', '', use_ntlm_v2=True)
conn.connect('10.51.111.9', 139)

data_path = "E:/test"

def search_folder(i,f = None):
    if f == None:
        filename = ""
    else:
        filename = f.filename
    if i.name != "IPC$":
        print("directory:" + i.name)
        files = conn.listPath(i.name, "/" + filename, smb_constants.SMB_FILE_ATTRIBUTE_DIRECTORY)
        for f in files:
            filename = f.filename
            if filename.startswith(".") == False and filename.endswith((".pdf", ".doc", "docx", "xls", ".txt", ".ppt",".xlsx",".pptx"))== True and f!=None:
                file_obj = open(data_path + '/' + f.filename, 'wb')
                conn.retrieveFile(i.name, f.filename, file_obj)

def samba_search():
    sharelist = conn.listShares()#列出共享目录
    for i in sharelist:
        search_folder(i)

        # file_obj = open('e:/test_samba2017011922.txt', 'wb')
        # file_attributes, filesize = conn.retrieveFile('docs', 'test_samba20170119.txt', file_obj)
        # file_obj.close()

def search_file():
    root_path = ""


if __name__ == '__main__':
    samba_search()