# -ExtensionBlurring
 Extension Blurring for Ransomware Protection


Blurring:

Steps:
1) Get OS File Association:
 - Run: python exinout.py --operation export --path C:\\Users\\XXX\\Desktop\\here
 - Result: DefaultAssoc.xml is exported.

2) Generate Extensions:
 - Run: python exgen.py --configure new --path C:\Users\XXX\Desktop\here
 - Result: DefaultAssoc.xml is changed, new_extensions.json is created.

3) Start Blurring:
 - Run: python exwalker.py --setting new --path C:\Users\XXX\Desktop\Test
 - Result: Matched file types are blurred.

4) Set OS File Association:
 - Run: python exinout.py --operation import --path C:\\Users\\XXX\\Desktop\\here
 - Result: DefaultAssoc.xml is imported.


Reverting Blurring:

Steps:
1) Get OS File Association:
 - Run: python exinout.py --operation export --path C:\\Users\\XXX\\Desktop\\here
 - Result: DefaultAssoc.xml is exported.

2) Revert Extensions:
 - Run: python exgen.py --configure old --path C:\Users\XXX\Desktop\here
 - Result: DefaultAssoc.xml is changed.

3) Remove Blurring:
 - Run: python exwalker.py --setting old --path C:\Users\XXX\Desktop\Test
 - Result: Matched file types are unblurred.
 
 4) Set OS File Association:
 - Run: python exinout.py --operation import --path C:\\Users\\XXX\\Desktop\\here
 - Result: DefaultAssoc.xml is imported.

Help:
 - Run:
   python python exwalker.py --help
   python python exinout.py --help
   python python exgen.py --help


Note: 
 All paths are example, Please define your own path.
   
 
 
