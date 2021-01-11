import json
import os
import argparse

class FileFolderHandler(object):

    def __init__(self, start_path):
        self.start_path = start_path
        self.config_file_path = "new_extensions.json"

    def set_new_extensions(self):
        json_file = open(self.config_file_path, 'r')
        data = json.load(json_file)
        for root, subFolders, files in os.walk(self.start_path):
            for file in files:
                full_filename = os.path.join(root, file)
                fname = os.path.splitext(full_filename)[0]
                old_extension = os.path.splitext(full_filename)[1]
                for i in data:
                    if i['extension'] == old_extension:
                        os.rename(full_filename, fname + i['value'])
                    else:
                        pass
                print("Extension is set for '{}'".format(full_filename))

    def set_old_extensions(self):
        json_file = open(self.config_file_path, 'r')
        data = json.load(json_file)
        for root, subFolders, files in os.walk(self.start_path):
            for file in files:
                full_filename = os.path.join(root, file)
                fname = os.path.splitext(full_filename)[0]
                old_extension = os.path.splitext(full_filename)[1]
                for i in data:
                    if i['value'] == old_extension:
                        os.rename(full_filename, fname + i['extension'])
                    else:
                        pass
                print("Extension is set for '{}'".format(full_filename))


def runner(args):
    agent = FileFolderHandler(args.path)
    if args.setting == 'new':
        agent.set_new_extensions()
    elif args.setting == 'old':
        agent.set_old_extensions()
    else:
        print("ERROR - Something went wrong!")


def main():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument('--setting', type=str, help="Provide your setting option, Example: '--setting new/old' (required)")

    my_parser.add_argument('--path', type=str, help="Provide your path for extension changes: '--path C:\\Users\\<username>\\Desktop' (required)")

    args = my_parser.parse_args()

    runner(args)


if __name__ == "__main__":
    main()


# Example execution:
# python exwalker.py --setting new --path C:\Users\XXX\Desktop\Test
# python exwalker.py --setting old --path C:\Users\XXX\Desktop\Test
# python python exwalker.py --help