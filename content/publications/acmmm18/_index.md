+++

template = "publication.html"
title = "DASH for 3D Networked Virtual Environment"
date = 2018-10-01

[extra]
abstract = "DASH is now a widely deployed standard for streaming video content due to its simplicity, scalability, and ease of deployment. In this paper, we explore the use of DASH for a different type of media content -- networked virtual environment (NVE), with different properties and requirements. We organize a polygon soup with textures into a structure that is compatible with DASH MPD (Media Presentation Description), with a minimal set of view-independent metadata for the client to make intelligent decisions about what data to download at which resolution. We also present a DASH-based NVE client that uses a view-dependent and network dependent utility metric to decide what to download, based only on the information in the MPD file. We show that DASH can be used on NVE for 3D content streaming. Our work opens up the possibility of using DASH for highly interactive applications, beyond its current use in video streaming."
authors = ["Thomas Forgione", "Axel Carlier", "Géraldine Morin", "Wei Tsang Ooi", "Vincent Charvillat", "Praveen Kumar Yadav"]
publication = "ACMMM"
year = 2018

links = [
    { name = "Long paper", link = "/publications/acmmm18/long.pdf" },
    { name = "Demo paper", link = "/publications/acmmm18/demo.pdf" },
    { name = "Explicative video", link = "https://www.youtube.com/watch?v=tGruvbs_H0g" },
    { name = "Poster", link = "/publications/acmmm188/poster.pdf" },
    { name = "Online demos", link = "/demo" }
]

image = { path = "/publications/acmmm18/bigpicture.png", style="banner" }

# Optional featured image (relative to `static/img/` folder).
[header]
image = "../publications/acmmm18/bigpicture.png"
caption = "A $k$-d tree of a scene, with a camera and the visible cells"

+++

