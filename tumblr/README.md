## Ebook tools for tumblr

To use the tumblr API you will need an API key. You can get one just by registering a free account and the filling out this form: [https://www.tumblr.com/oauth/register](https://www.tumblr.com/oauth/register)

Then set your API key in `get_contents.py`.


### Example

You can set the blog in the `get_contents.py` script and set an additional filter for tags. Currently it's set to catch the english translation of *Kumo Desu ga, Nani Ka?* / *I'm A Spider, So What?*. Of course, other blogs will probably format their posts differently, so you may have to adjust some settings.

    python get_contents.py

The entries will be saved to the `downloads` directory.

In the script `html2epub.sh` you can set an author, cover, tags and book title, then call it. Warning: If the cover file cannot be found, the script will fail.

    ./html2epub.sh

The script will create a file `chapters.epub` in the same directory as the script.
