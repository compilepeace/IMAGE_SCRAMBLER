# scrambler_tool

Hello, this is a tool uses Restricted algorithm to encrypt/decrypt (albeit not by using any key based
algorithms) all the files in a directory location, which is provided by the user. It uses BASH (Bourne 
Again SHell) scripting and python. There is no such commercial purpose of working on this tool, it was 
just made to scramble image files which are fairly small in size and can easily be encoded/decoded. The
larger files (for instance) can't be encoded/decoded with this tool efficiently. 
    
    
This tool uses the 'xxd' utility (converting the file into its hexdump or reverse), then it changes the
ASCII values of the hexdump recieved. Main is written in BASH scripts which calls encrypt.py as well as
decrypt.py according to what the user's needs are.
    
Righ now, it is made such that given the path of the directory, it will encrypt all the files in that 
directory but will not encrypt if path to a particular file is given rather than a directory.
    
Any suggestions and contributions will be appreciated.
    
    
Cheers,
