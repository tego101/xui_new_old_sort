import os
import time
import difflib
import json
from termcolor import colored

from signal import signal, SIGINT
from sys import exit

old_file = input('name of old file (DO NOT INCLUDE .m3u) ')
new_file = input('name of new file (DO NOT INCLUDE .m3u) ')

file_a = 'list/' + old_file + '.m3u'
file_b = 'list/'  + new_file + '.m3u'

f=open(file_b,'r')  #open a file
f1=open(file_a,'r') #open another file to compare

str1=f.read().split("#")
str2=f1.read().split("#")

s1 = set(str1)
s2 = set(str2)
res2 = s2-s1

f.close()
f1.close()


os.system('clear')
print(colored("""
                *
                |{~}
                |
     _____~~~~~~~~~~~~~~_____
    /____#``````T```````#____/
    ###=> TM3U SORT v2 <=####
    !!!!!!!!!!!!!!!!!!!!!!!!!
    [][][][][][][][][]][]][]]
    =========================
    \n
    BACKGROUND:
    This is an upgrade to my last TOOL for XUI Panel.
    This TOOL allows you to search, organize, and repack your M3U intelligently.
    \n
    WARRANTY & SUPPORT:
    THIS TOOL IS OPENSOURCE & FREE. IF YOU PAID SOMEONE FOR IT ASK FOR A REFUND.
""", 'yellow'))
print(colored("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #  http://github.com/tego101/tm3usort_v2
    => ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   BITCOIN -> 1KouUcQ7o4rVh8gTg6W3HPUDsBBdoC6G1K
    #   CASHAPP -> REDTVME
    => ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #   ALL DONATIONS WILL BE USED FOR SUSHI PLEASE DONATE :)
    => ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""", 'green'))

input("Press Enter to start or press CRTL-C to exit...")
os.system('clear')

print(colored("""
                *
                |{~}
                |
     _____~~~~~~~~~~~~~~_____
    /____#``````T```````#____/
    ###=> TM3U SORT v2 <=####
    !!!!!!!!!!!!!!!!!!!!!!!!!
    [][][][][][][][][]][]][]]
    =========================
    \n
    Let's get started!
""", 'green'))
print(colored("""
    SYNCED
    =========================
    This options downloads the newest version of your streams list from your host then
    it compares your oldest streams list to the new one and displays NEW STREAMS.

    So for example if your host adds new channels they will be displayed at newly added streams.
    =========================
    OPTIONS
    =========================
    1.  Text Format
    2.  JSON
""", 'yellow'))
print(colored("""
    STATIC
    =========================
    This options allows you to search a single file for a specific stream.
    eg: USA COMEDY CENTRAL
    eg: A MOVIE NAME (2021)
    =========================
    OPTIONS
    =========================
    3.  SEARCH
""", 'cyan'))

selection = input('===> Please select a function #: ')

if selection == "1":
    os.system('clear')
    print(colored("""
        \n
        Ok, Please select a option.
        \n
        1.  ALL NEW
            - Shows all new entries in comparison with your old content list.
        2.  SEARCH
            - Search for stream by name or year.
    """, 'green'))

    search_or_all = input('===> ALL or Search: ')
    if search_or_all == "2":
        os.system('clear')
        print(colored("""
            \n
            Ok, Please select a option.
            \n
            1.  YEAR
                - Enter a year to get the results to newly added movies from that year.
            2.  NAME
                - Search for stream by name.
        """, 'green'))
        yr_or_name = input('===> Year or Name? ').lower()

        if yr_or_name == '1':
            os.system('clear')
            year = input('===> What year? ')
            for stream in res2:
                if "(" + year + ")" in stream:
                    if not '/series/' in stream:
                        print(stream.replace("EXTINF:-1,", "#EXTINF:-1, ").strip())
            print("\n")
            input('Save?')

        if yr_or_name == '2':
            os.system('clear')
            find = input('===> What are you looking for? ')
            for stream in res2:
                if find in stream:
                    print(stream.replace("EXTINF:-1,", "#EXTINF:-1, ").strip())

    if search_or_all == '1':
        os.system('clear')
        print(colored("""
                \n
                Ok, Please select a option.
                \n
                1.  ALL MOVIES
                    - Returns all new movies added.
                2.  ALL SERIES
                    - Returns all new series added.
                3.  ALL CHANNELS
                    - Returns all new channels added.
        """, 'green'))
        movie_or_series = input('Movies or Series? ')
        if movie_or_series == "1":
            for stream in res2:
                if not '/series/' in stream:
                    print(stream.replace("EXTINF:-1,", "#EXTINF:-1, ").strip())

        if movie_or_series == "2":
            for stream in res2:
                if not '/movie/' in stream:
                    print(stream.replace("EXTINF:-1,", "#EXTINF:-1, ").strip())

if selection == "2":
    os.system('clear')

    strms = []
    for stream in res2:
        if "(2021)" in stream:
            filtered = stream.replace("EXTINF:-1,", "").strip().split("\n")

            strms.append({ "title": filtered[0], "url": filtered[1] })

        print(strms)

if not selection:
    print(colored("\n ERROR: Please select and option \n", 'red'))
