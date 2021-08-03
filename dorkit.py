#!/usr/bin/python3

from colored import fg,bg,attr
import argparse



def banner(banner):
    if banner:
        print("\n%sG%s%s"% (fg(27), bg(235), attr(1))+"%so%s%s"% (fg(9), bg(235), attr(1))+"%so%s%s"% (fg(220), bg(235), attr(1))+"%sg%s%s"% (fg(27), bg(235), attr(1))+"%sl%s%s"% (fg(28), bg(235), attr(1))+"%se%s%s"% (fg(9), bg(235), attr(1)))
        print("%s██████╗ %s%s"% (fg(27), bg(235), attr(1))+"%s ██████╗ %s%s"% (fg(9), bg(235), attr(1))+"%s██████╗ %s%s"% (fg(220), bg(235), attr(1))+"%s██╗  ██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██╗%s%s"% (fg(28), bg(235), attr(1))+"%s████████╗%s%s"% (fg(9), bg(235), attr(1)))
        print("%s██╔══██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██╔═══██╗%s%s"% (fg(9), bg(235), attr(1))+"%s██╔══██╗%s%s"% (fg(220), bg(235), attr(1))+"%s██║ ██╔╝%s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s╚══██╔══╝%s%s"% (fg(9), bg(235), attr(1)))
        print("%s██║  ██║%s%s"% (fg(27), bg(235), attr(1))+"%s██║   ██║%s%s"% (fg(9), bg(235), attr(1))+"%s██████╔╝%s%s"% (fg(220), bg(235), attr(1))+"%s█████╔╝ %s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
        print("%s██║  ██║%s%s"% (fg(27), bg(235), attr(1))+"%s██║   ██║%s%s"% (fg(9), bg(235), attr(1))+"%s██╔══██╗%s%s"% (fg(220), bg(235), attr(1))+"%s██╔═██╗ %s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
        print("%s██████╔╝%s%s"% (fg(27), bg(235), attr(1))+"%s╚██████╔╝%s%s"% (fg(9), bg(235), attr(1))+"%s██║  ██║%s%s"% (fg(220), bg(235), attr(1))+"%s██║  ██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
        print("%s╚═════╝ %s%s"% (fg(27), bg(235), attr(1))+"%s ╚═════╝ %s%s"% (fg(9), bg(235), attr(1))+"%s╚═╝  ╚═╝%s%s"% (fg(220), bg(235), attr(1))+"%s╚═╝  ╚═╝%s%s"% (fg(27), bg(235), attr(1))+"%s╚═╝%s%s"% (fg(28), bg(235), attr(1))+"%s   ╚═╝   %s%s"% (fg(9), bg(235), attr(1)))
        print("\n\n")


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-b','--banner', default=True, action='store_false', required=False, help='Don\'t print Banner')
parser.add_argument('-db','--database' , type=str, metavar='',required=False ,help='Use GHDB Search\n')
parser.add_argument('--allintext' , type=str, metavar='',required=False ,help='Searches for occurrences of all the keywords given. ( --allintext "keyword" )')
parser.add_argument('--intext' , type=str, metavar='',required=False ,help='Searches for the occurrences of keywords all at once or one at a time. ( --intext "keyword" )')
parser.add_argument('--inurl' , type=str, metavar='',required=False ,help='Searches for a URL matching one of the keywords. ( --inurl "keyword" )')
parser.add_argument('--allinurl' , type=str, metavar='',required=False ,help='Searches for a URL matching all the keywords in the query. ( --allinurl "keyword" )')
parser.add_argument('--intitle' , type=str, metavar='',required=False ,help='Searches for occurrences of keywords in title all or one. ( --intitle "keyword" )')
parser.add_argument('--allintitle' , type=str, metavar='',required=False ,help='Searches for occurrences of keywords all at a time. ( --allintitle "keyword" )')
parser.add_argument('--site' , type=str, metavar='',required=False ,help='Specifically searches that particular site and lists all the results for that site. ( --site "www.google.com" )')
parser.add_argument('--filetype' , type=str, metavar='',required=False ,help='Searches for a particular filetype mentioned in the query. ( --filetype "pdf" )')
parser.add_argument('--link' , type=str, metavar='',required=False ,help='Searches for external links to pages. ( --link "keyword" )')
parser.add_argument('--numrange' , type=str, metavar='',required=False ,help='Used to locate specific numbers in your searches. ( --numrange 321-325 )')
parser.add_argument('--before' , type=str, metavar='',required=False ,help='Used to search within a particular date range. ( --before 2000-01-01 )')
parser.add_argument('--after' , type=str, metavar='',required=False ,help='Used to search within a particular date range. ( --after 2000-01-01 )')
parser.add_argument('--inanchor ' , type=str, metavar='',required=False ,help='This shows sites which have the keyterms in links pointing to them, in order of the most links.( --inanchor rat )')
parser.add_argument('--inpostauthor ' , type=str, metavar='',required=False ,help='Exclusive to blog search, this one picks out blog posts that are written by specific individuals. ( --inpostauthor "keyword" )')
parser.add_argument('--related' , type=str, metavar='',required=False ,help='List web pages that are “similar” to a specified web page. ( --related www.google.com )')
parser.add_argument('--cache' , type=str, metavar='',required=False ,help='Shows the version of the web page that Google has in its cache. ( --cache www.google.com )')
parser.add_argument('--altloc' , type=str, metavar='',required=False ,help='Searches for location in addition to one specified by language of site. ( --altloc en-us )')
args = parser.parse_args()

banner(args.banner)
