
# My Website -- [Nellie's Noodles](http://nelliesnoodles.pythonanywhere.com/)




First commit and blog page setup taught in:

Django Girls @ https://tutorial.djangogirls.org/en/deploy/?q=

I have gone passed the point of the tutorial and am now setting up my own work on the site.

Settings.py file has been set to gitignore.

# Projects on this site:
> ###  blog 
> Django WEb app in site: blog
>
> #### Description:
> In my first attempt at creating a Django website, the blog was set up originally with bootstrap.
> See Django Girls tutorial link above to try one of your own.  
> This now holds info about what is going on with the site, it's projects and me.

> ### Whispering Wall 
> Django Web app in site: WIWA
> #### Description:
> A python NLTK [Natural Learning Toolkit](https://www.nltk.org/) chatbot
> 
> After the NLTK has tagged and separated parts of speech in a users input,
>
> The wiwa code uses scripts and logic evaluation of user input to pick a random script, and a line from the script in reply.
> Some scripts have simple sentences, and some scripts use tagged words from the user input to make the reply seem interactive.

> ### Word Finder
> Part of the initial web app in site: blog
> #### Description:
> This uses python import enchant to look words up in a dictionary.
> If the word is not found, code asks enchant to produce a list of 'similarly' spelled words.
> 
> file: speller_web.py
>
> At the bottom of the screen, users can type in a word to have NLTK retrieve a definition.
> This is run by a function in the views.py of blog directory: get_definition(request)

> ### NIM game
> web app directory: nim
> First vanilla JavaScript experiment used to create a game I found interesting from a mathmatical twitter post link.
> [Youtube video of mathmatical explanation of NIM](https://www.youtube.com/watch?v=niMjxNtiuu8)
> 
> A two player game, the way to win, is to NOT end up with the last card on the table. 
> 
> I may visit making this more interactive and User friendly in the future.
> For now it was just to learn, and have fun.

> ### Testing JavaScript Files
> web app directory: jstests
> A simple experiment used to test how javascript interacts with the page, and changing object orientation 
> on the page through styling  of an element. 

> ### StatsClass
> web app directory: StatsClass
> Not yet fully published, work in progress. 
> 
> #### Description:
> This will be a place for people studying statistics to play with changing, getting, and analyzing statistical data.
> 
> At this time, it accepts ten fields and will tell you the probability within those ten what each event has to happen.
> Simple division.   
> There is a lot more complex math to be done here, and hope to add more to it soon. 
> To see what it has so far:
> [StatsClass Home Page](http://nelliesnoodles.pythonanywhere.com/StatsClass)


### Plans / TO-DO ###
* Add more whispering wall content
* Add some python GUI or animation project
* Learn Javascript -- add more responsive design
* Personalize and style the site as I go
* Keep adding pieces of everything I can do and learn to showcase my programming abilities
* Add links to all my online work so I can use this as a resume
