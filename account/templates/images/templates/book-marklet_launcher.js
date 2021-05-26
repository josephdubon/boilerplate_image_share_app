/*
* Script discovers whether the bookmarklet has already been loaded by checking whether the
* myBookmarklet variable is defined. By doing so, you avoid loading it again if the user clicks on
* the bookmarklet repeatedly. If myBookmarklet is not defined, you load another JavaScript file by
* adding a <script> element to the document. The script tag loads the bookmarklet.js script using a
* random number as a parameter to prevent loading the file from the browser's cache. The actual bookmarklet
* code resides in the bookmarklet.js static file. This allows you to update your bookmarklet code without
* requiring your users to update the bookmark they previously added to their browser.
* */

(function () {
    if (window.myBookmarklet !== undefined) {
        myBookmarklet()
    } else {
        document.body.appendChild(
            document.createElement(
                'script'))
            .src = 'http://127.0.0.1:8000/static/js/bookmarklet.js?r=\'+Math.floor(Math.random()*99999999999999999999)'
    }
})