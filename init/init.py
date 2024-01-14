import os.path
import sys
import subprocess

def install(package):

    print('Starting download for ' + package)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
    print('Finished installing ' + package)

if __name__ == '__main__':
    print("\nSTARTING EXECUTING INIT.py\n")

    try: #ultralytics
        print("Searching for ultralytics\n")
        import ultralytics
        print("\nPackage already installed\n")
    except ImportError:
        install('ultralytics')
    finally:
        import ultralytics

    try: #pysimplegui
        print("Searching for pysimplegui\n")
        import PySimpleGUI
        print("\nPackage already installed\n")
    except ImportError:
        install('pysimplegui')
    finally:
        import PySimpleGUI

    try: #pandas
        print("Searching for pandas\n")
        import pandas
        print("\nPackage already installed\n")
    except ImportError:
        install('pandas')
    finally:
        import pandas

    img_dir_path = os.path.join("..","testPictures")
    os.mkdir(img_dir_path + "test")

    print("\nSUCCESSFULLY EXECUTED INIT.py")