#!/usr/bin/env python
#encoding: utf-8

#usag:e python 

__author__ = "Keisuke Sakaguchi"

import sys
import os
import argparse
import util.edit_dist
import util.assignIOB
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# use either one depending on your NLTK version
#from nltk.tag.stanford import POSTagger  
from nltk.tag.stanford import StanfordPOSTagger

### ENVIRONMENTAL SETTINGS ###
JAVA_PATH = "/usr/lib/jvm/default-java/bin/java"
# for Mac users, it would be like
#JAVA_PATH = "/Library/Java/JavaVirtualMachines/jdk1.7.0_25.jdk/Contents/Home/bin/java"

STANFORD="./stanford-postagger/"
##############################

os.environ['JAVAHOME'] = JAVA_PATH

# use either one depending on your NLTK version
#postagger = POSTagger(STANFORD+"models/english-bidirectional-distsim.tagger", STANFORD+"stanford-postagger.jar", encoding="utf-8")
postagger = StanfordPOSTagger(STANFORD+"models/english-bidirectional-distsim.tagger", STANFORD+"stanford-postagger.jar", encoding="utf-8")

# argparser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-s', action='store', dest='source_file_path',
        help='source file', required=True)
arg_parser.add_argument('-r', action='store', dest='reference_directory_path',
        help='directory which contains (the same kind of) references', required=True)
arg_parser.add_argument('-n', action='store', dest='ng_list_path',
        help='use this if you want to skip some sentences with specific line numbers', required=False)
arg_parser.add_argument('-d', action='store_true', dest='debug', default=False,
        help='print out verbosely just for debugging porposes', required=False)
arg_parser.add_argument('-t', action='store_true', dest='if_tokenized', default=False,
        help='if the source and reference are tokenized', required=False)
args = arg_parser.parse_args()


ng_sentid = {}
if args.ng_list_path:
    for li in open(args.ng_list_path, 'r').readlines():
        ng_sentid[int(li.rstrip())] = 1

    if args.debug:
        print("## ng_list loaded")

src_len = len(open(args.source_file_path).readlines())
src = open(args.source_file_path, "r")

if args.debug:
    print("## src loaded")


refs = []
for f in os.listdir(args.reference_directory_path):
    refs.append(args.reference_directory_path + '/' + f)
    
refFiles = []
refs.sort()
for ref in refs:
    refFiles.append(open(ref, 'r'))
    ref_len = len(open(ref, 'r').readlines())
    assert ref_len == src_len


for i, s in enumerate(src.readlines()):
    # list of all edits from all references
    all_refs_edits = []

    # flag to know if a annotator has rated it grammatical
    grammatical_edit_added = False

    if args.debug:
        print("## sentence line {}".format(str(i+1)))

    if i+1 in ng_sentid.keys():
        if args.debug:
            print("## in ng_list")
        print("S " + s.rstrip())
        print()
        for ref in refFiles:
            ref.readline()
    elif i < 0: # for debugging purpose: set the line number which you want to start 
        print("S " + s.rstrip())
        print()
        for ref in refFiles:
            ref.readline()
    else:
        src = s.rstrip()
        if args.if_tokenized:
            src_tokens = [w for w in src.split(' ')]
        else:
            src_tokens = [w for w in word_tokenize(src)]
        src_pos_tags = list(list(zip(*postagger.tag(src_tokens)))[1])
        print("S " + src)

        for r_id, ref in enumerate(refFiles):
            if args.if_tokenized:
                ref = ref.readline().rstrip()
            else:
                ref = " ".join(word_tokenize(ref.readline().rstrip()))
            ref_tokens = [w for w in ref.split(' ')]
            if len(ref) == 0:
                pass
            else:
                ref_pos_tags = list(list(zip(*postagger.tag(ref_tokens)))[1])
                if args.debug:
                    print("## src tokens: " + src_tokens)
                    print("## ref tokens: " + ref_tokens)
                    print("## src pos: " + src_pos_tags)
                    print("## ref pos: " + ref_pos_tags)

                dist, edits_operation = util.edit_dist.getEditDistWithPOS(src_tokens, ref_tokens, src_pos_tags, ref_pos_tags)

                edits_list = util.assignIOB.getIOB(edits_operation[0:-1])
                # D: reference includes but source deleted (inserted in reference / deleted in source)
                # I: reference deleted but source included (inserted in source / deleted in reference)
                # Rx: replacement with its type x (see ./util/edit_dist.py for more details)

                if args.debug:
                    print("## edits: ")
                    print(edits_operation[0:-1])
                    print(edits_list)

                src_idx = 0
                ref_idx = 0

                # if the reference has an edit
                ref_has_edit = False

                for edit in edits_list:
                    begin_src_idx, end_src_idx, operation, begin_ref_idx, end_ref_idx = edit
                    if operation == "I":
                        edit_annot = "A {} {}|||#Ins#||||||REQUIRED|||-NONE-|||{}".format(begin_src_idx, end_src_idx, r_id)
                        ref_has_edit = True
                        all_refs_edits.append(edit_annot)
                    elif operation == "D":
                        deleted = " ".join(ref.split()[begin_ref_idx:end_ref_idx])
                        edit_annot = "A {} {}|||#Del#|||{}|||REQUIRED|||-NONE-|||{}".format(begin_src_idx, begin_src_idx, deleted, r_id)
                        ref_has_edit = True
                        all_refs_edits.append(edit_annot)
                    elif operation[0] == "R":
                        replaced = " ".join(ref.split()[begin_ref_idx:end_ref_idx])
                        edit_annot = "A {} {}|||#{}#|||{}|||REQUIRED|||-NONE-|||{}".format(begin_src_idx, end_src_idx, operation, replaced, r_id)
                        ref_has_edit = True
                        all_refs_edits.append(edit_annot)
                    elif operation == "_":
                        pass
                    else:
                        raise

                # if ref is same as src, i.e. sentence is grammatical
                if not ref_has_edit and not grammatical_edit_added:
                    all_refs_edits.append("A -1 -1|||noop|||-NONE-|||REQUIRED|||-NONE-|||" + str(r_id))
                    grammatical_edit_added = True

        if len(all_refs_edits) != 1: # This will be 1 if all references annotate sentence as grammatical
            for edit in all_refs_edits:
                print(edit)
        print() 

