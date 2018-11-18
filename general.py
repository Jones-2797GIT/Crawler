import os

#creating file (if not created)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project '+directory)
        os.makedirs(directory)

#creating files queue and crawled files (if not created) to store links
def create_data_files(project_name,base_url):
    queue=project_name+'/queue.txt'#that are about to be crawled
    crawled=project_name+'/crawled.txt'#that are done crawling
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#to write on a file
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()

#append the data to the file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

#delete all the contents
def delete_file_contents(path):
    with open(path,'w'):
        pass

#read a file and convert it into set for easy reading
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#iterate through a set each item in new line
def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)





