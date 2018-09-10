# NLFM: Non-Linear File Manager

## Dependencies
* PanTidDoc
 * Cloned from GitHub, called `PanTidDoc-master`
 * set `flag2` to 0 (SHOULD ADD ARGUMENT)
* Tesseract: `sudo apt-get install tesseract-ocr`
* Pillow: `sudo pip3 install pillow`
* PyTesseract: `sudo pip3 install pytesseract`
* OpenCV: `sudo apt-get install python-opencv`
* OpenCV-python: `sudo pip3 install opencv-python`


## Configuration
* create `/tiddlers/` to hold newly generated tiddler files
* edit `definitions.json` to classify files however you like
* edit `blacklist.txt` to skip over certain directories


## Running
* Convert `.tid` files: `tiddlywiki --rendertiddler $:/core/save/all index.html text/plain` (MAY BE UNNECESSARY)
* Start the server: `tiddlywiki --server`
* Adding files requires restarting the server


## TODOS
* Create tiddlers for tags if don't already exist; contain list of all tiddlers with tag
* Add image OCR and wrapper tiddler (Google Vision?)
* Use a script to control the TiddlyWiki server; restart after adding files


https://stackoverflow.com/questions/18246053/how-can-i-create-a-link-to-a-local-file-on-a-locally-run-web-page#18246357
