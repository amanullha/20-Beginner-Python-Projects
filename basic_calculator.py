def add(a,b):
    ans=a+b
    print (f'{str(a)} + {str(b)} = {str(ans)}')
    
def sub(a,b):
    ans=a-b
    print (f'{str(a)} - {str(b)} = {str(ans)}')

def mul(a,b):
    ans=a*b
    print (f'{str(a)} * {str(b)} = {str(ans)}')

def div(a,b):
    ans=a//b
    print (f'{str(a)} // {str(b)} = {ans}')


while True:
    c=int(input("select: "))
    match c:
        case 1:
            div(8,5)
        case 2:
            sub(5,2)