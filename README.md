# paultohtml
Let's say you have an html page in one language, and you want to offer this page in another language.
You have several possibilities but two common ones are :
1) I create two html files, one for each language
2) I use gettext and I create a po files to store my translations

## It is bad 

1) It is bad because whenever you want to change something in one file you have to open the other one and make the same change
2) It is bad because you have to open two files at the same time, and find for the line you want to change where is it in the po files. And it is rendered at run time, so everytime you display the page you have to render it (well you can have cache)

## Two problems
* Not easy to maintain
* Two files to maintain

## How to fix that problem ?

 
Learning three keywords :
``` 
<%%% 
%%% 
%%%>
```

`<%%%` Indicate the beginning of a block of text to translate<br>
`%%%>` Indicates the end of a block of text to translate<br>
`%%%` separate the different languages<br>

In order to indicate in which language is the text of a segment you have to specify his acronym like `en` for english

So if you have an initial html file like that
```html
<h1> I go home </h1>
<p> But it is not that far
I can go there by walk</p>
```

And you want to translate it into french you have to write :
```html
<h1> <%%%en I go home  %%%fr Je rentre chez moi %%%></h1>
<p> <%%%en But it is not that far
I can go there by walk %%%fr Mais ce n'est pas loin
Je peux y aller en marchant %%%></p>
```


And the last thing you have to do is two generate the two html files with :
```
python paultohtml.py name_of_the_file.html en fr
```

```en fr``` to indicate you want to generate these two languages

and it will output two files :
```
name_of_the_file_en.html
```
```html
<h1> I go home </h1>
<p> But it is not that far
I can go there by walk</p>
```
And
```
name_of_the_file_fr.html
```
```html
<h1> Je rentre chez moi </h1>
<p> Mais ce n'est pas loin
Je peux y aller en marchant</p>
```

## BUT
This is not intended to replace gettext for big websites, but if you have a few pages and only 2 or 3 languages supported it  is much easier.
