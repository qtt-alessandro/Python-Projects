
HOMEWORK PT.1

Section 1.1- Introduction
#exsercise Hello, World! - 1
print ("Hello, World!")

#exsercise Python if-else -2
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print ("Weird")
    elif n % 2 ==0 and n in range(2,6):
        print ('Not Weird')
    elif n % 2 == 0 and n in range(6,21):
        print ('Weird')
    elif n % 2 == 0 and n>20:
        print('Not Weird')

#exsercise Arithmetic Operator -3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#exercise Division -4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#exercise Loops -5
if __name__ == '__main__':
    n = int(input())
for i in range(0, n):
    print(i * i)

#exercise Write a function -6
def is_leap(year):
    leap = False

    # Write your logic here
    year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap
year = int(input())
print(is_leap(year))

#exercise Print function -7
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

Section 1.2 - Data Types

#exercise List Comprehensions - 1
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
permutations = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1)if (i+j+k != n)]
print (permutations)

#exercise Find the Runner-Up Score -2
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr.remove(max(arr))
print(arr [-2])

#exercise Finding the Percentage - 3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_values = sum(student_marks[query_name])
    lenght = len(student_marks[query_name])
    average = sum_values/lenght
    print("{0:.2f}".format(average))

#exersice Lists -4
if __name__ == '__main__':
    N = int(input())
    results = []

    for _ in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'pop':
            results.pop()
        if command == 'print':
            print(results)
        if command == 'append':
            results.append(int(x[1]))
        if command == 'insert':
            results.insert(int(x[1]), int(x[2]))
        if command == 'remove':
            results.remove(int(x[1]))
        if command == 'reverse':
            results = results[::-1]
        if command == 'sort':
            results = sorted(results)

#exercise Tuples -5
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

#exercise Nested List -6
if __name__ == '__main__':
    dic={}
    a = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in a:
            a.append(score)
    first_lower= min(a)
    a.remove(first_lower)
    second_lower= min(a)
    dic[second_lower].sort()
    for i in dic[second_lower]:
        print(i)


Section 1.3 - Strings

#exercise Swap Case-1
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print result

#exercise String Split and Join-2
def split_and_join(line):
    words = line.split(" ")
    words = "-".join(words)
    return words
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print result

#exercise What's Your Name?-3
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a,b))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#exercise Mutations-4
def mutate_string(string, position, character):
    l= list(string)
    l[position] = character
    string = ''.join(l)
    return  string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#exercise Find a string-5
def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            counter += 1
    return counter
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#exercise String Validator-6
if __name__ == '__main__':
    s =input()
print (any(i.isalnum() for i in s))
print (any(i.isalpha() for i in s))
print (any(i.isdigit() for i in s))
print (any(i.islower() for i in s))
print (any(i.isupper() for i in s))

#exercise Text Alignment-7
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)
#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

#exercise Text Wrap-8
import textwrap
def wrap(string, max_width):
    l= (textwrap.fill(string,max_width))
    return l

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#exercise Designer Door Mat-9
N, M = map(int, input().split())
for i in range(1,N,2):
    print ((i*'.|.').center(M, '-'))
print ('WELCOME'.center(M,'-'))
for i in range(N-2,-1,-2):
    print ((i*'.|.').center(M, '-'))

#exercise String Formatting-10
def print_formatted(number):
    l = len(bin(n)) - 2
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=l))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#exercise Capitalize-11
 a= s.split(" ")
    b= [i.capitalize() for i in a]
    return " ".join

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#exercise The Minion Game-12
def minion_game(string):
    vocali = ['A', 'I', 'O', 'E', 'U']
    c_t = dict()
    v_t = dict()
    kevin = 0
    stuart = 0
    count = 0
    for i in range(len(string)):
        if string[i] in vocali:
            kevin = kevin + len(string) - i
        else:
            stuart = stuart + len(string) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

#exercise Merge The Tools!-13
def no_rep(t):
    string= set()
    a= []
    for i in t:
        if i not in string:
            string.add(i)
            a.append(i)
    return "".join(a)


def merge_the_tools(string, k):
     n= len(string)
     for j in [string[i:i+k] for i in range (0,n,k)]:
         print(no_rep(j))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#exercise Alphabet Rangoli-14
def print_rangoli(size):
    import string
    font = string.ascii_lowercase
    c=[]

    for i in range(n):
        s = "-".join(font[i:n])
        c.append(s[::-1]+s[1:])
    width = len(c[0])
    for i in range(n-1, 0, -1):
        print(c[i].center(width, "-"))
    for i in range(n):
        print(c[i].center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



Section 1.4 - Sets

# exercise 1 Introduction to Sets-1
def average(array):
    heights = set(array)
    n = len(heights)
    sum_heights = sum(heights)
    average = sum_heights / n
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#exercise No Idea!-2
n_m = input().split()
n_m = map(int, n_m)
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int,input().split()))
happy = 0
for i in n:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print (happy)

#exercise Symmetric Difference-3
int(input())
N= input().split()
N_int = set(list(map(int, N)))
int(input())
M = input().split()
M_int = set(list(map(int, M)))
lis=[]
for x in list(N_int.difference(M_int)):
    lis.append(x)
for y in list(M_int.difference(N_int)):
    lis.append(y)
for z in sorted(lis):
    print (z)

#exercise Set .add()-4
N= int(input())
countries = set()
for i in range (N):
    stamps= input()
    countries.add(stamps)
print (len(countries))

#exercise Discard,Remove and Pop-5
n = input()
s = set(map(int,input().split()))
a = int(input())

for _ in range(a):
    k = []
    k = input().split(" ")
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
print(sum(set(s)))

#exercise Set Union Operation-6
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.union(french)
print (len(un))

#exercise Set Intersection Operation-7
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.intersection(french)
print (len(un))

#exercise Set Difference Operation-8
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.difference(french)
print (len(un))

#exercise Symmetric Difference Operation-9
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.symmetric_difference(french)
print (len(un))

#exercise Set Mutations-10
n = int(input())
A = set(input().split())
for _ in range (int(input())):
    op = input().split()
    B= input().split()
    if op[0]== 'intersection_update':
        A.intersection_update(B)
    elif op[0]== 'difference_update':
        A.difference_update(B)
    elif op[0]== 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif op[0] == 'update':
        A.update(B)
print(sum(map(int, A)))

#exercise The Captain's Room-11
from collections import Counter

n=int(input())
A= list(map(int,input().split()))
AA= Counter(A)

for i in A:
    if AA[i]==1:
        print(i)

#exercise Check Subset-12
T = int(input())
for _ in range(T):
    n = int(input())
    A = set(list(map(int, input().split())))
    m = int(input())
    B = set(list(map(int, input().split())))
    print(True if len(A.difference(B)) == 0 else False)

# exercise Check String Superset-13
A = set(input().split())
N = int(input())
conta = 0
for _ in range(N):
    B = set(input().split())
if len(B.difference(A)) != 0:
    conta = 1
if conta == 0:
    print("True")

else:
    print("False")



Section 1.5 - Collection

#exercise Collections.Counter()-1
from collections import Counter
X = int(input())
collected_shoes = [int(val) for val in input().split()]
N = int(input())

shoes_stored = Counter(collected_shoes)
daily_budget = 0

for i in range(N):
    size, money = [int(val) for val in input().split()]

    if shoes_stored.get(size):
        daily_budget += money
        shoes_stored[size] -= 1

print(daily_budget)

#exercise Default Dictonary -2
from collections import defaultdict
dictonary = defaultdict(list)
lista = []
n, m = map(int, input().split())  # acquire n and m in input
for i in range(0, n):
    dictonary[input()].append(i + 1)
for i in range(0, m):  # fill the list with a for cicle
    lista = lista + [input()]
for i in lista:  # for the len of lista
        if i in dictonary:  # if you find i in d print togheter
        print(" ".join(map(str, dictonary[i])))  # print with space the dictonary as list
        else:
        print - 1

#exercise Collections.namedtuple()-3
from collections import namedtuple
N = int(input())
primo = input().split()
grades = namedtuple("grades", primo)
ave = []
for _ in range(N):
    ins = (sum([int(grades(*input().split()).MARKS)]) / N)
    ave.append(ins)
print(sum(ave))

# exercise Collections.OrderedDict()-4
from collections import OrderedDict
n = int(input())
d = OrderedDict()

for i in range(n):
    products, space, quantity = input().rpartition(' ')
d[products] = d.get(products, 0) + int(quantity)
    for products, quantity in d.items():
print(products, quantity)

#exercise Word Order-5
import collections
N = int(input())
dictionary = collections.OrderedDict()

for i in range(N):
    words = input()
    if words in dictionary:
        dictionary[words] +=1
    else:
        dictionary[words] = 1

print(len(dictionary))

for key, value in dictionary.items():
    print(value,end=' ')

#exercise Collection.denque()-6
from collections import deque
d = deque()
N = int(input())

for _ in range(N):
    x = input().split(" ")
    command = x[0]

    if command == "append":
        d.append(int(x[1]))
    if command == "pop":
        d.pop()
    if command == "popleft":
        d.popleft()
    if command == "appendleft":
        d.appendleft(int(x[1]))
for i in range(len(d)):
    print(d[i], end = " ")

#exercise Company Logo-7
from collections import Counter
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    a = Counter(s)
    b = sorted(a.items(), key=lambda item: (-item[1], item[0]))
    for i in range(3):
        print(b[i][0], b[i][1])

#exercise Pilling Up!-8
N = int(input())
for _ in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a, reverse = True)
    if b[0] == a[0] or b[0] == a[n-1]:
        print("Yes")
    else:
        print("No")


Section 1.6 - Date and Time

#exercise Calendar Module-1
import calendar
day,month,year =map(int,input().split())
print(list(calendar.day_name)[calendar.weekday(year,day,month)].upper())

#exercise Time Delta-2
import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def time_delta(t1, t2):
    formato_orario = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, formato_orario)
    t2 = datetime.strptime(t2, formato_orario)
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

Section 1.7 Exeptions

#exercise - Exeptions-1
for i in range(int(input())):

    try:
        a,b=map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)

Section 1.8 Built In

#exercise Zipped!-1
n, x = map(int, input().split())
results = []
for _ in range(x):
    results.append( map(float, input().split()) )

for i in zip(*results):
    avg= sum(i)/len(i)
    print(avg)

#exercise Athlete Sort-2
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    s = sorted(arr, key = lambda x: x[k])

    for i in range(n):
        print(str.join(' ', map(str, s[i])))

#exercise GinortS-3
import re
string = input()
cases = [r'[a-z]', r'[A-Z]' , r'[13579]' ,r'[02468]']
b = [r for cases in cases for r in sorted(re.findall(cases, string))]
print("".join(b))

Section 1.9 Python Functionals

#exercise Map and lambda Function-1
cube = lambda x:x ** 3
def fibonacci(n):
    a=0
    b=1
    l=[]
    if n== 0:
        pass
    elif n==1:
        l.append(a)
    else:
        l.append(a)
        l.append(b)
        for i in range (2,n):
            c= a+b
            a=b
            b=c
            l.append(c)
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

Section 1.10  Regex and Parsing

#exercise Detect Floating Point Number-1
import re
n = int(input())
for _ in range(n):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

#exercise Re.split()-2
regex_pattern = r"[\,*\.*]"
import re
print("\n".join(re.split(regex_pattern, input())))

#exercise Group(), Groups() & Groupdict()-3
import re
alphanumeric = input()
m = re.search(r'([a-z A-Z 0-9])\1', alphanumeric)
if m:
    print(m.group(1))
else:
    print(-1)

#exercise Re.findall()& Re.finditer()-4
import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))


#exercise Re.star()& Re.end()-5
import re
text, pattern = input(), input()
m= list(re.finditer("(?=(%s))"%pattern,text))
if not m:
    print((-1,-1))
for i in m:
    print((i.start(1),i.end(1)-1))


#exercise Validating Roman Numerals-6
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))

#exercise Validating phone numbers-7
import re
n=int(input())
reges= r"^[789]{1}\d{9}$"
for _ in range(n):
    line = input()
    if re.match(reges, line):
        print("YES")
    else:
        print("NO")

#exercise Validating and parsing Email Addresses-8
import re
n = int(input())
for _ in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)

#exercise Hex Color Code-9
import re
n= int(input())

for _ in range(n):
    font = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if font:
        print(*font, sep='\n')

#exercise HTML Parser- Part 1- 10
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        if bool(attrs)== True:
            for items in attrs:
                print ('->', items[0], '>', items[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        if bool(attrs)== True:
            for items in attrs:
                print ('->', items[0], '>', items[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

#exercise HTML Parser- Part 2-11
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if '\n' in data:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        print(data)
    def handle_data (self,data):
        if data== '\n':
            return
        else:
            print(">>> Data")
            print(data)
html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#exercise Detect HTML tags, attributes and attributes value-12
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for at in attrs:
            print("-> {} > {}".format(at[0], at[1]))

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

#exercise Valid UID-13
import re
n= int(input())

for i in range (n):
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})[a-zA-Z0-9]{10}$', input()):
        print('Valid')
    else:
        print("Invalid")

#exercise Validating Credit Card -14
import re
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")

#exercise Regex Substitution-15
import re
n = int(input())
for i in range(n):
    a = input()
    while " && " in a or " || " in a:
        a = re.sub(r'\s\&\&\s',' and ',a)
        a = re.sub(r'\s\|\|\s',' or ',a)
    print(a)
#exercise Validating Postal Code-16
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=(\d)\1)"
import re
P = input()
print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

#exercise Matrix Script -17
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for i in range(n):
    a = str(input())
    matrix.append(a)
s = ''
for i in range (m):
    for a in matrix:
        s += a[i]
print ( re.sub(r"(?<=[a-zA-Z])([\$\#\!\@\%\&\s]+)(?=[a-zA-Z])", " ", s))
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

Section 1.11  Xml

#exercise Xml Find the score-1
import sys
import xml.etree.ElementTree as etree
sum_get= 0
def get_attr_number(node):
    a= sum(get_attr_number(child) for child in node);
    return len(node.attrib) +a


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#exercise Find the maximum Depth-2
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if (maxdepth<level):
        maxdepth= level
    for child in elem:
        depth(child,level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)


Section 1.12 - Closures and Decorations

#exercise Standardize Mobile Number Using Decorators-1
def wrapper(f):
    def fun(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

#exercise Name directory-2
import operator
def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


Section 1.13 Numpy

#exercise Array-1
import numpy
def arrays(arr):
    a=numpy.array(arr,float)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#exercise Shape and Reshape-2
import numpy
n= input().split()
print(numpy.array(n,int).reshape(3,3))

#exercise Transpose and Flatten-3
import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for i in range(0,n)], int)
print (array.transpose())
print (array.flatten())

#exercise Concatenate-4

import numpy
n, m, p = map(int,input().split())

a = numpy.array([input().split() for i in range(0,n)],int)
b = numpy.array([input().split() for _ in range(0,m)],int)
print(numpy.concatenate((a, b), axis = 0))

#exercise Zeros and Ones-5
import numpy
extension= list(map(int,input().split()))
print (numpy.zeros(extension,dtype = numpy.int))
print (numpy.ones(extension, dtype = numpy.int))

#exercise Eye and Identity-6
import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
print (numpy.eye(n,m,k = 0))

#exercise Array Mathematics-7
import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print (a+b)
print (a-b)
print (a*b)
print (a//b)
print (a%b)
print (a**b)

#exercise Floor, Ceil and Rint-8
import numpy
numpy.set_printoptions(sign=' ')
arr=numpy.array(input().split(),float)
print (numpy.floor(arr))
print (numpy.ceil(arr))
print (numpy.rint(arr))

#exercise Sum and Prod-9
import numpy
n,m=map(int,input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
a=numpy.sum(arr, axis = 0)
print (numpy.prod(a, axis = None))

#exercise Min and Max-10
import numpy
n,m=map(int,input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
a= numpy.min(arr, axis = 1)
print (numpy.max(a))

#exercise Mean, var and std-11
import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
print (numpy.mean(arr, axis = 1))
print (numpy.var(arr, axis = 0))
print (numpy.std(arr))

#exercise Dot and Cross-12
import numpy
n=int(input())
a = numpy.array([input().split() for _ in range(n)],int)
b = numpy.array([input().split() for _ in range(n)],int)
print (numpy.dot(a, b))

#exercise Inner and Outer-13

import numpy
a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print (numpy.inner(a,b))
print (numpy.outer(a,b))

#exercise Polynomials-14
import numpy
a = numpy.array(input().split(), float)
x= float(input())
print (numpy.polyval(a, x))

#exercise Linear Algebra-15
import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
print(round(numpy.linalg.det(a),2))



HOMEWORK PT.2

#exercise Birthday Cake Candles-1
import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#exercise Number Line Jumps-2
import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if x1>x2 and v1>v2:
        return "NO"
    if x1<x2 and v1<v2:
        return "NO"
    if v1==v2:
        return "NO"
    if (x2-x1)%(v1-v2)==0 or (x2-x1)%(v2-v1)==0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#exercise Strange Advertising-3
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 2
    cumulative= 2
    for _ in range(n-1):
        cumulative = cumulative*3//2
        shared= shared + cumulative
    return shared

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#exercise Recursive digit Sum-4
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    def sum_digit(v):
        if v < 10:
            return v
        s = sum(int(i) for i in str(v))
        return sum_digit(s)
    x= sum_digit(int(n))
    return sum_digit(x*k)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#exercise Insertion Sort-Part1-5
import math
import os
import random
import re
import sys
def insertionSort1(n, arr):
    e= arr[-1]
    arr[-1]=arr[-2]
    i = n - 2
    while True:
        print(*arr, sep = ' ')
        if arr[i-1]>e and i>0:
            arr[i]= arr[i-1]
            i-= 1
        else:
            arr[i]= e
            print(*arr, sep= ' ')
            break

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#exercise Insertion Sort-Part 2 -6
import math
import os
import random
import re
import sys
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        var_temp = arr[i]
        j = i
        while j > 0 and var_temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = var_temp
        print (' '.join(str(j) for j in arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)







