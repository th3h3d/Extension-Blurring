import os
import argparse

class OSExtensionSetting(object):
    # Windows 10 only
    
    def __init__(self, path_to_EI, fname="DefaultAssoc.xml"):
        self.full_path = os.path.join(path_to_EI, fname)
       

    def export_extension(self):
        try:
            export_string = """Dism.exe /online /Export-DefaultAppAssociations:"""
            os.system(export_string+str(self.full_path))
        except Exception as e:
            print("Error: {}".format(e))

    def import_extension(self):
        try:
            export_string = """Dism.exe /online /Import-DefaultAppAssociations:"""
            os.system(export_string+str(self.full_path))
        except Exception as e:
            print("Error: {}".format(e))

def runner(args):
    agent = OSExtensionSetting(args.path)
    if args.operation == 'export':
        agent.export_extension()
    elif args.operation == 'import':
        agent.import_extension()
    else:
        print("ERROR - Something went wrong!")


def main():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument('--operation', type=str, help="Provide your operation, Example: '--operation export/import' (required)")

    my_parser.add_argument('--path', type=str, help="Provide your XML file path, Example: '--path C:\\Users\\<username>\\Desktop' (required)")

    args = my_parser.parse_args()

    runner(args)


if __name__ == "__main__":
    main()


# Example execution:
# python exinout.py --operation export --path C:\\Users\\XXX\\Desktop\\here
# python exinout.py --operation import --path C:\\Users\\XXX\\Desktop\\here
# python python exinout.py --help