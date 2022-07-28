# https://www.acmicpc.net/problem/2941
def croatian(word : str):
    if 'c=' in word:
        word = word.replace("c=", '1')
    
    if 'c-' in word:
        word = word.replace('c-', '2')
    
    if "dz=" in word:
        word = word.replace('dz=', '3')
    
    if 'd-' in word:
        word = word.replace('d-', '4')
    
    if 'lj' in word:
        word = word.replace('lj', '5')
        
    if 'nj' in word:
        word = word.replace('nj', '6')
        
    if 's=' in word:
        word = word.replace('s=', '7')
        
    if 'z=' in word:
        word = word.replace("z=", '8')
    
    return word

word = input()
print(len(croatian(word)))