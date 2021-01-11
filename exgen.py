import xml.etree.ElementTree as ET
from datetime import datetime
import random
import time
import hashlib
import json
import os
import argparse


class _ExtensionGeneration(object):
    def __init__(self):
        pass

    def get_new_extension(self):
        time.sleep(0.1)
        now = datetime.now()
        current_date_and_time = now.strftime("%Y%m%d%H%M%S%f")
        random_num = random.randint(random.randint(0,500),random.randint(1000,1500))
        full_text = str(current_date_and_time)+str(random_num)
        generated_extension = hashlib.md5(full_text.encode()).hexdigest()
        return generated_extension


class HandleXML(object):

    def __init__(self, file_location):
        self.output_filename = "new_extensions.json"
        self.new_xml_full_fname = "DefaultAssoc.xml"
        self.tree = ET.parse(os.path.join(file_location, self.new_xml_full_fname))
        self.root = self.tree.getroot()
        self.extension_gen = _ExtensionGeneration()
        self.json_data = ""


    def list_all(self):
        for idx in range(len(self.root)):
            print(type(self.root[idx].attrib))


    def configure_new_extensions(self):
        result_file = open(self.output_filename, "w")
        new_extensions = list()
        for item in self.root.iter('Association'):
            dict_element = dict()

            # Get data
            ex_gen = "."+self.extension_gen.get_new_extension()
            item_value = item.attrib['Identifier']

            # Add data to dict
            dict_element['value'] = ex_gen
            dict_element['extension'] = item_value
            new_extensions.append(dict_element)

            # Set data
            item.set('Identifier', ex_gen)
            print(ex_gen,"|",item_value)

        json.dump(new_extensions, result_file, indent = 6) 
        result_file.close()
        self.tree.write(self.new_xml_full_fname)


    def configure_old_extensions(self):
        json_file = open(self.output_filename, 'r')
        data = json.load(json_file)
        for item in self.root.iter('Association'):
            item_value = item.attrib['Identifier']

            for i in data:
                if i['value'] == item_value:
                    item.set('Identifier', i['extension'])
                    print(i['value'],"|",i['extension'])
                else:
                    pass
                
        self.tree.write(self.new_xml_full_fname)



def runner(args):
    agent = HandleXML(args.path)
    if args.configure == 'new':
        agent.configure_new_extensions()
    elif args.configure == 'old':
        agent.configure_old_extensions()
    else:
        print("ERROR - Something went wrong!")


def main():
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument('--configure', type=str, help="Provide your configure option, Example: '--configure new/old' (required)")

    my_parser.add_argument('--path', type=str, help="Provide your XML file path, Example: '--path C:\\Users\\<username>\\Desktop' (required)")

    args = my_parser.parse_args()

    runner(args)


if __name__ == "__main__":
    main()


# Example execution:
# python exgen.py --configure new --path C:\Users\XXX\Desktop\here
# python exgen.py --configure old --path C:\Users\XXX\Desktop\here
# python python exgen.py --help