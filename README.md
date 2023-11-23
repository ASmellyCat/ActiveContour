# ActiveContour
Active contour techniques for image segmentation

## Introduction
In the rapidly evolving field of image processing, the ability to accurately segment and represent images is of paramount importance. With a plethora of images available for analysis, selecting the right parameters for processing becomes a nuanced task that can significantly influence the outcomes. This report presents the outcomes of applying active contour techniques for image segmentation and details the optimal parameters for a range of images.

Our objectives, as outlined, are twofold:

1. To present visual results on the provided images. This will encompass several scenarios:
    - For binary images like circle, square, star, and shape, as well as the vase, our goal is to segment the objects seamlessly.
    - The dental image poses a unique challenge, where the task is to segment the row of teeth distinctly.
    - The intricacies of the brain image require us to segment not just the outer layer of the skull but also the inner contour of the brain matter.
    - A specific focus will also be given to the segmentation of the right eye hole.
2. As an optional challenge, we will also touch upon the bonus question, providing proof of our approach and detailing the steps undertaken.

## Parameters Explanation
The following are the definitions of the parameters used in the active contour method:

- `n`: Number of points on the initial contour.
- `loop`: Maximum number of iterations.
- `w_line`: Weight of line energy. Controls attraction to brightness.
- `w_edge`: Weight of edge energy. Controls attraction to edges.
- `w_term`: Weight of terminal energy. Control the convergence. 
- `alpha`: Length shape parameter. Control the contraction speed.
- `beta`: Smoothness shape parameter. Control the smoothness.
- `gamma`: Time step, or the rate of contour evolution.
- `kappa`: Balloon force, which either pushes the contour outwards or pulls it inwards.

## Visual Results
![circle_combined](https://github.com/ASmellyCat/ActiveContour/assets/110814688/f2f7aa22-ee55-4dfa-bb20-68f9f667a34f)

![square_combined](https://github.com/ASmellyCat/ActiveContour/assets/110814688/007cb22f-75f8-48ec-940b-33e66588d87b)

![vase_combined](https://github.com/ASmellyCat/ActiveContour/assets/110814688/98cb02ba-f720-48b6-95a1-eaa820a4d7dc)

![star_combined1](https://github.com/ASmellyCat/ActiveContour/assets/110814688/46772c93-57f5-4dbd-b217-9b9a79222771)

![shape_combined1](https://github.com/ASmellyCat/ActiveContour/assets/110814688/0000f4fb-069a-44fe-8ff3-141424019201)

![dental_combined](https://github.com/ASmellyCat/ActiveContour/assets/110814688/1e32f70f-c436-4cd1-8a8a-67e139cd12e8)

![brain_outter_combined2](https://github.com/ASmellyCat/ActiveContour/assets/110814688/a512eaf6-397f-4ce8-ad70-0ad4c6950960)

![brain_outter_combined1](https://github.com/ASmellyCat/ActiveContour/assets/110814688/15de146a-c0f4-4908-8545-5312bf83a674)

![brain_inner_combined](https://github.com/ASmellyCat/ActiveContour/assets/110814688/1caf4580-77e5-44d7-8b30-b0ef2f58d7be)

![brain_eye_combined2](https://github.com/ASmellyCat/ActiveContour/assets/110814688/a5734065-82cd-4eb3-bbf3-ee8b6bf5d541)

![brain_eye_combined1](https://github.com/ASmellyCat/ActiveContour/assets/110814688/8c0151e1-dba4-4694-a251-e090e497247e)

## Conclusion
In this documentation, we provided a comprehensive view of various images ranging from binary representations to more complex anatomical illustrations. The parameters associated with each image shed light on specific attributes that influence the interpretation and processing of these images. Notably, binary images such as circles, squares, and stars presented simpler structures, whereas the dental and brain images displayed intricate details which require more complex parameters for accurate representation. It's evident that the choice of parameters is crucial for image processing tasks, ensuring that the details and features of each image are accurately captured and represented.
