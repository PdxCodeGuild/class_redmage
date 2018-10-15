# VSCode Cheatsheet

VSCode is a Microsoft's open source text editor written using JavaScript and the Electron Framework.

For the rest of this cheatsheet the name `Ctrl` to denote either the Windows/Linux `Ctrl`, replace with `⌘` if you're on OS X unless specified otherwise.

## The command palette

To access the command palette you enter the following shortcut:

`Ctrl+Shift+P`

This will bring up a window at the top of your editor with the `>` symbol already in it. This is where you can search for and run a huge set of commands that come with VSCode by default. It also is a place where you can run commands from plug-ins you've installed.

Removing the `>` will actually allow you to search for files in your curently opened project folder and open them in the currently opened window.

Press enter to use either functionality

#### Some useful commands

* `Reindent Lines` This will automatically indent and prettify weird of misaligned indentation automatically (it's not always exactly right).
* `Terminal: Create New Integrated Terminal` This will actually create a Terminal/PowerShell panel inside your editor window.

## Manipulating text

VSCode and most editors/IDEs have keyboard shortcuts to help make manipulating and altering text easier.

Here's a few super helpful shortcuts:

* `Select multiple lines of text + Tab` Tab not only adds a tab character where specified, if you select some lines of code you can indent all of them together.
* `Select multiple lines of text + Shift+Tab` This functions the same as above but in the opposite direction, this will dedent your code.
* `Select any text + Ctrl+D` This will create multiple cursors (one at a time) around matching occurrence of the text selected. This can be super helpful for renaming variables in larger sets of code.
* `Ctrl+F` This will bring up the find panel, the find panel also has a bunch of different settings for how you want to match including ignoring capitalization, or even using RegEX
* `Ctrl+H` Will bring up the find panel, but also give you the option to replace occurrence of the found string/pattern.
* `Alt+Up and Alt+Down` this allows you to move either the currently selected line of code or multiple lines of code up or down in the file. It will move lines not inside of the selection around it.

## Plug-ins, Snippets & Productivity

VSCode has a marketplace you can use to install all sorts of cool and productive tools to make your life easier. In this class I advise you use the `Python` plug-in, if you installed VSCode with Anaconda you might already have this installed and configured! Otherwise you can install this yourself.

VSCode also comes with a collection snippets that allow you to avoid writing simple boilerplate code for things you write a lot. You can also create and download snippets of code you find yourself frequently writing.

#### Suggested Plug-ins

* `Todo+` (Super helpful for keeping track of goals and leaving a papertrail for other people watching your progress)
* `Python-autopep8` Automatically formats your python code to comply to the pep8 standard
* `Prettier` Will help with formatting unruley or huge lines of text

## Themes

VSCode comes with a few themes by default, but you can extend/download more to your heart's content. Themes are a very aesthetic thing and vary wildly between developers.

To get to the theme selection open the `Command Panel` and search for `color theme` you can also set the themes for icons if you please this can be found by using the `Command Panel` and searching for `icon theme`

Pick whichever one is easiest to read, but also make sure that the color scheme fits what you like! You have full control here.
