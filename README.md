# django-general-filter-tag
useful custom django tags and filters.

# Demo
### divide  
num = 10  
{ { num|divide:"5" } }  
### result  
2.0  
### append    
times = 100, { { times|append:" times"} }  
### result  
100 times  
### describe  
types = [0,1,2,2,2,1,1,0],{ {type|describe:"0:typeA,1:typeB,2:typeC"} }  
### result  
typeA typeB typeC typeC typeC typeB typeB typeA   
### exclude_str  
src_str='aaabbbcccaaabbbcccaaa', { { src_str|exclude_str:'a' } }  
### result  
bbbcccbbbccc    
# Install
pip install django-general-filters

#Quick start

1. Add "generalfilters" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'generalfilters',
    ]

2. Load the general_filters filter in your templates like this::

    {% load general_filters %}
