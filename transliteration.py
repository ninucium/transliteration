import re
import os

## Transliteration rule
dict_letters = {'ий':'y', 'а':'a', 'б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh',
              'з':'z','и':'i', 'й':'y','к':'k','л':'l','м':'m','н':'n','о':'o',
              'п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts',
              'ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e','ю':'yu',
              'я':'ya', ' ': ' '}

## Reading names in russian
file_name = input('Enter path to the file = ')
start_path = os.path.abspath(file_name)

try:
    file = open(start_path)
except (FileNotFoundError,OSError) as e:
    print('Error: %s' % e)
    quit()

try:
    buffer = file.read()
    file.close()
    names = re.split(r'\n', buffer)

    ## Creating output file
    end_path = os.path.join(os.path.dirname(start_path), re.split('[.]',os.path.basename(start_path))[0] + '_english.txt')
except NameError as e:
    print('Error: %s' % e)
    quit()

try:    
    end_file = open(end_path, 'w')
    end_file.close()
except:
   print('Error')
   quit()

try:
    ## Transliteration
    for name in names:
        english_name = ''
        ## Lower case for not creating dict to Upper case
        name = name.lower()
        ## One additional rule - replacing to y. Cause I like to use 'y' instead of 'ij',
        ## but that rule could be deleted.
    
        name = name.replace('ий','y')
        for letter in name:
            if dict_letters.get(letter) is not None:
                english_name = english_name + str(dict_letters.get(letter))
            else:
                ## Passing the y letter
                english_name = english_name + letter
        ## Capitalizing both words
        english_name = ' '.join(word[0].upper() + word[1:] for word in english_name.split())
        end_file = open(end_path, 'a')
        end_file.write(english_name + '\n')
        end_file.close()

    ## Closing file
    end_file.close()
    print('\n\nFile has been saved to {}'.format(end_path))
    
except:
    print('\n\nError with transliteration')

