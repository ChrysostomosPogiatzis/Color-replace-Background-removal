from PIL import Image
import sys
print('''
--    _____                               _____      _               _____ _                                  
--   |_   _|                             / ____|    | |             / ____| |                                 
--     | |  _ __ ___   __ _  __ _  ___  | |     ___ | | ___  _ __  | |    | |__   __ _ _ __   __ _  ___ _ __  
--     | | | '_ ` _ \ / _` |/ _` |/ _ \ | |    / _ \| |/ _ \| '__| | |    | '_ \ / _` | '_ \ / _` |/ _ \ '__| 
--    _| |_| | | | | | (_| | (_| |  __/ | |___| (_) | | (_) | |    | |____| | | | (_| | | | | (_| |  __/ |    
--   |_____|_| |_| |_|\__,_|\__, |\___|  \_____\___/|_|\___/|_|     \_____|_| |_|\__,_|_| |_|\__, |\___|_|    
--                           __/ |                                                            __/ |           
--                          |___/                                                            |___/   
By Chrysostomos Pogiatzis 2019          '''
);
image=input(str("Enter the name  of the Image: "))
img = Image.open(image)
img = img.convert("RGBA")

pixdata = img.load()
color=input(str("Enter the hex code of the  color you want to replace: exmp.ffffff=white "))

new_color=input(str("Enter the new color : "))
transperant=input(str("Do you want the new color to be trasperant:yes/no "))

# Clean the background noise, if color != white, then set to black.

def split(s, chunk_size):
    a = zip(*[s[i::chunk_size] for i in range(chunk_size)])
    return [''.join(t) for t in a]


a=split(color, 2)
print("Red: "+str(int(a[0],16)));
print("Green: "+str(int(a[1],16)));
print("Blue: "+str(int(a[2],16)));

b=split(new_color, 2)
print("Red: "+str(int(b[0],16)));
print("Green: "+str(int(b[1],16)));
print("Blue: "+str(int(b[2],16)));
print("Transperant: "+transperant);
print("Height: "+str(img.size[1]));
print("width: "+str(img.size[0]));
if (transperant=="yes"):
	image=(int(b[0],16), int(b[1],16), int(b[2],16),0);
else:
	image=(int(b[0],16), int(b[1],16), int(b[2],16),255);

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y] == (int(a[0],16), int(a[1],16), int(a[2],16),255):
           pixdata[x, y] = image;
img.save('Foto.png')

                                                                                                                        
                                                                                                                            
                                                                                                                            
