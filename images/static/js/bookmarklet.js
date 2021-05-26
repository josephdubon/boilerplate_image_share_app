/*
*This is the main jQuery loader script. It takes care of using jQuery if it
* has already been loaded on the current website. If jQuery is not loaded, the
* script loads jQuery from Google's content delivery network (CDN), which hosts
* popular JavaScript frameworks. When jQuery is loaded, it executes the bookmarklet()
* function that will contain your bookmarklet code. Also, set some variables at the top of the file:
    - jquery_version: The jQuery version to load
    - site_url and static_url: The base URL for your website and the base URL for static files
    - min_width and min_height: The minimum width and height in pixels for the images that your
    * bookmarklet will try to find on the site
* */

(function () {
    const jquery_version = '3.4.1';
    const site_url = 'https://127.0.0.1:8000/';
    const static_url = site_url + 'static/';
    const min_width = 100;
    const min_height = 100;

    function bookmarklet(msg) {
        /**
         *
         You load the bookmarklet.css stylesheet using a random number as a parameter
         to prevent the browser from returning a cached file.
         You add custom HTML to the document <body> element of the current website.
         This consists of a <div> element that will contain the images found on the current website.
         You add an event that removes your HTML from the document when the user clicks on the close
         link of your HTML block. You use the #bookmarklet #close selector to find the HTML element
         with an ID named close, which has a parent element with an ID named bookmarklet. jQuery selectors
         allow you to find HTML elements. A jQuery selector returns all elements found by the given CSS
         selector. You can find a list of jQuery selectors at https://api.jquery.com/category/selectors/.
         *
         **/
        const css = jQuery('<link>');
        css.attr({
            rel: 'stylesheet',
            type: 'text/css',
            href: static_url + 'css/bookmarklet.css?r=' + Math.floor(Math.random() * 99999999999999999999)
        });
        jQuery('head').append(css);
        // load HTML
        box_html = '<div id="bookmarklet"><a href="#" id="close">&times;</a><h1>Select an image to bookmark:</h1><div class="images"></div></div>';
        jQuery('body').append(box_html);
        // close event
        jQuery('#bookmarklet #close').click(function () {
            jQuery('#bookmarklet').remove();
        });
        // find images and display them
        jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
            if (jQuery(image).width() >= min_width && jQuery(image).height()
                >= min_height) {
                image_url = jQuery(image).attr('src');
                jQuery('#bookmarklet .images').append('<a href="#"><img src="' +
                    image_url + '" /></a>');
            }
        });

    };
    // Check if jQuery is loaded
    if (typeof window.jQuery != 'undefined') {
        bookmarklet();
    } else {
        // Check for conflicts
        const conflict = typeof window.$ != 'undefined';
        // Create the script and point to Google API
        const script = document.createElement('script');
        script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
            jquery_version + '/jquery.min.js';
        // Add the script to the 'head' for processing
        document.head.appendChild(script);
        // Create a way to wait until script loading
        let attempts = 15;
        (function () {
            // Check again if jQuery is undefined
            if (typeof window.jQuery == 'undefined') {
                if (--attempts > 0) {
                    // Calls himself in a few milliseconds
                    window.setTimeout(arguments.callee, 250)
                } else {
                    // Too much attempts to load, send error
                    alert('An error occurred while loading jQuery')
                }
            } else {
                bookmarklet();
            }
        })();
    }
})()
