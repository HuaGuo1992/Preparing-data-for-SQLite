## 1. Introduction to the Data ##

raw_hamlet = sc.textFile('hamlet.txt')
raw_hamlet.take(5)

## 2. The Map Method ##

split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))

## 4. The FlatMap Method ##

def hamlet_speaks(line):
    id = line[0]
    speaketh = False
    
    if "HAMLET" in line:
        speaketh = True
    
    if speaketh:
        yield id,"hamlet speaketh!"

hamlet_spoken = split_hamlet.flatMap(lambda x: hamlet_speaks(x))
# hamlet_spoken.take(10)

## 5. Filter Using a Named Function ##

def filter_hamlet_speaks(line):
    if 'HAMLET' in line:
        return True
    return False

hamlet_spoken_lines = split_hamlet.filter(lambda line: filter_hamlet_speaks(line))
hamlet_spoken_lines.take(5)

halmet_spoken_lines = split_hamlet.filter(filter_hamlet_speaks)



























## 6. Actions ##

spoken_count = 0
spoken_101 = list()

spoken_count = hamlet_spoken_lines.count()
spoken_101 = hamlet_spoken_lines.collect()[100]
