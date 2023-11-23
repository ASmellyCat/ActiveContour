import cv2
import numpy as np
from scipy import interpolate
import json

from external_energy import external_energy
from internal_energy_matrix import get_matrix

def click_event(event, x, y, flags, params):
    # Checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        #save point
        xs.append(x)
        ys.append(y)

        #display point
        cv2.circle(img_copy, (x, y), 3, 80, -1)
        cv2.imshow('image', img_copy)

def interpolate_points(input_x, input_y, num_points):
    combined_data = np.column_stack((input_x, input_y))
    tck, u = interpolate.splprep(combined_data.T, s=0, per=0, k=1)
    u_new = np.linspace(u.min(), u.max(), num_points)
    interpolated_x, interpolated_y = interpolate.splev(u_new, tck, der=0)
    return interpolated_x, interpolated_y


def bilinear_interpolation(grad, x, y):
    # Bilinear interpolation
    x1, y1 = int(x) , int(y)
    x2, y2 = x1 + 1, y1 + 1
    # Interpolate values into mid point
    interpolated_value = (grad[y1, x1] * (x2 - x) * (y2 - y) +
                          grad[y1, x2] * (x - x1) * (y2 - y) +
                          grad[y2, x1] * (x2 - x) * (y - y1) +
                          grad[y2, x2] * (x - x1) * (y - y1))

    return interpolated_value

def optimize_contour(xs, ys, M, grad_x, grad_y, kappa, gamma):
    # Get optimized x, y
    f_x = np.array([bilinear_interpolation(grad_x, xi, yi) for xi, yi in zip(xs, ys)])
    f_y = np.array([bilinear_interpolation(grad_y, xi, yi) for xi, yi in zip(xs, ys)])
    x_t = M @ (gamma * np.array(xs) - kappa * f_x)
    y_t = M @ (gamma * np.array(ys) - kappa * f_y)

    return x_t, y_t



if __name__ == '__main__':
    # Open file
    with open("../images/parameters.json", "r") as file:
        images = json.load(file)

    # Let the user choose one of the pic to operate
    print("Choose an image:")
    for idx, img_name in enumerate(images.keys()):
        print(f"{idx + 1}. {img_name}")
    choice = int(input("Enter the number corresponding to your choice: "))
    img_path = list(images.keys())[choice - 1]
    params = images[img_path]

    # Read the image
    img = cv2.imread('../images/' + img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    xs = []
    ys = []
    img_copy = img.copy()
    cv2.imshow('image', img_copy)

    # Let user choose points
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)

    # Get interpolated x, y
    n = params['n']
    xs, ys = interpolate_points(xs, ys, n)

    img_before = img.copy()
    if len(img_before.shape) == 2:  # Grayscale
        img_before = cv2.cvtColor(img_before, cv2.COLOR_GRAY2BGR)
    points = np.array(list(zip(xs, ys)), np.int32)
    points = points.reshape((-1, 1, 2))
    # Draw the contour
    cv2.polylines(img_before, [points], isClosed=True, color=(168, 96, 255), thickness=4)

    cv2.imshow('Interpolated Image', img_before)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    num_points = len(xs)

    #Get matrix
    M = get_matrix(params['alpha'], params['beta'], params['gamma'], num_points)

    #Get external energy
    kernel_size = (5, 5)
    sigma = 1.5
    img_blurred = cv2.GaussianBlur(img, kernel_size, sigma)
    E = external_energy(img_blurred, params['w_line'], params['w_edge'], params['w_term'])
    # Compute the gradient of the external energy
    grad_x = np.gradient(E)[1]
    grad_y = np.gradient(E)[0]

    for iteration in range(params['loop']):
        img_copy = img.copy()
        if len(img_copy.shape) == 2:
            img_copy = cv2.cvtColor(img_copy, cv2.COLOR_GRAY2BGR)

        # Get optimized x,y in each loop
        xs, ys = optimize_contour(xs, ys, M, grad_x, grad_y, params['kappa'], params['gamma'])

    # Draw the optimized points in each loop
        points = np.array(list(zip(xs, ys)), np.int32)
        points = points.reshape((-1, 1, 2))
        # Draw the contour
        cv2.polylines(img_copy, [points], isClosed=True, color=(20, 255, 57), thickness=4)
        cv2.imshow(f'Iteration {iteration}', img_copy)
        cv2.waitKey(2)

    # Show and save img
    combined = np.hstack((img_before, img_copy))
    save_path = 'images/' + img_path.split('.')[0] + "_combined.png"
    cv2.imwrite(save_path, combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

