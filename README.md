# AutomateCatalog
Automate updating catalog information for an online store. Develop a system that will update the catalog information with data provided by the suppliers for an online store.

<ins>**Project tasks:**</ins>


<ins>**Task 1:**</ins>  Upload the new products to the online store. Images and descriptions should be uploaded separately, using two different web endpoints.

(The suppliers send the data as large images with an associated description of the       products in two files (.TIF for the image and .txt for the description).)
  
   a)  The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. 
  
   b)  The contents of the HTML file need to be uploaded to a web service that is already running using Django. 
  
   c)  Gather the name and weight of all items from the .txt files and use a Python request to upload it to your Django server.
  
  d)  Create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

<ins>**Task 2:**</ins> Once the task 1 is complete, send a report back to the supplier, letting them know what you imported.

   a)   the supplier should be notified with an email that indicates the total weight of items (in lbs) that were uploaded. 
   
   b) The email should have a PDF attached with the name of the item and its total weight (in lbs). 

Finally, in parallel to the automation running, check the health of the system and send an email if something goes wrong. 

<ins>**Task 3:**</ins> Run a script on your web server to monitor system health.

<ins>**Task 4:**</ins> Send an email with an alert if the server is ever unhealthy.

