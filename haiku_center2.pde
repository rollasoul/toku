PImage img;

void setup() {
  size(410, 400);
  fill(0);
  background (255, 255, 255);
  img = loadImage("/home/pi/imageToSave1.png");
}

void draw() {
  int iStart = new Float(img.height/3).intValue();
  int iHeight = img.height-iStart;
  copy(img, 0, 0,img.width,2*iStart,50,0,img.width,iHeight);
  save("nunuimageToSave2.png");
}