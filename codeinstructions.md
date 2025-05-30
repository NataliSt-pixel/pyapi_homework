# Правила оформления Python-кода

1. [Отступы](#1-Отступы)
2. [Точки с запятой](#2-Точки-с-запятой)
3. [Скобки](#3-Скобки)
4. [Пробелы в выражениях и инструкциях](#4-Пробелы-в-выражениях-и-инструкциях)  
   4.1. [Пробелы и скобки](#41-Пробелы-и-скобки)  
   4.2. [Пробелы рядом с запятой, точкой с запятой и точкой](#42-Пробелы-рядом-с-запятой-точкой-с-запятой-и-точкой)  
   4.3. [Пробелы вокруг бинарных операторов](#43-Пробелы-вокруг-бинарных-операторов)  
5. [Длина строк](#5-Длина-строк)
6. [Пустые строки](#6-Пустые-строки)
7. [Имена](#7-Имена)  
   7.1. [Имена функций](#71-Имена-функций)  
   7.2. [Имена модулей и пакетов](#72-Имена-модулей-и-пакетов)  
   7.3. [Имена классов](#73-Имена-классов)  
   7.4. [Имена констант](#74-Имена-констант)  
8. [Комментарии](#8-Комментарии)  
   8.1. [Блоки комментариев](#81-Блоки-комментариев)  
   8.2. [Комментарии в строке с кодом](#82-Комментарии-в-строке-с-кодом)  
   8.3. [Строки документации](#83-Строки-документации)  
9. [Циклы](#9-Циклы)  
   9.1. [Циклы по спискам](#91-Циклы-по-спискам)  
   9.2. [Циклы по списку чисел](#92-Циклы-по-списку-чисел)  
   9.3. [Циклы по спискам с индексами](#93-Циклы-по-спискам-с-индексами)  
   9.4. [Циклы по двум спискам](#94-Циклы-по-двум-спискам)  
10. [Импорты](#10-Импорты)  

## 1. Отступы
Рекомендуется использовать 4 пробела на каждый уровень отступа. Python 3 запрещает смешивание табуляции и пробелов в отступах. Код, в котором используются и те, и другие типы отступов, должен быть исправлен так, чтобы отступы в нем были расставлены только с помощью пробелов.

**Хорошо**
```python
def no_tab_using():
    no_tab = 'Using 4 spaces'
```

**Плохо**
```python
def use_tab():
	one_tab_using = 'Ugly'
```

## 2. Точки с запятой
Не разделяйте ваши строки с помощью точек с запятой и не используйте точки с запятой для разделения команд, находящихся на одной строке.

**Хорошо**
```python
a = 'String'
b = 15
c = 7.2
```
**Плохо**
```python
a = 'String';
b = 15; c = 7.2;
```

## 3. Скобки
Используйте скобки экономно. Не используйте их с выражением `return` или с условной конструкцией, если не требуется организовать перенос строки. Однако скобки хорошо использовать для создания кортежей.

**Хорошо**
```python
if budget < 0:
    return False
# -------------------
while counter <= 10:
  counter += 1
# -------------------
if sea_country and cheap_country:
    add_country_for_visit()
# -------------------
if not line:
    continue
# -------------------
return result
# -------------------
for (key, value) in dict.items(): ...
```

**Плохо**
```python
if (budget < 0):
    return (False)
# -------------------
if not(line):
    continue
# -------------------
return (result)
```

## 4. Пробелы в выражениях и инструкциях

### 4.1 Пробелы и скобки
Не ставьте пробелы внутри каких-либо скобок (обычных, фигурных и квадратных).

**Хорошо**
```python
pineapple(pine[1], {apple: 2})
```

**Плохо**
```python
pineapple( pine[ 1 ], { apple: 2 } )
```

Никаких пробелов перед открывающей скобкой, которая начинает список аргументов, индекс или срез.

**Хорошо**
```python
get_number_of_guests(1)
```

**Плохо**
```python
get_number_of_guests (1)
```

**Хорошо**
```python
dish['ingredients'] = cook_book[:3]
```

**Плохо**
```python
dish ['ingredients'] = cook_book [:3]
```

### 4.2 Пробелы рядом с запятой, точкой с запятой и точкой
Перед запятой, точкой с запятой либо точкой не должно быть никаких пробелов. Используйте пробел после запятой, точки с запятой или точки (кроме того случая, когда они находятся в конце строки).

**Хорошо**
```python
if number_of_goods == 4:
    print(number_of_goods, total_price)
```

**Плохо**
```python
if number_of_goods == 4 :
    print(number_of_goods , total_price)
```

### 4.3 Пробелы вокруг бинарных операторов
Окружайте бинарные операторы одиночными пробелами с каждой стороны. Это касается присваивания (`=`), операторов сравнения (`==`, `<`, `>`, `!=`, `<>`, `<=`, `>=`, `in`, `not in`, `is`, `is not`), и булевых операторов (`and`, `or`, `not`). Используйте, как вам покажется правильным, окружение пробелами по отношению к арифметическим операторам, но расстановка пробелов по обеим сторонам бинарного оператора придает целостность коду.

**Хорошо**
```python
counter == 1
```

**Плохо**
```python
counter<1
```

Не используйте более одного пробела вокруг оператора присваивания (или любого другого оператора) для того, чтобы выровнять его с другим.

**Хорошо**
```python
price = 1000
price_with_taxes = 1200
price_with_taxes_and_discounts = 1100
```

**Плохо**
```python
price                          = 1000
price_with_taxes               = 1200
price_with_taxes_and_discounts = 1100
```

Не используйте пробелы по сторонам знака `=`, когда вы используете его, чтобы указать на именованный аргумент или значение по умолчанию.

**Хорошо**
```python
def complex(real, imag=0.0): return magic(r=real, i=imag)
```

**Плохо**
```python
def complex(real, imag = 0.0): return magic(r = real, i = imag)
```

## 5. Длина строк
Ограничивайте длину строк 79 символами (а длину строк документации и комментариев — 72 символами). В общем случае не используйте обратный слеш в качестве перехода на новую строку. Используйте доступное в Python явное объединение строк посредством круглых и фигурных скобок. Если необходимо, можно добавить дополнительную пару скобок вокруг выражения.

**Хорошо**
```python
style_object(self, width, height, color='black', design=None,
        emphasis=None, highlight=0)

if (width == 0 and height == 0 and
    color == 'red' and emphasis == 'strong'):
```

Если ваш текст не помещается в одну строку, используйте скобки для явного объединения строк.

**Хорошо**
```python
long_string = ('This will build a very long long '
    'long long long long long long string')
```

Что касается длинных URL в комментариях, то располагайте их, если это необходимо, на одной строке.

**Хорошо**
```python
# See details at
# http://www.example.com/example/example/example/example/example/example/example_example.html
```

**Плохо**
```python
# See details at
# http://www.example.com/example/example/example/example/example/\
# example/example_example.html
```

Обратный слеш иногда используется. Например, с длинной конструкцией with для переноса блока инструкций.

**Хорошо**
```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

Ещё один подобный случай — длинные `assert`.

## 6. Пустые строки
Отделяйте функции (верхнего уровня, не функции внутри функций) и определения классов двумя пустыми строками. Определения методов внутри класса отделяйте одной пустой строкой. Две пустые строки должны быть между объявлениями верхнего уровня, будь это класс или функция. Одна пустая строка должна быть между определениями методов и между объявлением класса и его первым методом.

```python
import os
.
.
class MyClass:
.
  def __init__(self):
      self.name = 'My name'
  .
  def f(self):
      return 'hello world'
  .
  .
def MyFunc():
i = 12345
return i
.
myclass = MyClass()
```

Используйте (без энтузиазма) пустые строки в коде функций, чтобы отделить друг от друга логические части.

Python расценивает символ `control+L` как незначащий (whitespace), и вы можете использовать его, потому что многие редакторы обрабатывают его как разрыв страницы — таким образом, логические части в файле будут на разных страницах. Однако не все редакторы распознают `control+L` и могут на его месте отображать другой символ.

## 7. Имена
Имена, которых следует избегать:

* Односимвольные имена, исключая счетчики либо итераторы. Никогда не используйте символы `l` (маленькая латинская буква «эль»), `O` (заглавная латинская буква «о») или `I` (заглавная латинская буква «ай») как однобуквенные идентификаторы. В некоторых шрифтах эти символы неотличимы от цифры один и нуля. Если очень нужно `l`, пишите вместо неё заглавную `L`.

**Хорошо**
```python
long_name = 'Хорошее имя переменной'
L = 'Допустимо, но лучше избегать'
```

**Плохо**
```python
l = 1
I = 1
O = 0
```
* Дефисы и подчеркивания в именах модулей и пакетов.

**Хорошо**
```python
import my_module
```

**Плохо**
```python
import my-module
```

* Двойные подчеркивания (в начале и конце имен) зарезервированы для языка.

**Хорошо**
```python
my_variable = 'Variable'
```

**Плохо**
```python
__myvariable__ = 'Variable'
```

### 7.1 Имена функций
Имена функций должны состоять из маленьких букв, а слова разделяться символами подчеркивания — это необходимо, чтобы увеличить читабельность.

**Хорошо**
```python
my_variable = 'Variable'
```

**Плохо**
```python
My-Variable = 'Variable'
```

Стиль mixedCase допускается в тех местах, где уже преобладает такой стиль — для сохранения обратной совместимости.

### 7.2 Имена модулей и пакетов
Модули должны иметь короткие имена, состоящие из маленьких букв. Можно использовать символы подчёркивания, если это улучшает читабельность. То же самое относится и к именам пакетов, однако в именах пакетов не рекомендуется использовать символ подчёркивания.

Так как имена модулей отображаются в имена файлов, а некоторые файловые системы являются нечувствительными к регистру символов и обрезают длинные имена, очень важно использовать достаточно короткие имена модулей — это не проблема в Unix, но, возможно, код окажется непереносимым в старые версии Windows, Mac, или DOS.

**Хорошо**
```python
import vkapi
```

**Плохо**
```python
import My-First-VKontakte-API-Modul
```

### 7.3 Имена классов
Все имена классов должны следовать соглашению CapWords почти без исключений.

```python
class MyFirstClass:
```

Иногда вместо этого могут использоваться соглашения для именования функций, если интерфейс документирован и используется в основном как функции.

Обратите внимание, что существуют отдельных соглашения о встроенных именах: большинство встроенных имен — одно слово (либо два слитно написанных слова), а соглашение CapWords используется только для именования исключений и встроенных констант.

Так как исключения являются классами, к исключениями применяется стиль именования классов. Однако вы можете добавить Error в конце имени (если, конечно, исключение действительно является ошибкой).

### 7.4 Имена констант
Константы обычно объявляются на уровне модуля и записываются только заглавными буквами, а слова разделяются символами подчеркивания.

```python
MAX_OVERFLOW = 10
TOTAL = 100
```

## 8. Комментарии
Комментарии, противоречащие коду, хуже, чем отсутствие комментариев. Всегда исправляйте комментарии, если меняете код!

Комментарии должны быть законченными предложениями. Если комментарий — фраза или предложение, первое слово должно быть написано с большой буквы, если только это не имя переменной, которая начинается с маленькой буквы (никогда не отступайте от этого правила для имен переменных).

Ставьте два пробела после точки в конце предложения.

Если вы — программист, не говорящий по-английски, то всё равно следует использовать английский язык для написания комментариев. Особенно, если нет уверенности на 120% в том, что этот код будут читать только люди, говорящие на вашем родном языке.

### 8.1 Блоки комментариев
Блок комментариев обычно объясняет код (весь или только некоторую часть), идущий после блока, и должен иметь тот же отступ, что и сам код. Каждая строчка такого блока должна начинаться с символа `#` и одного пробела после него (если только сам текст комментария не имеет отступа).

Абзацы внутри блока комментариев разделяются строкой, состоящей из одного символа `#`.

### 8.2 Комментарии в строке с кодом
Старайтесь реже использовать подобные комментарии.

Такой комментарий находится в той же строке, что и инструкция. «Встрочные» комментарии должны отделяться хотя бы двумя пробелами от инструкции. Они должны начинаться с символа `#` и одного пробела.

Комментарии в строке с кодом не нужны и только отвлекают от чтения, если они объясняют очевидное.

**Плохо**
```python
counter = counter + 1                 # Increment counter
```

### 8.3 Строки документации
Соглашения о написании хорошей документации (docstrings) зафиксированы в [PEP 257](https://www.python.org/dev/peps/pep-0257/).

Пишите документацию для всех публичных модулей, функций, классов, методов. Строки документации необязательны для приватных методов, но лучше написать, что делает метод. Комментарий нужно писать после строки с `def`.

Очень важно, чтобы закрывающие кавычки стояли на отдельной строке. А еще лучше, если перед ними будет ещё и пустая строка.

**Хорошо**
```python
"""Return something useful

Optional plotz says to frobnicate the bizbaz first.

"""
```

Для однострочной документации можно оставить `"""` на той же строке.

## 9. Циклы

### 9.1 Циклы по спискам
Если нам необходимо в цикле пройти по всем элементам списка, то хорошим тоном (да и более читаемым) будет такой способ:

**Хорошо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print(color)
```

И хотя бывалые программисты или просто любители C могут использовать и такой код, это моветон.

**Плохо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(colors[i])
```

А если нужно пройти по списку задом наперед, то лучше всего использовать метод `reversed`:

**Хорошо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for color in reversed(colors):
    print(color)
```

Вместо того чтобы писать избыточный код, который и читается-то не очень внятно.

**Плохо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)-1, -1, -1):
    print(colors[i])
```

### 9.2 Циклы по списку чисел
Если есть необходимость пройти в цикле по ряду чисел, то метод range будет намного приемлемее, как минимум потому, что этот метод потребляет намного меньше памяти, чем вариант в блоке «Плохо». А представьте, что у вас ряд из трёх миллиардов последовательных чисел!

**Хорошо**
```python
for i in range(6):
    print(i**2)
```

**Плохо**
```python
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)
```

### 9.3 Циклы по спискам с индексами
Метод `enumerate` позволяет получить сразу индекс и значение из списка, что, во-первых, предоставляет множество возможностей для дальшнейшего проектирования, а во-вторых, такой код легче читается и воспринимается.

**Хорошо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, '-->', color)
```

**Плохо**
```python
colors = ['red', 'green', 'blue', 'yellow']
for i in range(len(colors)):
    print(i, '-->', colors[i])
```

### 9.4 Циклы по двум спискам
Используя метод `zip`, мы получаем из двух списков один список кортежей, что более удобно для дальнейшего использования и требует меньше памяти. Да и просто этот вариант более элегантный.

**Хорошо**
```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
for name, color in zip(names, colors):
    print(name, '-->', color)
```

**Плохо**
```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])
```

## 10. Импорты
Каждый импорт, как правило, должен быть на отдельной строке.

**Хорошо**
```python
import os
import sys
```

**Плохо**
```python
import sys, os
```

В то же время, можно писать так:

**Хорошо**
```python
from subprocess import Popen, PIPE
```

Импорты всегда располагаются в начале файла, сразу после комментариев уровня модуля, строк документации, перед объявлением констант и объектов уровня модуля. Импорты должны быть сгруппированы в порядке от самых простых до самых сложных:

* импорты из стандартной библиотеки,
* сторонние импорты,
* импорты из библиотек вашего приложения.

Наряду с группированием, импорты должны быть отсортированы лексикографически, нерегистрозависимо, согласно полному пути до каждого модуля.

**Хорошо**
```python
import foo
from foo import bar
from foo.bar import baz
from foo.bar import Quux
from Foob import ar
```

Рекомендуется абсолютное импортирование, так как оно обычно более читаемо и ведет себя лучше (или, по крайней мере, даёт понятные сообщения об ошибках), если импортируемая система настроена неправильно (например, когда каталог внутри пакета заканчивается на `sys.path`).

**Хорошо**
```python
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

Тем не менее, явный относительный импорт является приемлемой альтернативой абсолютному импорту, особенно при работе со сложными пакетами, где использование абсолютного импорта было бы излишне подробным.

**Хорошо**
```python
from . import sibling
from .sibling import example
```

Следует избегать шаблонов импортов (`from import *`), так как они делают неясным то, какие имена присутствуют в глобальном пространстве имён, что вводит в заблуждение как читателей, так и многие автоматизированные средства.

Рекомендуем также ознакомиться с [полной версией](https://www.python.org/dev/peps/pep-0008/) соглашения о том, как писать код на Python (PEP 8)