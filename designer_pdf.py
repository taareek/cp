

def designerPdfViewer(h, word):
    # Write your code here
    word_len = len(word)
    max_height = 0
    
    for letter in word:
        max_height = max(max_height, h[ord(letter) - ord('a')])
        
    area = max_height * word_len
    return area

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
name = 'tarek'

area = designerPdfViewer(h, name)

print(area)