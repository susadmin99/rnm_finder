Rick and Morty character finder.
Website: 

API I used in the project: https://rickandmortyapi.com/

The projects main goal is to showcase all of the characters of the popular cartoon series "Rick and Morty".
It includes features such as searching for a specific character, paginated table (20 characters per page), a seperate "Profile" page which collects all the important data for the selected character.

Project uses Python with Flask for the backend part and html, css, javascript and Tailwind CSS.
I chose python and flask because for a long time I wanted to try the python backed webapp.

Currently I know about one feature which is not added yet to the project and that it's can't do character search on the whole API but it can only search from characters listed in the table's current page.

How to run the project: 
1. Download the project
2. Run app.py (inside the src directory) (it starts the webserver)
3. Open local address with the port number:7342 (site: 127.0.0.1:7342)
    a. If you'd like to use different port number, you can change it in the app.py

Test cases:
1. Check the console if there is any errors when loading the website.
2. Check the functionalities such as testing the main tasks the site does.
    a. Showing the characters on the table.
    b. The openning of the "Profile" page is successful with all the required data from the clicked character.
    c. The pagination is working on the "Home" page, it can go until 42 pages (thats the max the api has)
    d. Can the table show the avatar
    e. What does the website do when there is no data coming from the api, such as an incoming type is null in the api the site should render nothing.
3. Test the UX by visiting the site from different devices with different screen sizes. (responsiveness)
4. Test the site from different web-browsers due to how differently can browser handle html and javascript.
5. Performance test the site that the loading doesn't take forever.
