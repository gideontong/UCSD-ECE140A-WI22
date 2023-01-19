# Lab 3

> Gideon Tong (PID: A15960885)

## Tutorials

### Tutorial 1: Numpy

In this tutorial we learned about how to initialize an array and lists using numpy, and how to restructure an array. We learned how to resize them and index them as well.

1. Size 4
2. `hstack`
3. `hstack(2).vstack(2)`
4. `arange(-3, 15, 6)`
5. `linspace(0, 100, 49)`. It is different because it determines the number of steps rather than the step size.
6. See code below.

```py
array6 = np.zeros((3, 4))
array6[0] = [12, 3, 1, 2]
array6[1, 0] = 0
array6[:, 1] = [3, 0 ,2]
array6[2, :2] = [4 ,2]
array6[2, 2:] = [3 ,1] 
array6[:, 2] = [1 ,1, 3]
array6[1, 3] = 2
```

### Tutorial 2: OpenCV

In this tutorial we learned about how to use OpenCV to do image processing.

1. See code below.
   ```py
   img = cv2.imread('./images/geisel.jpg')
   img[:, :, 0] = 255 - img[:, :, 0]
   ```
2. See code below.
   ```py
   print(img.shape)
   img = cv2.resize(img, (img.shape[0] * 0.5, img.shape[1]))
   ```

### Tutorial 3: Your Own Web Server

I learned how to start my own webserver with Pyramid and to write and serve HTML files with my own Python Pyramid web server as well. I learned about some of the basic functions in Pyramid.

### Tutorial 4: Your Own REST Server

I learned how to start a REST server and serve not only HTML pages and content for the web but also REST data and JSON data that computers can query and understand as well.

## Challenges

### Challenge 1: My Local Portfolio

In this challenge I created a portfolio which was really similar to the challenge I made in the previous lab, except I served it with a Python webserver instead of using pure HTML files.

### Challenge 2: The Triton Gallery

In this lab I made a gallery of Triton images and we calculated the price and displayed it to the user using Javscript and HTML and served it using Pyramid Python.
