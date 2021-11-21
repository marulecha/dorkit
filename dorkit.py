#!/usr/bin/python3

from colored import fg,bg,attr
import argparse
import sys, os, shutil


def banner():

    print("\n%sG%s%s"% (fg(27), bg(235), attr(1))+"%so%s%s"% (fg(9), bg(235), attr(1))+"%so%s%s"% (fg(220), bg(235), attr(1))+"%sg%s%s"% (fg(27), bg(235), attr(1))+"%sl%s%s"% (fg(28), bg(235), attr(1))+"%se%s%s"% (fg(9), bg(235), attr(1)))
    print("%s██████╗ %s%s"% (fg(27), bg(235), attr(1))+"%s ██████╗ %s%s"% (fg(9), bg(235), attr(1))+"%s██████╗ %s%s"% (fg(220), bg(235), attr(1))+"%s██╗  ██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██╗%s%s"% (fg(28), bg(235), attr(1))+"%s████████╗%s%s"% (fg(9), bg(235), attr(1)))
    print("%s██╔══██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██╔═══██╗%s%s"% (fg(9), bg(235), attr(1))+"%s██╔══██╗%s%s"% (fg(220), bg(235), attr(1))+"%s██║ ██╔╝%s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s╚══██╔══╝%s%s"% (fg(9), bg(235), attr(1)))
    print("%s██║  ██║%s%s"% (fg(27), bg(235), attr(1))+"%s██║   ██║%s%s"% (fg(9), bg(235), attr(1))+"%s██████╔╝%s%s"% (fg(220), bg(235), attr(1))+"%s█████╔╝ %s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
    print("%s██║  ██║%s%s"% (fg(27), bg(235), attr(1))+"%s██║   ██║%s%s"% (fg(9), bg(235), attr(1))+"%s██╔══██╗%s%s"% (fg(220), bg(235), attr(1))+"%s██╔═██╗ %s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
    print("%s██████╔╝%s%s"% (fg(27), bg(235), attr(1))+"%s╚██████╔╝%s%s"% (fg(9), bg(235), attr(1))+"%s██║  ██║%s%s"% (fg(220), bg(235), attr(1))+"%s██║  ██╗%s%s"% (fg(27), bg(235), attr(1))+"%s██║%s%s"% (fg(28), bg(235), attr(1))+"%s   ██║   %s%s"% (fg(9), bg(235), attr(1)))
    print("%s╚═════╝ %s%s"% (fg(27), bg(235), attr(1))+"%s ╚═════╝ %s%s"% (fg(9), bg(235), attr(1))+"%s╚═╝  ╚═╝%s%s"% (fg(220), bg(235), attr(1))+"%s╚═╝  ╚═╝%s%s"% (fg(27), bg(235), attr(1))+"%s╚═╝%s%s"% (fg(28), bg(235), attr(1))+"%s   ╚═╝   %s%s"% (fg(9), bg(235), attr(1)))
    print("%shttps://github.com/marulecha%s%s\n"% (fg(8), bg(235), attr(1)))
    print("%sWarning! Excessive usage may cause Google to block your IP Address.%s%s\n\n"% (fg(1), bg(235), attr(1)))

def arguments():
    parser = argparse.ArgumentParser(description='List of accepted arguments.')
    parser.add_argument('--results' , type=int, metavar='',required=False, default=10, help='Number of results we want to retrieve. (Default = 10)')
    parser.add_argument('--pause' , type=int, metavar='',required=False, default=2, help='Lapse to wait between HTTP requests. Too short Lapse may cause Google to block your IP. (Default = 2)')
    parser.add_argument('--allintext' , type=str, metavar='',required=False ,help='Searches for occurrences of all the keywords given. ( --allintext <keyword> )')
    parser.add_argument('--intext' , type=str, metavar='',required=False ,help='Searches for the occurrences of keywords all at once or one at a time. ( --intext <keyword> )')
    parser.add_argument('--inurl' , type=str, metavar='',required=False ,help='Searches for a URL matching one of the keywords. ( --inurl <keyword> )')
    parser.add_argument('--allinurl' , type=str, metavar='',required=False ,help='Searches for a URL matching all the keywords in the query. ( --allinurl <keyword> )')
    parser.add_argument('--intitle' , type=str, metavar='',required=False ,help='Searches for occurrences of keywords in title all or one. ( --intitle <keyword> )')
    parser.add_argument('--allintitle' , type=str, metavar='',required=False ,help='Searches for occurrences of keywords all at a time. ( --allintitle <keyword> )')
    parser.add_argument('--site' , type=str, metavar='',required=False ,help='Specifically searches that particular site and lists all the results for that site. ( --site "www.google.com" )')
    parser.add_argument('--filetype' , type=str, metavar='',required=False ,help='Searches for a particular filetype mentioned in the query. ( --filetype "pdf" )')
    parser.add_argument('--link' , type=str, metavar='',required=False ,help='Searches for external links to pages. ( --link <keyword> )')
    parser.add_argument('--numrange' , type=str, metavar='',required=False ,help='Used to locate specific numbers in your searches. ( --numrange 321-325 )')
    parser.add_argument('--before' , type=str, metavar='',required=False ,help='Used to search within a particular date range. ( --before 2000-01-01 )')
    parser.add_argument('--after' , type=str, metavar='',required=False ,help='Used to search within a particular date range. ( --after 2000-01-01 )')
    parser.add_argument('--inanchor ' , type=str, metavar='',required=False ,help='This shows sites which have the keyterms in links pointing to them, in order of the most links.( --inanchor rat )')
    parser.add_argument('--inpostauthor ' , type=str, metavar='',required=False ,help='Exclusive to blog search, this one picks out blog posts that are written by specific individuals. ( --inpostauthor <keyword> )')
    parser.add_argument('--related' , type=str, metavar='',required=False ,help='List web pages that are “similar” to a specified web page. ( --related www.google.com )')
    parser.add_argument('--cache' , type=str, metavar='',required=False ,help='Shows the version of the web page that Google has in its cache. ( --cache www.google.com )')
    parser.add_argument('--altloc' , type=str, metavar='',required=False ,help='Searches for location in addition to one specified by language of site. ( --altloc en-us )')

    args = parser.parse_args()
    argLen = len(sys.argv)
    def argCheck(argLen,parser):
        if argLen < 2:
            print("%s[-] Example Usage:\n\tpython3 dorkit.py --inurl \"keyword\"%s%s\n"% (fg(9), bg(235), attr(1)))
            print("[-] For more help:\n\tpython3 dorkit.py --help\n")

    argCheck(argLen,parser)

    return args

args = arguments()

#take the input and create a list of the arguments the user inserted.
def getArguments():
    argumentList = []
    for k in args.__dict__:
        if args.__dict__[k] is not None:
            if args.__dict__[k] is args.results:
                results = args.results
            elif args.__dict__[k] is args.pause:
                pause = args.pause
            else:
                j = k+':'+args.__dict__[k]
                #print(j)
                argumentList.append(j)
    #print(argumentList)    
    #     
    #create query based on arguments.
    query = ""
    for i in argumentList:
        query = str(query +i +" ")
    #print(query)
    return query, results, pause

def googleSearch(query, num2, pause2):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    dir = query.strip()
    #create directory if not already there
    if os.path.exists(dir):
        createNewFile = input("A File with such results already exists, do you want to rescan? [y/N] ")
        if createNewFile == 'Y' or createNewFile =='y':
            shutil.rmtree(dir)
            os.mkdir(dir)
        else:
            exit()
    else:
        os.mkdir(dir)
        
    #file names
    textFile = dir+"/output_dorkit.txt"
    csvFile = dir+"/output_dorkit.csv"
    #write the results into csv and txt files.
    with open(textFile,'a') as txt:
        with open(csvFile,'a') as csv:
            for url in search(query, tld="co.in", num=results, stop=results, pause=pause2):
                print(url +'%s'% (fg(2)))
                txt.write(url+"\n")
                csv.write(url+"\n")

#print banner and check if there are any arguments.
banner()

#Query for the google search.
query, results, pause2 = getArguments()
googleSearch(query, results, pause2)