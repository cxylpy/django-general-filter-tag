# django-general-filter-tag
useful custom django tags and filters.

# Demo
#### code  
num = 10, { { num|divide:"5" } }  
#### result  
2.0  

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
