# example4-extrafiles.py - get info about all files in first thread
from __future__ import print_function
import pyfuuka
import requests
import json
import copy
#def _get_json(self, url):
#    res = self._requests_session.get(url)
#    res.raise_for_status()
#    return res
def main():
    # grab the first thread on the board by checking first page
    board = pyfuuka.Board('a','archived.moe')
    # error if inputted non-existent board
    
    ## ORIG
    #all_thread_ids = board.get_all_thread_ids()
    #first_thread_id = all_thread_ids[0]
    
    #print("printing thread ids")
    #print(all_thread_ids)
    
    thread = board.get_thread(192139412)
    
    # thread information
    print('thread-info', thread)
    print('Sticky?', thread.sticky)
    print('Closed?', thread.closed)
    print()

    # topic information
    topic = thread.topic
    print('Topic Repr', topic)
    print('Postnumber', topic.post_number)
    print('Timestamp',  topic.timestamp)
    print('Datetime',   repr(topic.datetime))
    print('Subject',    topic.subject)
    print('Comment',    topic.text_comment)
    print('Replies',    thread.replies)
    print()

    # file information
    #for f in thread.file_objects():
    #    print('Filename', f.filename)
    #    print('  Filemd5hex', f.file_md5_hex)
    #    print('  Fileurl', f.file_url)
    #    print('  Thumbnailurl', f.thumbnail_url)
    #    print()
        
    # display info about every file on the first thread, even extra files in posts
    for post in thread.all_posts:
        if post.has_file:
            print(":: Post #", post.post_number)
            print("  ", post.file.filename)
            print("  ", post.file.file_md5_hex)
            print("  ", post.file.file_url)
            print("  ", post.file.thumbnail_url)
            print()
    exit()

if __name__ == '__main__':
    main()