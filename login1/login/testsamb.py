from smb.SMBConnection import SMBConnection
from smb import smb_constants

##smb连接
conn = SMBConnection('deploy', 'deploy', '', '', use_ntlm_v2=True)
conn.connect('10.51.111.9', 139)
data_path = "E:/test"

##读写文件
def search_folder(share,f = None,path = None):
    if f == None:
        filename = ""
    else:
        filename = f.filename
        # print(filename)
    if path != None:
        path = path + '/' + filename
    else:
        path = "/"
    if share.name != "IPC$":
        print("directory:" + share.name)
        files = conn.listPath(share.name, path, smb_constants.SMB_FILE_ATTRIBUTE_DIRECTORY)
        for f in files:
            fname = f.filename
            if not fname.startswith("."):
                if fname.endswith((".pdf", ".doc", "docx", "xls", ".txt", ".ppt",".xlsx",".pptx",".htm",".html")):
                    file_obj = open(data_path + '/' + fname, 'wb')
                    if path.endswith("/"):
                        t_file = path + fname
                    else:
                        t_file = path + '/' + fname
                    conn.retrieveFile(share.name, t_file, file_obj)
                elif f.isDirectory:
                    search_folder(share,f,path)


def samba_search():
    sharelist = conn.listShares()#列出共享目录
    for i in sharelist:
        search_folder(i)

if __name__ == '__main__':
    samba_search()