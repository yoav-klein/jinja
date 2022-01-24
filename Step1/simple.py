
### This demonstrates a very basic usage of jinja
### Taken from https://realpython.com/primer-on-jinja-templating/

from jinja2 import Template

t = Template("Hello {{ something }}!")
print(t.render(something="World"))

t = Template("My favorite numbers: {% for n in range(10) %}{{n}}, {% endfor %}")
print(t.render())