import imageio
frames = []
for i in [9,19,29,39,49,59,69]:
    print("./result_%d.jpg" % i)
    im = imageio.imread("./result_%d.jpg" % i)
    frames.append(im)
imageio.mimsave("result.gif",frames,'GIF',duration = 0.1)
