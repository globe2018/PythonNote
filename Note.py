PYTHON 写入list并换行的方法
f.writelines(lists) 是不换行的写入，可用以下方法在写入时换行。

方法一：
for line in lists:
f.write(line+'\n')

方法二：
lists=[line+"\n" for line in lists]
f.writelines(lists)

方法三：
f.write('\n'.join(lists))


##############################
##############################

def get_name(*names): # *names參數中的星號會讓python建立一個名字為names的空多元組
    for name in names:
        print("hello,"+name)
    
get_name("bonny","steven")
get_name("jack")
get_name("rose","john","jane")


兩個星號(建立空字典)
範例如下 :

def users(first_name,last_name,**user_info): # **user_info參數中的星號會讓python建立一個名字為user_info的空字典
    user={}  
    user["first"]=first_name # 將first_name新增至user字典
    user["last"]=last_name # 將last_name新增至user字典
    for key,value in user_info.items(): # 用迴圈遍訪user_info裡的鍵值對並將其新增至user字典
        user[key]=value
    return user
    
user1=users("bonny","chang",city="taipei")
print(user1)
user2=users("steven","chang",city="taoyuan")
print(user2)


https://ithelp.ithome.com.tw/articles/10203722?sc=iThelpR
 
 
##############################
##############################
python中對檔案、資料夾（檔案操作函式）的操作需要涉及到os模組和shutil模組。

得到當前工作目錄，即當前Python指令碼工作的目錄路徑: os.getcwd()

返回指定目錄下的所有檔案和目錄名:os.listdir()

函式用來刪除一個檔案:os.remove()

刪除多個目錄：os.removedirs（r“c：\python”）

檢驗給出的路徑是否是一個檔案：os.path.isfile()

檢驗給出的路徑是否是一個目錄：os.path.isdir()

判斷是否是絕對路徑：os.path.isabs()

檢驗給出的路徑是否真地存:os.path.exists()

返回一個路徑的目錄名和檔名:os.path.split() eg os.path.split(‘/home/swaroop/byte/code/poem.txt’) 結果：(‘/home/swaroop/byte/code’, ‘poem.txt’)

分離副檔名：os.path.splitext()

獲取路徑名：os.path.dirname()

獲取檔名：os.path.basename()

執行shell命令: os.system()

讀取和設定環境變數:os.getenv() 與os.putenv()

給出當前平臺使用的行終止符:os.linesep Windows使用’\r\n’，Linux使用’\n’而Mac使用’\r’

指示你正在使用的平臺：os.name 對於Windows，它是’nt’，而對於Linux/Unix使用者，它是’posix’

重新命名：os.rename（old， new）

建立多級目錄：os.makedirs（r“c：\python\test”）

建立單個目錄：os.mkdir（“test”）

獲取檔案屬性：os.stat（file）

修改檔案許可權與時間戳：os.chmod（file）

終止當前程序：os.exit（）

獲取檔案大小：os.path.getsize（filename）

檔案操作：
os.mknod(“test.txt”) 建立空檔案
fp = open(“test.txt”,w) 直接開啟一個檔案，如果檔案不存在則建立檔案

關於open 模式：

w 以寫方式開啟，
a 以追加模式開啟 (從 EOF 開始, 必要時建立新檔案)
r 以讀寫模式開啟
w 以讀寫模式開啟 (參見 w )
a 以讀寫模式開啟 (參見 a )
rb 以二進位制讀模式開啟
wb 以二進位制寫模式開啟 (參見 w )
ab 以二進位制追加模式開啟 (參見 a )
rb 以二進位制讀寫模式開啟 (參見 r )
wb 以二進位制讀寫模式開啟 (參見 w )
ab 以二進位制讀寫模式開啟 (參見 a )

fp.read([size]) #size為讀取的長度，以byte為單位

fp.readline([size]) #讀一行，如果定義了size，有可能返回的只是一行的一部分

fp.readlines([size]) #把檔案每一行作為一個list的一個成員，並返回這個list。其實它的內部是通過迴圈呼叫readline()來實現的。如果提供size引數，size是表示讀取內容的總長，也就是說可能只讀到檔案的一部分。

fp.write(str) #把str寫到檔案中，write()並不會在str後加上一個換行符

fp.writelines(seq) #把seq的內容全部寫到檔案中(多行一次性寫入)。這個函式也只是忠實地寫入，不會在每行後面加上任何東西。

fp.close() #關閉檔案。python會在一個檔案不用後自動關閉檔案，不過這一功能沒有保證，最好還是養成自己關閉的習慣。 如果一個檔案在關閉後還對其進行操作會產生ValueError

fp.flush() #把緩衝區的內容寫入硬碟

fp.fileno() #返回一個長整型的”檔案標籤“

fp.isatty() #檔案是否是一個終端裝置檔案（unix系統中的）

fp.tell() #返回檔案操作標記的當前位置，以檔案的開頭為原點

fp.next() #返回下一行，並將檔案操作標記位移到下一行。把一個file用於for … in file這樣的語句時，就是呼叫next()函式來實現遍歷的。

fp.seek(offset[,whence]) #將檔案打操作標記移到offset的位置。這個offset一般是相對於檔案的開頭來計算的，一般為正數。但如果提供了whence引數就不一定了，whence可以為0表示從頭開始計算，1表示以當前位置為原點計算。2表示以檔案末尾為原點進行計算。需要注意，如果檔案以a或a 的模式開啟，每次進行寫操作時，檔案操作標記會自動返回到檔案末尾。


 
fp.truncate([size]) #把檔案裁成規定的大小，預設的是裁到當前檔案操作標記的位置。如果size比檔案的大小還要大，依據系統的不同可能是不改變檔案，也可能是用0把檔案補到相應的大小，也可能是以一些隨機的內容加上去。

目錄操作：
os.mkdir(“file”) 建立目錄
複製檔案：
shutil.copyfile(“oldfile”,”newfile”) oldfile和newfile都只能是檔案
shutil.copy(“oldfile”,”newfile”) oldfile只能是資料夾，newfile可以是檔案，也可以是目標目錄
複製資料夾：
shutil.copytree(“olddir”,”newdir”) olddir和newdir都只能是目錄，且newdir必須不存在
重新命名檔案（目錄）
os.rename(“oldname”,”newname”) 檔案或目錄都是使用這條命令
移動檔案（目錄）
shutil.move(“oldpos”,”newpos”)
刪除檔案
os.remove(“file”)
刪除目錄
os.rmdir(“dir”)只能刪除空目錄
shutil.rmtree(“dir”) 空目錄、有內容的目錄都可以刪
轉換目錄
os.chdir(“path”) 換路徑

Python讀寫檔案

1.open
使用open開啟檔案後一定要記得呼叫檔案物件的close()方法。比如可以用try/finally語句來確保最後能關閉檔案。

file_object = open(‘thefile.txt’)
try:
all_the_text = file_object.read( )
finally:
file_object.close( )


 
注：不能把open語句放在try塊裡，因為當開啟檔案出現異常時，檔案物件file_object無法執行close()方法。

2.讀檔案
讀文字檔案
input = open(‘data’, ‘r’)
#第二個引數預設為r
input = open(‘data’)

讀二進位制檔案
input = open(‘data’, ‘rb’)

讀取所有內容
file_object = open(‘thefile.txt’)
try:
all_the_text = file_object.read( )
finally:
file_object.close( )

讀固定位元組
file_object = open(‘abinfile’, ‘rb’)
try:
while True:
chunk = file_object.read(100)
if not chunk:
break
do_something_with(chunk)
finally:
file_object.close( )

讀每行
list_of_all_the_lines = file_object.readlines( )

如果檔案是文字檔案，還可以直接遍歷檔案物件獲取每行：

for line in file_object:
process line

3.寫檔案
寫文字檔案
output = open(‘data’, ‘w’)

寫二進位制檔案
output = open(‘data’, ‘wb’)

追加寫檔案
output = open(‘data’, ‘w ‘)

寫資料
file_object = open(‘thefile.txt’, ‘w’)
file_object.write(all_the_text)
file_object.close( )

寫入多行
file_object.writelines(list_of_text_strings)

注意，呼叫writelines寫入多行在效能上會比使用write一次性寫入要高。

在處理日誌檔案的時候，常常會遇到這樣的情況：日誌檔案巨大，不可能一次性把整個檔案讀入到記憶體中進行處理，例如需要在一臺實體記憶體為 2GB 的機器上處理一個 2GB 的日誌檔案，我們可能希望每次只處理其中 200MB 的內容。
在 Python 中，內建的 File 物件直接提供了一個 readlines(sizehint) 函式來完成這樣的事情。以下面的程式碼為例：

file = open(‘test.log’, ‘r’)sizehint = 209715200 # 200Mposition = 0lines = file.readlines(sizehint)while not file.tell() – position < 0: position = file.tell() lines = file.readlines(sizehint)


 
每次呼叫 readlines(sizehint) 函式，會返回大約 200MB 的資料，而且所返回的必然都是完整的行資料，大多數情況下，返回的資料的位元組數會稍微比 sizehint 指定的值大一點（除最後一次呼叫 readlines(sizehint) 函式的時候）。通常情況下，Python 會自動將使用者指定的 sizehint 的值調整成內部快取大小的整數倍。

file在python是一個特殊的型別，它用於在python程式中對外部的檔案進行操作。在python中一切都是物件，file也不例外，file有file的方法和屬性。下面先來看如何建立一個file物件：

file(name[, mode[, buffering]])
file()函式用於建立一個file物件，它有一個別名叫open()，可能更形象一些，它們是內建函式。來看看它的引數。它引數都是以字串的形式傳遞的。name是檔案的名字。
mode是開啟的模式，可選的值為r w a U，分別代表讀（預設） 寫 新增支援各種換行符的模式。用w或a模式開啟檔案的話，如果檔案不存在，那麼就自動建立。此外，用w模式開啟一個已經存在的檔案時，原有檔案的內容會被清空，因為一開始檔案的操作的標記是在檔案的開頭的，這時候進行寫操作，無疑會把原有的內容給抹掉。由於歷史的原因，換行符在不同的系統中有不同模式，比如在 unix中是一個\n，而在windows中是‘\r\n’，用U模式開啟檔案，就是支援所有的換行模式，也就說‘\r’ ‘\n’ ‘\r\n’都可表示換行，會有一個tuple用來存貯這個檔案中用到過的換行符。不過，雖說換行有多種模式，讀到python中統一用\n代替。在模式字元的後面，還可以加上 b t這兩種標識，分別表示可以對檔案同時進行讀寫操作和用二進位制模式、文字模式（預設）開啟檔案。
buffering如果為0表示不進行緩衝;如果為1表示進行“行緩衝“;如果是一個大於1的數表示緩衝區的大小，應該是以位元組為單位的。

file物件有自己的屬性和方法。先來看看file的屬性。

closed #標記檔案是否已經關閉，由close()改寫
encoding #檔案編碼
mode #開啟模式
name #檔名
newlines #檔案中用到的換行模式，是一個tuple
softspace #boolean型，一般為0，據說用於print

file的讀寫方法：

F.read([size]) #size為讀取的長度，以byte為單位
F.readline([size])
#讀一行，如果定義了size，有可能返回的只是一行的一部分
F.readlines([size])
#把檔案每一行作為一個list的一個成員，並返回這個list。其實它的內部是通過迴圈呼叫readline()來實現的。如果提供size引數，size是表示讀取內容的總長，也就是說可能只讀到檔案的一部分。
F.write(str)
#把str寫到檔案中，write()並不會在str後加上一個換行符
F.writelines(seq)
#把seq的內容全部寫到檔案中。這個函式也只是忠實地寫入，不會在每行後面加上任何東西。

file的其他方法：

F.close()
#關閉檔案。python會在一個檔案不用後自動關閉檔案，不過這一功能沒有保證，最好還是養成自己關閉的習慣。如果一個檔案在關閉後還對其進行操作會產生ValueError
F.flush()
#把緩衝區的內容寫入硬碟
F.fileno()
#返回一個長整型的”檔案標籤“
F.isatty()
#檔案是否是一個終端裝置檔案（unix系統中的）
F.tell()
#返回檔案操作標記的當前位置，以檔案的開頭為原點
F.next()
#返回下一行，並將檔案操作標記位移到下一行。把一個file用於for … in file這樣的語句時，就是呼叫next()函式來實現遍歷的。
F.seek(offset[,whence])
#將檔案打操作標記移到offset的位置。這個offset一般是相對於檔案的開頭來計算的，一般為正數。但如果提供了whence引數就不一定了，whence可以為0表示從頭開始計算，1表示以當前位置為原點計算。2表示以檔案末尾為原點進行計算。需要注意，如果檔案以a或a 的模式開啟，每次進行寫操作時，檔案操作標記會自動返回到檔案末尾。
F.truncate([size])
#把檔案裁成規定的大小，預設的是裁到當前檔案操作標記的位置。如果size比檔案的大小還要大，依據系統的不同可能是不改變檔案，也可能是用0把檔案補到相應的大小，也可能是以一些隨機的內容加上去。

以上這篇python 讀寫、建立 檔案的方法(必看)就是小編分享給大家的全部內容了，希望能給大家一個參考，也希望大家多多支援指令碼之家。
