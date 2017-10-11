from django.shortcuts import render

# Create your views here.

def demo(request):
    context={
        'list1':[1,2,3,4,5,'6','7'],
        'num':10,
        'times':100,
        'types':[0,1,2,2,2,1,1,0],
        'src_str':'aaabbbcccaaabbbcccaaa',
    }
    return render(request,'generalfilters/demo.html',context)