# package_relion_project
package the files necessary to move a relion project to a different system
./package_relion_project.py <particles starfile>

it will generate a zip archive called relion-packet.tar.gz.  This archive contains only the files necessary to process the data in that star file.

Copy the archive into your project directory on the new system unpack it with:

tar xvf relion-packet.tar.gz

It will rebuild the directory structure and put all the files in the right places  so all you need to do is import the star file into relion and go.
This also has the advantages of only copying the files you actually need, and compressing them, so it should overall make the transfer much faster.
